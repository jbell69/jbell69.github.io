import pandas as pd

# create dataframe
data_table_df = pd.read_csv (r'/Resources/cities.csv')

#set index to City_ID
data_table_df.set_index('City_ID', inplace=True)

#renaming column and setting date
data_table_df.rename(columns = {'Lat':'Latitude', 
                              'Lng':'Longitude'}, inplace = True)
data_table_df = data_table_df.rename_axis('City ID')
data_table_df['Date'] = pd.to_datetime(data_table_df['Date'],unit='s')

# render dataframe as html
data_table_df.to_html("data_table_html.html")

#export file
data_table_file = open("data_table.html", "w")
data_table_file.write(html)
data_table_file.close()