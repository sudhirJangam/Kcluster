import pandas as pd
#from sklearn.cluster import KMeans

fields = [ 'Complaint ID','Company','Date received', 'Product', 'Sub-product', 'Issue', 'Sub-issue',
          'Consumer complaint narrative','Submitted via']
df = pd.read_csv(r'C:\Users\sudhi\Downloads\archive\Consumer_Complaints.csv', usecols=fields)
print(df.columns);
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
d1=df[df['Consumer complaint narrative'].notnull()]

#d1 = d1.reset_index(drop=True)
topdata=d1[0:100]
#d1["Date received"]=d1["Date received"].replace("\\")
#print(df['Consumer complaint narrative'].isna().sum())
print(d1.count())

print(d1)

#d1.to_csv(r'C:\Users\sudhi\Downloads\archive\100_Complaints.csv')


#df.to_csv(r(r'C:\Users\sudhi\Downloads\archive\Consumer_Complaints_vec.csv'))
#print(topdata)