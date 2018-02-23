
# coding: utf-8

# In[64]:

import pandas as pd
import logging
import os
# try:
#     os.remove("./Documents/Atlanta/FlowMeterGraphing/Test.csv")
# except OSError:
    # pass
col_names = ['SiteID', 'Timestamp','Reading','Unit']
filename = "INC-17.csv"
filename = filename.replace(".csv","") #testing for filename replacement
df= pd.read_csv('//423207-amviis1.mwhexternal.local/coatlanta/_output/INC-17.csv')
df2 = pd.read_csv('//423207-amviis1.mwhexternal.local/coatlanta/_output/Utoy Railroad.csv')
# df_test = pd.read_csv('./Documents/Atlanta/FlowMeterGraphing/Test.csv')
df.head()
df2.shape

# def return_col(x):
#     locid = 'na'
#     param = 'na'
    
#     if filename in x:
#         locid = filename

#     if x.SiteID.str.split(filename)[1] in ('Level', 'Rainfall', 'Velocity'):    
        
#         param = x.SiteID.str.split(filename)[1]

#     return (locid,param)



# In[65]:

df.drop_duplicates
df2.drop_duplicates
df.columns = col_names
df2.columns = col_names
df2 = df2[df2['Reading'] != 0 ]
# print(df.SiteID.str.split(filename)
df['LocationID'] = filename
# print(df.SiteID.str.split(filename)[0][1])
df['Property'] = df.SiteID.str.split(filename)[0][1]

# In[66]:

# df[df['Reading']!=0]


# In[67]:

df.to_csv('./TestRuns/Test.csv')
df2.to_csv('./TestRuns/Test.csv', mode = 'a', header = False)


# In[ ]:



