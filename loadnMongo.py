import pandas as pd
import json
from pymongo import MongoClient
from datetime import datetime

def loadData(df , opt):
        # Initialize MongoDB python client
        mongodb_conn_string = 'mongodb+srv://<UID>:<PASS>@mydb.sdiiymp.mongodb.net/?retryWrites=true&w=majority&appName=Mydb'
        db_name = "complaints_db"
        if (opt==0) :
           collection_name = "ClusterCenter"
        else:
           collection_name = "Complaints"

        client = MongoClient(mongodb_conn_string)
        collection = client[db_name][collection_name]

        # Reset w/out deleting the Search Index
        collection.delete_many({})


        dJson=df.to_json(orient='records', lines=False)


        data = json.loads(dJson)
        #print(data)
        for obj in data:
            if (opt==0) :
                mydict = { "cluster": obj["Unnamed: 0"] , "centerVec":eval(obj['embeddings']) }
            else:
                dt=datetime.strptime(obj['Date received'],'%m/%d/%Y').date()
                Appdt =datetime.fromisoformat(dt.isoformat())

                mydict = { "repoDt": Appdt ,"product": obj['Product'] , "subProduct":obj['Sub-product'],"issue":obj['Issue'],
                     "subIssue":obj['Sub-issue'],"complaint":obj['Consumer complaint narrative'],
                     "company":obj['Company'], "channel":obj['Submitted via'], "complaintId":obj['Complaint ID'],
                     "embeddings":eval(obj['embeddings']),"cluster":obj['cluster']}

                #print(mydict)
            x = collection.insert_one(mydict)
            print(mydict)


df = pd.read_csv(r'C:\Users\sudhi\Downloads\archive\512_complaints_embeded_final.csv')
fdf=df[['Date received',
            'Product', 'Sub-product', 'Issue', 'Sub-issue',
        'Consumer complaint narrative', 'Company', 'Submitted via',
        'Complaint ID', 'embeddings', 'cluster']]

loadData(fdf,1)

df = pd.read_csv(r'C:\Users\sudhi\Downloads\archive\512_complaints_embeded_centers.csv')
loadData(df,0)
