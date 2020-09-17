# This program goes through each Excel file and changes the
# sheet names to "Sheet1".
# NOTE: Each Excel file only has one sheet, so there is no
# conflict with sheet names

import openpyxl
from os import walk
from os.path import isfile, join

PATH = r"C:\Users\AJ\Desktop\Finance_Analysis_PowerBI\Finance_Data"
NEW_SHEET_NAME = "Sheet1"

for path, _, files in walk(PATH):
    for file in files:
        file_path = join(path, file)

        if isfile(file_path):

            workbook = openpyxl.load_workbook(file_path)
            all_sheets = workbook.sheetnames

            for sheet_name in all_sheets:
                workbook[sheet_name].title = NEW_SHEET_NAME
                workbook.save(file_path)
                workbook.close()