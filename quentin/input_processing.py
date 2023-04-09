import pandas as pd
import ipywidgets as widgets
from IPython.display import display

#TODO REAL DATA PROCESSING & GENERATION

def getVariantData():
    df = pd.DataFrame(pd.read_excel(getExcelName(), header = None, index_col=0))
    df.index.name=None
    return df 

#TODO file extension check using regex
def getExcelName():
    excel_name = input("Please enter the name of the excel file: ")
    return excel_name

#def getExcelName():
#    text = widgets.Textarea(
#   value = input(),
#    placeholder='"example.xlsx"',
#    description='Filename:',
#    disabled=False
#    )
#    display(text)
#    return text.value



# def getExcelName():
#     while True:
#         excel_name = input("Please enter the name of the excel file: ")
#         if not re.match("(\S+(\\.(?i)(xlsx|xlsm|xlsb|xltx|xltm|xls|xlt|xls|xml|xlam|xla|xlw|xlr))$)", excel_name):
#             print ("Error! Incorrect input. Input example: 'variants.xlsx' ")
#         else:
#             #print("Hello "+ excel_name)
#             break

# df = getVariantData("input_example_excel.xlsx")
# print(df)
# print(df.iloc[:, [0]])
