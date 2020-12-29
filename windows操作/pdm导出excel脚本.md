# pdm导出excel脚本

## 1.一张表一个sheet，建目录

```
'******************************************************************************
Option Explicit
   Dim rowsNum,tablesNum
   rowsNum = 0
   tablesNum = 0
'-----------------------------------------------------------------------------
' Main function
'-----------------------------------------------------------------------------
' Get the current active model
    Dim Model
    Set Model = ActiveModel
    If (Model Is Nothing) Or (Not Model.IsKindOf(PdPDM.cls_Model)) Then
       MsgBox "The current model is not an PDM model."
    Else
      ' Get the tables collection
      '创建EXCEL APP
      dim beginrow
      DIM EXCEL,BOOK,SHEETLIST
      set EXCEL = CREATEOBJECT("Excel.Application")
      Set BOOK = EXCEL.Workbooks.Add(-4167) '新建工作簿
      BOOK.sheets(1).name ="目录"
      set SHEETLIST = BOOK.sheets("目录")
      ShowTableList Model,SHEETLIST

      ShowProperties Model,BOOK,SHEETLIST
      
      MsgBox "导出完成！"
      
 End If
'-----------------------------------------------------------------------------
' Show properties of tables
'-----------------------------------------------------------------------------
Sub ShowProperties(mdl,BOOK,SheetList)
   ' Show tables of the current model/package
   rowsNum=0
   beginrow = rowsNum+1
   Dim rowIndex 
   rowIndex=3
   ' For each table
   output "begin"
   Dim tab
   For Each tab In mdl.tables
      tablesNum = tablesNum +1
      ShowTable tab,BOOK,rowIndex,sheetList,tablesNum
      rowIndex = rowIndex +1
   Next
   if mdl.tables.count > 0 then
        BOOK.Sheets(BOOK.Sheets.count).Range("A" & beginrow + 1 & ":A" & rowsNum).Rows.Group
   end if
   output "end"
End Sub
'-----------------------------------------------------------------------------
' Show table properties
'-----------------------------------------------------------------------------
Sub ShowTable(tab, BOOK,rowIndex,sheetList,tablesNum)


   If IsObject(tab) Then
   
     
     Dim rangFlag,SHEET
     
     'EXCEL.workbooks.add(-4167)'添加工作表
     BOOK.Sheets.Add , BOOK.Sheets(BOOK.Sheets.count)
     BOOK.Sheets(BOOK.Sheets.count).Name = tab.code
     set SHEET = BOOK.sheets(tab.code)
      
     'EXCEL.workbooks(1).sheets.add(-4167)
      EXCEL.workbooks(1).Sheets(tablesNum).Select
      EXCEL.visible = true
      '设置列宽和自动换行
      sheet.Columns(1).ColumnWidth = 20 
      sheet.Columns(2).ColumnWidth = 20 
      sheet.Columns(3).ColumnWidth = 20 
      sheet.Columns(4).ColumnWidth = 40 
      sheet.Columns(5).ColumnWidth = 10 
      sheet.Columns(6).ColumnWidth = 10 
      sheet.Columns(1).WrapText =true
      sheet.Columns(2).WrapText =true
      sheet.Columns(4).WrapText =true
      '不显示网格线
      EXCEL.ActiveWindow.DisplayGridlines = False
      
     rowsNum = 0
     rowsNum = rowsNum + 1
      ' Show properties
      Output "================================"
      sheet.cells(rowsNum, 1) ="返回目录"
      sheet.cells(rowsNum, 2) =tab.name
      sheet.cells(rowsNum, 2).HorizontalAlignment=3
      sheet.cells(rowsNum, 3) = tab.code
      'sheet.cells(rowsNum, 5).HorizontalAlignment=3
      'sheet.cells(rowsNum, 6) = ""
      'sheet.cells(rowsNum, 7) = "表说明"
      sheet.cells(rowsNum, 4) = tab.comment
      'sheet.cells(rowsNum, 8).HorizontalAlignment=3
      sheet.Range(sheet.cells(rowsNum, 4),sheet.cells(rowsNum, 7)).Merge
      '设置超链接，从目录点击表名去查看表结构
      '字段中文名    字段英文名    字段类型    注释    是否主键    是否非空    默认值
      sheetList.Hyperlinks.Add sheetList.cells(rowIndex,2), "",tab.code&"!B"&rowsNum
      sheet.Hyperlinks.Add sheet.cells(rowsNum,1), "","目录"&"!B"&rowIndex
      rowsNum = rowsNum + 1
      sheet.cells(rowsNum, 1) = "字段中文名"
      sheet.cells(rowsNum, 2) = "字段英文名"
      sheet.cells(rowsNum, 3) = "字段类型"
      sheet.cells(rowsNum, 4) = "注释"
      sheet.cells(rowsNum, 5) = "是否主键"
      sheet.cells(rowsNum, 6) = "是否非空"
      sheet.cells(rowsNum, 7) = "默认值"
      '设置边框
      sheet.Range(sheet.cells(rowsNum-1, 1),sheet.cells(rowsNum, 7)).Borders.LineStyle = "1"
      'sheet.Range(sheet.cells(rowsNum-1, 4),sheet.cells(rowsNum, 9)).Borders.LineStyle = "1"
      '字体为10号
      sheet.Range(sheet.cells(rowsNum-1, 1),sheet.cells(rowsNum, 7)).Font.Size=10
            Dim col ' running column
            Dim colsNum
            colsNum = 0
      for each col in tab.columns
        rowsNum = rowsNum + 1
        colsNum = colsNum + 1
          sheet.cells(rowsNum, 1) = col.name
        'sheet.cells(rowsNum, 3) = ""
          'sheet.cells(rowsNum, 4) = col.name
          sheet.cells(rowsNum, 2) = col.code
          sheet.cells(rowsNum, 3) = col.datatype
        sheet.cells(rowsNum, 4) = col.comment
          If col.Primary = true Then
        sheet.cells(rowsNum, 5) = "Y" 
        Else
        sheet.cells(rowsNum, 5) = " " 
        End If
        If col.Mandatory = true Then
        sheet.cells(rowsNum, 6) = "Y" 
        Else
        sheet.cells(rowsNum, 6) = " " 
        End If
        sheet.cells(rowsNum, 7) =  col.defaultvalue
      next
      sheet.Range(sheet.cells(rowsNum-colsNum+1,1),sheet.cells(rowsNum,7)).Borders.LineStyle = "3"       
      'sheet.Range(sheet.cells(rowsNum-colsNum+1,4),sheet.cells(rowsNum,9)).Borders.LineStyle = "3"
      sheet.Range(sheet.cells(rowsNum-colsNum+1,1),sheet.cells(rowsNum,7)).Font.Size = 10
      rowsNum = rowsNum + 2
      
      Output "FullDescription: "       + tab.Name
   End If
   
End Sub
'-----------------------------------------------------------------------------
' Show List Of Table
'-----------------------------------------------------------------------------
Sub ShowTableList(mdl, SheetList)
   ' Show tables of the current model/package
   Dim rowsNo
   rowsNo=1
   ' For each table
   output "begin"
   SheetList.cells(rowsNo, 1) = "主题"
   SheetList.cells(rowsNo, 2) = "表中文名"
   SheetList.cells(rowsNo, 3) = "表英文名"
   SheetList.cells(rowsNo, 4) = "表说明"
   rowsNo = rowsNo + 1
   SheetList.cells(rowsNo, 1) = mdl.name
   Dim tab
   For Each tab In mdl.tables
     If IsObject(tab) Then
         rowsNo = rowsNo + 1
      SheetList.cells(rowsNo, 1) = ""
      SheetList.cells(rowsNo, 2) = tab.name
      SheetList.cells(rowsNo, 3) = tab.code
      SheetList.cells(rowsNo, 4) = tab.comment
     End If
   Next
    SheetList.Columns(1).ColumnWidth = 20 
      SheetList.Columns(2).ColumnWidth = 20 
      SheetList.Columns(3).ColumnWidth = 30 
     SheetList.Columns(4).ColumnWidth = 60 
   output "end"
End Sub
```

