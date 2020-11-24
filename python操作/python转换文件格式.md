# python转换文件格式

```
import win32com.client as wc

def do_save_as():
    """
    文件另存为，将doc文档转换成docx文档
    :return:
    """
    word = wc.Dispatch('Word.Application')
    doc = word.Documents.Open(r'D:\work\表清单20201029\再保系统数据结构(2012).doc')  # 目标路径下的文件
    doc.SaveAs(r'D:\work\表清单20201029\再保系统数据结构(2012).docx', 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件
    doc.Close()
    word.Quit()
```

需要安装pywin32模块

```
pip install pywin32 (--user)
```

## 转换xls到xlsx

```
def do_save_as(filename, excel):
    excel = wc.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(filename)
    wb.SaveAs(目标文件名, FileFormat=51)
    wb.Close()
    excel.Application.Quit()
```

