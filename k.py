from sklearn.cluster import KMeans
import numpy as np
import pandas
import matplotlib.pyplot as plt
data1 = pandas.read_csv('Customers.csv',header=0)
print(data1)
data=data1.as_matrix(columns=None)
kmeans = KMeans(n_clusters=5, random_state=0).fit(data1)
print(kmeans.labels_)
labels=kmeans.labels_
print(kmeans.cluster_centers_)
centroid=kmeans.cluster_centers_
colors = ["g.","r.","c.","b.","y."]

for i in range(len(data)):
   plt.plot(data[i][0],data[i][1],colors[labels[i]],markersize=10)

plt.scatter(centroid[:,0],centroid[:,1], marker = "x", s=150, linewidths = 5, zorder =10)

plt.show()

