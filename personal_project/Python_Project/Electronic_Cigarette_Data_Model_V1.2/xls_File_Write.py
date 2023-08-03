import xlrd  # 引入Excel库的xlrd

def xls_File_Write(flie_path):
    filename = flie_path
    excel_data = xlrd.open_workbook(flie_path)
    excel_sheets0_data = excel_data.sheets()[0]
    return excel_sheets0_data