## 2.一张表一个sheet，会有表清单，没有目录

```
'****************************************************************************** 
'* File:     pdm2excel.txt 
'* Title:    pdm export to excel 
'* Purpose:  To export the tables and columns to Excel 
'* Model:    Physical Data Model 
'* Objects:  Table, Column, View 
'* Author:   Chirs 
'* Created:  2015-01-28 
'* Version:  1.0 
'****************************************************************************** 
Option Explicit 
   Dim rowsNum 
   rowsNum = 0 
'----------------------------------------------------------------------------- 
' Main function 
'----------------------------------------------------------------------------- 
' Get the current active model 
Dim Model 
Set Model = ActiveModel 
If (Model Is Nothing) Or (Not Model.IsKindOf(PdPDM.cls_Model)) Then 
  MsgBox "The current model is not an PDM model." 
Else 
 ' Get the tables collection 
 '创建EXCEL APP 
 
 
Dim beginrow
 Dim EXCEL, BOOK, SHEET
 Set EXCEL = CreateObject("Excel.Application")
 EXCEL.Visible = True
 Set BOOK = EXCEL.Workbooks.Add(-4167) '新建工作簿
 
 BOOK.Sheets(1).Name = "数据库表结构"
 Set SHEET = EXCEL.workbooks(1).sheets("数据库表结构")
 
 ShowProperties Model, SHEET
 EXCEL.visible = true 
 '设置列宽和自动换行 
 SHEET.Columns(1).ColumnWidth = 10   
 SHEET.Columns(2).ColumnWidth = 30   
 SHEET.Columns(3).ColumnWidth = 20   
 
 SHEET.Columns(1).WrapText =true 
 SHEET.Columns(2).WrapText =true 
 SHEET.Columns(3).WrapText =true 
 
End If
 
'----------------------------------------------------------------------------- 
' Show properties of tables 
'----------------------------------------------------------------------------- 
Sub ShowProperties(mdl, sheet) 
   ' Show tables of the current model/package 
   rowsNum=0 
   beginrow = rowsNum+1 
   ' For each table 
   output "begin" 
   Dim tab 
   For Each tab In mdl.tables 
      ShowTable tab,sheet 
   Next 
   if mdl.tables.count > 0 then 
        sheet.Range("A" & beginrow + 1 & ":A" & rowsNum).Rows.Group 
   end if 
   output "end" 
End Sub
 
'----------------------------------------------------------------------------- 
' 数据表查询 
'-----------------------------------------------------------------------------
Sub ShowTable(tab, sheet)   
   If IsObject(tab) Then 
     Dim rangFlag
      sheet.cells(1, 1) = "序号" 
      sheet.cells(1, 2) = "表名"
      sheet.cells(1, 3) = "实体名"
      '设置边框 
      sheet.Range(sheet.cells(1, 1),sheet.cells(1, 3)).Borders.LineStyle = "1"
      '设置背景颜色
      sheet.Range(sheet.cells(1, 1),sheet.cells(1, 3)).Interior.ColorIndex = "19"
 
      rowsNum = rowsNum + 1
      sheet.cells(rowsNum+1, 1) = rowsNum 
      sheet.cells(rowsNum+1, 2) = tab.code
      sheet.cells(rowsNum+1, 3) = tab.name
      '设置边框
      sheet.Range(sheet.cells(rowsNum+1,1),sheet.cells(rowsNum+1,3)).Borders.LineStyle = "2"
 
      '增加Sheet
      BOOK.Sheets.Add , BOOK.Sheets(BOOK.Sheets.count)
      BOOK.Sheets(rowsNum+1).Name = tab.code 
 
      Dim shtn
      Set shtn = EXCEL.workbooks(1).sheets(tab.code)
      '设置列宽和换行
       shtn.Columns(1).ColumnWidth = 30   
       shtn.Columns(2).ColumnWidth = 20   
       shtn.Columns(3).ColumnWidth = 20
       shtn.Columns(5).ColumnWidth = 30   
       shtn.Columns(6).ColumnWidth = 20   
 
       shtn.Columns(1).WrapText =true 
       shtn.Columns(2).WrapText =true 
       shtn.Columns(3).WrapText =true
       shtn.Columns(5).WrapText =true 
       shtn.Columns(6).WrapText =true
 
       '设置列标题
       shtn.cells(1, 1) = "字段中文名" 
       shtn.cells(1, 2) = "字段名"
       shtn.cells(1, 3) = "字段类型"
       shtn.cells(1, 5) = tab.code
       shtn.cells(1, 6) = tab.Name
       '设置边框 
       shtn.Range(shtn.cells(1, 1),shtn.cells(1, 3)).Borders.LineStyle = "1"
       shtn.Range(shtn.cells(1, 5),shtn.cells(1, 6)).Borders.LineStyle = "1"
       '设置背景颜色
       shtn.Range(shtn.cells(1, 1),shtn.cells(1, 3)).Interior.ColorIndex = "19"
       shtn.Range(shtn.cells(1, 5),shtn.cells(1, 6)).Interior.ColorIndex = "19"
 
      Dim col ' running column 
      Dim colsNum
      Dim rNum 
      colsNum = 0
      rNum = 0 
            for each col in tab.columns 
              rNum = rNum + 1 
              colsNum = colsNum + 1 
 
            shtn.cells(rNum+1, 1) = col.name 
            shtn.cells(rNum+1, 2) = col.code 
            shtn.cells(rNum+1, 3) = col.datatype 
            next 
            shtn.Range(shtn.cells(rNum-colsNum+2,1),shtn.cells(rNum+1,3)).Borders.LineStyle = "2"         
            rNum = rNum + 1 
 
            Output "FullDescription: "       + tab.Name
 
   End If   
End Sub
```

