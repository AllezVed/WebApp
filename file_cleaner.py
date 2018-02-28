import numpy as np
import pandas as pd
import logging
import os
try:
    os.remove("Test.csv")
except OSError:
    print('Error, File not found')
    
col_names = ['SiteID', 'Timestamp','Reading','Unit']

path = '//423207-amviis1.mwhexternal.local/coatlanta/_output/'

def is_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

# filenames = ['1371 Kimberly Way -SSO.csv', 'INC-17.csv']
for filename in os.listdir(path):
        # if filename not in ('111.csv', '1371 Kimberly Way -SSO.csv'):
        #     break
    print(filename)
    if not is_non_zero_file(os.path.join(path,filename)):
        continue

# df2 = pd.read_csv('//423207-amviis1.mwhexternal.local/coatlanta/_output/Utoy Railroad.csv')
# # df_test = pd.read_csv('./Documents/Atlanta/FlowMeterGraphing/Test.csv')
# df.head()
# df2.shape


# # In[65]:
    
    df = pd.read_csv(os.path.join(path, filename), names = col_names, parse_dates= ['Timestamp'] , index_col = ['Timestamp'])
    if df.empty:
        continue
    df = df[df['Reading'].apply(lambda x: type(x) in [int, np.int64, float, np.float64])]
    df.drop_duplicates(inplace = True)
    df.dropna(inplace = True)
    # df2.drop_duplicates
    # df.columns = col_names
    # df2.columns = col_names
    # df = df[df['Reading'] != 0 ]
    def col_splitter(x):
        loc_id = 'na'
        param = 'na'
        location = filename.replace('.csv','')
        if location in x:
            loc_id = location
        if (location in x) and (len(x.split(location)[1]) != 0):
            param = x.split(location)[1]
        
        return loc_id, param
        
    # df['Property'] = df['SiteID'].str.split(filename.replace(".csv",""),1)
#         filename_check = filename.replace(".csv", "")
#         df['LocationID'] = filename_check
# # print(df.SiteID.str.split(filename)[0][1])
#         df['Property'] = df.SiteID.str.split(filename_check)[0][1]

    # # In[66]:I

    # # df[df['Reading']!=0]

    df['LocationID'] , df['Property'] = zip(*df['SiteID'].apply(col_splitter))
    # # In[67]:

    df.to_csv('Test.csv', mode = 'a', index = True, header = False)
        # df2.to_csv('./Documents/Atlanta/FlowMeterGraphing/Test.csv', mode = 'a', header = False)


        # # In[ ]:
