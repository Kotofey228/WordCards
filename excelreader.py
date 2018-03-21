from openpyxl import load_workbook

wb = load_workbook(filename = 'test.xlsx')
sheet = wb.active
print(sheet['D5'].value)