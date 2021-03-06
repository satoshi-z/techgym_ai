import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import re
import csv
import numpy as np

# graph
from matplotlib import pylab as plt

# グラフを横長にする
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

import matplotlib as mpl
mpl.rcParams['font.family'] = ['AppleGothic']

# データ加工
df = pd.read_csv("words2vector.csv")
tags2vec = []
for v in df["vectors"].values:
    value = map(float, v.strip("\n[]").split())
    tags2vec.append(list(value))

df_vec = pd.DataFrame(data=tags2vec, index=df["words"])

# 次元削減
pca = PCA(n_components=2)
pca.fit(df_vec)
existing_2d            = pca.transform(df_vec)
existing_df_2d         = pd.DataFrame(existing_2d)
existing_df_2d.index   = df_vec.index
existing_df_2d.columns = ['PC1','PC2']
existing_df_2d.head()

# クラスタリング
kmeans = KMeans(n_clusters=20)
clusters = kmeans.fit(df_vec)
existing_df_2d['cluster'] = pd.Series(clusters.labels_, index=existing_df_2d.index)

existing_df_2d.plot(
        kind="scatter",
        x = "PC2", y = "PC1",
        c=existing_df_2d.cluster.astype(np.float),
        figsize=(16,8))
plt.show()