## 3.所有的表在同一个 Sheet 页中

```
'******************************************************************************
'* File:     pdm2excel.txt
'* Title:    pdm export to excel
'* Purpose:  To export the tables and columns to Excel
'* Model:    Physical Data Model
'* Objects:  Table, Column, View
'* Author:   ziyan
'* Created:  2012-05-03
'* Version:  1.0
'******************************************************************************
Option Explicit
   Dim rowsNum
   rowsNum = 0
'-----------------------------------------------------------------------------
' Main function
'-----------------------------------------------------------------------------
' Get the current active model
Dim Model
Set Model = ActiveModel
If (Model Is Nothing) Or (Not Model.IsKindOf(PdPDM.cls_Model)) Then
  MsgBox "The current model is not an PDM model."
Else
 ' Get the tables collection
 '创建EXCEL APP
 dim beginrow
 DIM EXCEL, SHEET
 set EXCEL = CREATEOBJECT("Excel.Application")
 EXCEL.workbooks.add(-4167)'添加工作表
 EXCEL.workbooks(1).sheets(1).name ="test"
 set sheet = EXCEL.workbooks(1).sheets("test")
 
 ShowProperties Model, SHEET
 EXCEL.visible = true
 '设置列宽和自动换行
 sheet.Columns(1).ColumnWidth = 20 
 sheet.Columns(2).ColumnWidth = 40 
 sheet.Columns(4).ColumnWidth = 20 
 sheet.Columns(5).ColumnWidth = 20 
 sheet.Columns(6).ColumnWidth = 15 
 sheet.Columns(1).WrapText =true
 sheet.Columns(2).WrapText =true
 sheet.Columns(4).WrapText =true
 End If
'-----------------------------------------------------------------------------
' Show properties of tables
'-----------------------------------------------------------------------------
Sub ShowProperties(mdl, sheet)
   ' Show tables of the current model/package
   rowsNum=0
   beginrow = rowsNum+1
   ' For each table
   output "begin"
   Dim tab
   For Each tab In mdl.tables
      ShowTable tab,sheet
   Next
   if mdl.tables.count > 0 then
        sheet.Range("A" & beginrow + 1 & ":A" & rowsNum).Rows.Group
   end if
   output "end"
End Sub
'-----------------------------------------------------------------------------
' Show table properties
'-----------------------------------------------------------------------------
Sub ShowTable(tab, sheet)
   If IsObject(tab) Then
     Dim rangFlag
     rowsNum = rowsNum + 1
      ' Show properties
      Output "================================"
      sheet.cells(rowsNum, 1) = "实体名"
      sheet.cells(rowsNum, 2) =tab.name
      sheet.cells(rowsNum, 3) = ""
      sheet.cells(rowsNum, 4) = "表名"
      sheet.cells(rowsNum, 5) = tab.code
      sheet.Range(sheet.cells(rowsNum, 5),sheet.cells(rowsNum, 6)).Merge
      rowsNum = rowsNum + 1
      sheet.cells(rowsNum, 1) = "属性名"
      sheet.cells(rowsNum, 2) = "说明"
      sheet.cells(rowsNum, 3) = ""
      sheet.cells(rowsNum, 4) = "字段中文名"
      sheet.cells(rowsNum, 5) = "字段名"
      sheet.cells(rowsNum, 6) = "字段类型"
      '设置边框
      sheet.Range(sheet.cells(rowsNum-1, 1),sheet.cells(rowsNum, 2)).Borders.LineStyle = "1"
      sheet.Range(sheet.cells(rowsNum-1, 4),sheet.cells(rowsNum, 6)).Borders.LineStyle = "1"
Dim col ' running column
Dim colsNum
colsNum = 0
      for each col in tab.columns
        rowsNum = rowsNum + 1
        colsNum = colsNum + 1
      sheet.cells(rowsNum, 1) = col.name
      sheet.cells(rowsNum, 2) = col.comment
        sheet.cells(rowsNum, 3) = ""
      sheet.cells(rowsNum, 4) = col.name
      sheet.cells(rowsNum, 5) = col.code
      sheet.cells(rowsNum, 6) = col.datatype
      next
      sheet.Range(sheet.cells(rowsNum-colsNum+1,1),sheet.cells(rowsNum,2)).Borders.LineStyle = "2"       
      sheet.Range(sheet.cells(rowsNum-colsNum+1,4),sheet.cells(rowsNum,6)).Borders.LineStyle = "2"
      rowsNum = rowsNum + 1
 
      Output "FullDescription: "       + tab.Name
   End If
End Sub
```

