import pandas as pd

##############################################################################################################################
######################################################READING FROM FILES(.to_string - PRINT ENTIRE DATAFRAME)
df1 = pd.read_csv('./working_with_files/table.csv')
print(df1)
# print(df1.to_string())

df2 = pd.read_json('./working_with_files/table.json')
print(df2)
# print(df1.to_string())

df3 = pd.read_excel('./working_with_files/table.xlsx')
print(df3)
# print(df1.to_string())

df4 = pd.read_fwf('./working_with_files/table.txt', delimiter=" ") # read_table working with delimiter
print(df4)
# print(df1.to_string())

######################################################READ FIRST AND LAST n ROWS(WITHOUT PARAMETER READS 5 ROWS)
df1 = df1.head()
print(df1)

df2 = df2.tail()
print(df2)

df3 = df3.head(10)
print(df3)

df4 = df4.tail(10)
print(df4)

################################################PRINT DATAFRAMES INFO(ALSO SHOW HOW MANY NULL AND NOT NULL VALUES HAVE COLUMNS)
print(df1.info())
print(df2.info()) 
print(df1.info()) 
print(df4.info())