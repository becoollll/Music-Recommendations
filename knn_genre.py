import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

def knn_genre(genres):
    df = pd.read_csv('data_by_genres.csv')

    # Use selected features
    features = ['acousticness', 'danceability', 'instrumentalness', 'speechiness', 'tempo']
    X = df[features].values
    y = df['genres'].values

    # Standardize all features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    knn = KNeighborsClassifier(n_neighbors=15)

    knn.fit(X_scaled, y)

    # specified music genre
    target = genres



    # Predict the top 3 most relevant genres
    ret_genres = []
    
    for i in range(len(target)):
        try:
            target_idx = list(df['genres']).index(target[i])
            target_features = X_scaled[target_idx].reshape(1, -1)
            nearest_neighbors = knn.kneighbors(target_features, n_neighbors=4, return_distance=False)

            # the most relevant genre
            most_similar_genres = [y[i] for i in nearest_neighbors[0]]
            for tmp in most_similar_genres[1:]:
                ret_genres.append(tmp)
                
            #ret_genres.append(most_similar_genres[1:])
            #print(f'與{target[i]}最相近的三個音樂種類:', most_similar_genres[1:])
        except:
            ### Some genres might be missing from the dataset
            print(f"'{target[i]}' doesn't exist in dataset.")
    
    ## Remove duplicate genres
    return list(dict.fromkeys(ret_genres))