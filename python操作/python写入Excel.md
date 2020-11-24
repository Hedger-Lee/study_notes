# python写入Excel

## 安装xlwt模块

```
pip install xlwt
```

用法示例：

```
def write_to_excel(tables_content, des_file):
    wb = xlwt.Workbook(encoding='utf-8')
    st = wb.add_sheet("农险理赔")
    index = 0
    for i, table_content in enumerate(tables_content[:]):
        if i == 0:
            continue
        st.write(index, 0, i)
        # 该循环写入一个表格信息
        for row_content in table_content:
            # 该循环写入一行信息
            for j, cell in enumerate(row_content[:]):
                if '--' in cell:
                    cell = cell.replace('--**', '')
                st.write(index, j+1, cell)
            index += 1
    wb.save(des_file)
```
