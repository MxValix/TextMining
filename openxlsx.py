import pandas as pd

if __name__ == '__main__':
    excel_name = 'textmining.xlsx'
    data = pd.read_excel(excel_name)
    print(data)
