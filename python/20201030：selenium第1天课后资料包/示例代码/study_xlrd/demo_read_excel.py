import xlrd

# 打开Excel文件，获取文件对象
wb = xlrd.open_workbook(r"E:\testdata.xlsx")

# 根据工作薄文件中的标签页的标题，获取一个标签页对象
sheet = wb.sheet_by_name("用户数据")

# 从标签页对象中，获取指定行和列的单元格中的值
print(sheet.cell_value(1,1))
print(sheet.cell_value(1,2))