import openpyxl as xl
from openpyxl.chart import BarChart, Reference

workbook = xl.load_workbook(
    'pradeep/tutorial2/projects/xl_processor/transactions.xlsx')

sheet1 = workbook['Sheet1']
cell = sheet1['a1']
cell = sheet1.cell(1, 1)

print(cell.value)

for row in range(2, sheet1.max_row + 1):
    cell = sheet1.cell(row, 3)
    print(cell.value)
    corrected_value = cell.value * 0.9
    corrected_price_cell = sheet1.cell(row, 4)
    corrected_price_cell.value = corrected_value

values = Reference(sheet1,
                   min_row=2,
                   max_row=sheet1.max_row,
                   min_col=4,
                   max_col=4)

chart1 = BarChart()
chart1.add_data(values)
sheet1.add_chart(chart1)

workbook.save(
    'pradeep/tutorial2/projects/xl_processor/corrected_transactions.xlsx')
