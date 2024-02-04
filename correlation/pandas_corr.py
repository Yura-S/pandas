import pandas as pd

pd.options.display.max_rows = 100
##############################################################################################################################
######################################################SHOWING DEPENDENCIES OF VALUES FOR NUMERIC COLUMNS(TO EACH OTHER)
df = pd.read_excel('./correlation/table.xlsx')
print(df)
df_correlation = df[["SalesTaxRateID", "StateProvinceID", "TaxType", "TaxRate"]].corr() #ONLY NUMBERS
print(df_correlation)