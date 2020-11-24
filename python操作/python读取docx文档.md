# python读取docx文档

安装python-docx模块

```
pip install python-docx
```

用法示例：

```
def read_docx(filename):
    document = docx.Document(filename)
    # print(document)
    # print(len(document.paragraphs))
    # print(len(document.tables))
    tables_content = []
    for table in document.tables:
        # print(table)
        # print(table.rows[:])
        table_content = []
        for i, row in enumerate(table.rows[:]):
            # print(i, row)
            row_content = []
            for cell in row.cells[:]:  # 读一行中的所有单元格
                c = cell.text
                row_content.append(c)
            # print(row_content)  # 以列表形式导出每一行数据
            # 将每行的数据添加到一个表中
            table_content.append(row_content)
        # 将每个表的数据添加到总表中
        tables_content.append(table_content)
    return tables_content
```

