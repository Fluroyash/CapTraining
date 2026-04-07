import openpyxl
def get_test_data():
    wb = openpyxl.load_workbook('sample.xlsx')
    wb = wb['sheet1']

    data = []

    for row in wb.iter_rows(min_row=2, values_only=True):
        data.append(row)

    return data
print(get_test_data())
\





