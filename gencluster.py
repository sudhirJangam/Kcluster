import pandas as pd
from sklearn.cluster import KMeans
import numpy as np



df = pd.read_csv(r'C:\Users\sudhi\Downloads\archive\512_Complaints_embed.csv')
print(df.columns);
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
#print(df.to_json(orient = "records"))

columns=[]
for i in range(0,512):
    columns.append(str(i))

y=[]
for i in df.index:
    #print (len(df["embeddings"][i]))
    em=df["embeddings"][i]
    el = em.replace("[","").replace("]","").split(",")
    #y = em.split(",")
    y.append(el)
    #dataset = list(zip(x,y))


#  print("length in list ==>", y[0])
ndf = pd.DataFrame(y,
                   columns =columns)
model = KMeans(n_clusters = 6, init = "k-means++")
label = model.fit_predict(ndf)

dat1 = pd.DataFrame({'cluster': label})
result = pd.concat([df, dat1], axis=1, join="inner")
centers = np.array(model.cluster_centers_)
centers.shape
centerDF = pd.DataFrame({'embeddings': centers.tolist()})

centerDF.to_csv(r'C:\Users\sudhi\Downloads\archive\512_complaints_embeded_centers.csv')
result.to_csv(r'C:\Users\sudhi\Downloads\archive\512_complaints_embeded_final.csv')

