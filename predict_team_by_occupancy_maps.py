import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn import neighbors, metrics
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

from codes.data_parsers.stats_bomb.json_directories import JsonDirectories


def predict_team_by_occupancy_maps(play_segments_length, x_bins, y_bins, train_occurances, k):
    maps_to_train, maps_to_test = prepare_maps(train_occurances, play_segments_length, x_bins, y_bins)
    knn = neighbors.KNeighborsClassifier(n_neighbors=k, p=2, weights = 'uniform')\
        .fit(maps_to_train['occupancy_map'].tolist(), maps_to_train['team'].tolist())
    pred = knn.predict(maps_to_test['occupancy_map'].tolist())
    return metrics.accuracy_score(maps_to_test['team'].tolist(), pred)


def prepare_maps(train_occurances, play_segment_length, x_bins, y_bins):
    json_directories = JsonDirectories()
    maps = pd.read_pickle(json_directories.create_occupancy_maps_pkl_path(play_segment_length, x_bins, y_bins))
    # maps = maps[filterDataByTeamsOccurancesMoreThan(list(maps['team']), 10)]
    maps = maps[filterEnglishWomanTeams(list(maps['team']))]
    unique_teams = getUniqueTeams(list(maps['team']))
    # showDataPCA(maps, unique_teams)
    # showDataTSNE(maps, unique_teams)

    train_maps, test_maps = subsetTrainAndTestSet(maps, train_occurances, unique_teams)
    # do_lda_transform(train_maps, test_maps, 11)
    changeTeamsForIndexes(train_maps, unique_teams)
    changeTeamsForIndexes(test_maps, unique_teams)

    return train_maps, test_maps

def do_lda_transform(train_maps, test_maps, classes_cnt):
    sc = StandardScaler()
    lda = LDA(n_components=classes_cnt)
    lda_train_maps = lda.fit_transform(sc.fit_transform(list(train_maps['occupancy_map'])), list(train_maps['team']))
    train_maps.drop(columns=['occupancy_map'])
    train_maps['occupancy_map'] = pd.DataFrame(lda_train_maps).apply(lambda r: tuple(r), axis=1).apply(np.array)
    lda_test_maps = (lda.transform(sc.transform(list(test_maps['occupancy_map']))))
    test_maps.drop(columns=['occupancy_map'])
    test_maps['occupancy_map'] = pd.DataFrame(lda_test_maps).apply(lambda r: tuple(r), axis=1).apply(np.array)
    return train_maps, test_maps

def filterDataByTeamsOccurancesMoreThan(teams, occurances_cnt):
    unique_teams = getUniqueTeams(teams)
    occurances = {}
    for i in range(0,len(unique_teams)):
        cnt = teams.count(unique_teams[i])
        if cnt >= occurances_cnt and unique_teams[i] != 'FC Barcelona':
            occurances[unique_teams[i]] = True
        else:
            occurances[unique_teams[i]] = False
    return [occurances[team] for team in teams]

def filterEnglishWomanTeams(teams):
    legit_teams = ['Reading WFC','West Ham United LFC','Manchester City WFC','Bristol City WFC','Arsenal WFC','Brighton & Hove Albion WFC','Everton LFC','Birmingham City WFC','Yeovil Town LFC','Chelsea FCW','Liverpool WFC']
    return [team in legit_teams for team in teams]

def subsetTrainAndTestSet(data, team_train_occurances, unique_teams):
    train_set = pd.DataFrame()
    test_set = pd.DataFrame()
    for id in unique_teams:
        train_set = train_set.append(data.loc[data['team'] == id].iloc[1:team_train_occurances, ])
        test_set = test_set.append(data.loc[data['team'] == id].iloc[team_train_occurances+1:, ])

    return train_set, test_set

def changeTeamsForIndexes(data, unique_teams):
    for index, row in data.iterrows():
        row['team'] = unique_teams.index(row['team'])

def getUniqueTeams(teams):
    return list(set(teams))

def showDataPCA(dataframes, unique_teams):
    data = StandardScaler().fit_transform(list(dataframes['occupancy_map']))
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(data)
    principalDf = pd.DataFrame(data=principalComponents
                               , columns=['component 1', 'component 2'])
    t = dataframes[['team']]
    t = t.set_index(pd.Index(range(0,len(t))))
    finalDf = pd.concat([t, principalDf], axis=1)
    makeGraph(finalDf, unique_teams, 'PCA')

def showDataTSNE(dataframes, unique_teams):
    data = list(dataframes['occupancy_map'])
    tsne = TSNE(n_components=2)
    principalComponents = tsne.fit_transform(data)
    principalDf = pd.DataFrame(data=principalComponents
                               , columns=['component 1', 'component 2'])
    t = dataframes[['team']]
    t = t.set_index(pd.Index(range(0,len(t))))
    finalDf = pd.concat([t, principalDf], axis=1)
    makeGraph(finalDf, unique_teams, 'TSNE')

def makeGraph(dataframes, unique_teams, plot_title):
    if(plot_title == 'PCA'):
        axis_range = [-16,16]
    else:
        axis_range = [-30, 30]
    fig = go.Figure()
    fig.update_layout(
        title=go.layout.Title(
            text=plot_title,
            xref="paper",
            x=0
        ),
        xaxis=dict(
            nticks=10, range=axis_range, ),
        yaxis=dict(
            nticks=10, range=axis_range, )
    )
    targets = unique_teams
    for target in targets:
        indicesToKeep = dataframes['team'] == target
        fig.add_trace(go.Scatter(
            x=list(dataframes.loc[indicesToKeep, 'component 1']),
            y=list(dataframes.loc[indicesToKeep, 'component 2']),
            name=target,
            mode="markers",
            marker = dict(colorscale="Spectral")))
    fig.show()