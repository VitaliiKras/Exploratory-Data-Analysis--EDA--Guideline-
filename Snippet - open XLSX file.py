import pandas as pd
pd.set_option('display.max_rows', None)

# documentaiton about Python Pandas read_excel() function
#       https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.parse.html
#
#       pandas.ExcelFile.parse
#
#       pd.ExcelFile.parse(sheet_name=0, header=0, names=None, index_col=None, usecols=None, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, parse_dates=False, date_format=None, thousands=None, comment=None, skipfooter=0, dtype_backend=<no_default>, **kwds)
    

# quick video tip
#       https://youtu.be/ual8QWlEQH4?si=prLkWFSCqNSnJne0
#       https://youtu.be/ual8QWlEQH4?si=D2KxkdOtnEeMUhhY

df = pd.read_excel(r"Exploratory-Data-Analysis--EDA--Guideline-\kodifikator - семплування.xlsx", sheet_name=None)
#print(df)
print(df.keys())

print(df.get('Області').head(3)) # first 3 rows of the sheet 'Області'
print(df.get('Області').tail(3)) # last 3 rows of the sheet 'Області'


print("--- Information about 'Області' ---")
print(df.get('Області').info()) # information about the dataframe of the sheet 'Області'
# FYI for each column there info value is printed

print("--- Count of non-null values ---")
print(str(df.get('Області').count())) # information about the dataframe of the sheet 'Області'
# FYI foreach column there counting of non-null values is printed


#ExcelFile = pd.ExcelFile(r"Exploratory-Data-Analysis--EDA--Guideline-\kodifikator - семплування.xlsx")
#print(ExcelFile.sheet_names)

