import pandas as pd

pd.options.display.max_rows = 200
#############################################################################################################################
######################################################READING DATA FROM EXCEL FILE
df1 = pd.read_excel('./clear_data/table.xlsx')

######################################################REMOVE ROWS THAT HAVE EMPTY CELLS AND ADD TO NEW DATAFRAME
df2 = df1.dropna()
# print(df2)

######################################################CHANGE ORIGINAL DARAFRAME(df)
df1.dropna(inplace = True)
# print(df1)

######################################################REPLACE NULL VALUES TO 1
df3 = pd.read_excel('./clear_data/table.xlsx')
df3.fillna(1, inplace = True)
# print(df3)

######################################################REPLACE NULL VALUES OF PhoneNumber to 000-000-0000
df4 = pd.read_excel('./clear_data/table.xlsx')
df4["PhoneNumber"].fillna('000-000-0000', inplace = True)
# print(df4)

######################################################TRYING TO CONVERT ModifiedDate CELLS TO DATETIME FORMAT
######################################################WHAT CAN CONVERT CONVERTS, FOR EXAMPLE NULLS CAN'T
df5 = pd.read_excel('./clear_data/table.xlsx')
df5['ModifiedDate'] = pd.to_datetime(df5['ModifiedDate'])
# print(df5)

######################################################NULLS CAN BE DROPPED
df5.dropna(subset=['ModifiedDate'], inplace = True)
# print(df5)

######################################################FIXING DATA BY HAND
df6 = pd.read_excel('./clear_data/table.xlsx')

for x in df6.index:
  if df6.loc[x, "PhoneNumberTypeID"] > 1:
    df6.loc[x, "PhoneNumberTypeID"] = 3 #OR REMOVE BY df6.drop(x, inplace = True)

# print(df6)

######################################################SHOW DUBLICATES(BY TRUE) AND DROP THEM
df7 = pd.read_excel('./clear_data/table.xlsx')
# print(df7.duplicated())
df7.drop_duplicates(inplace = True)
# print(df7)