import os
csvs = [csv for csv in os.listdir('data') if '.csv' in csv]

df = pd.DataFrame()

for csv in tqdm(csvs):
    df_ = pd.read_csv('data/' + csv )
    df = pd.concat((df,df_))

df.to_csv('data.csv', index = False)
