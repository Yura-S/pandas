import pandas as pd

#############################################################################################################INFO ABOUT PANDAS
######################################################PANDAS VERSION
print(pd.__version__)

######################################################MAXIMUM SHOWED ROWS(COLUMNS) / CHANGING IT
print(pd.options.display.max_rows) 
pd.options.display.max_rows = 1000
# pd.options.display.max_columns = 1000

########################################################################################################################SERIES
######################################################CREATE SERIES(ONE COLUMN) FROM LIST
a = [1, 2, 3]
var1 = pd.Series(a)
print(var1)

######################################################TAKE ONE ELEMENT FROM SERIES
print(var1[0])

######################################################CREATE BY NAMING ROWS OF SERIES AND TAKE ONE ELEMENT BY NAME
var2 = pd.Series(a, index = ["first_row", "second_row", "third_row"])
print(var2["third_row"])

######################################################CREATE SERIES(TABLE) FROM DICTIONARY
foods = {"apple": 15, "pear": 18, "peach": 20}
var3 = pd.Series(foods, index = ["apple", "peach"])
print(var3)

###################################################################################################################DATAFRAMES
######################################################CREATE DATAFRAME(TABLE) FROM DICTIONARY
mydataset = {
  'people': ["Anna", "Vahe", "Mariam"],
  'height': [165, 168, 166]
}
var4 = pd.DataFrame(mydataset)
print(var4)

######################################################GET ROW(S) INFORMATION BY ROW NUMBER
print(var4.loc[0])
print(var4.loc[[0, 1]])

######################################################CREATE BY NAMING ROWS OF DATAFRAME AND GET BY NAME
var5 = pd.DataFrame(mydataset, index = ["human1", "human2", "human3"])
print(var5.loc["human2"])