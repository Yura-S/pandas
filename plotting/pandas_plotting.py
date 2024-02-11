import pandas as pd
import matplotlib.pyplot as plt

##############################################################################################################################
######################################################DRAW PLOT FROM DATAFRAME
df = pd.read_excel('./plotting/table.xlsx')
df[["SalesTaxRateID", "StateProvinceID", "TaxType", "TaxRate"]].plot()
plt.show()