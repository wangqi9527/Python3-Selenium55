# coding=utf-8

import xlrd
import getcwd
import os

def read_xlrd(excelFile):
   data = xlrd.open_workbook(excelFile)
   table = data.sheet_by_index(0)
   dataFile = []

   for rowNum in range(table.nrows):
       # if 去掉表头
       if rowNum > 0:
           dataFile.append(table.row_values(rowNum))

   return dataFile


if __name__ == '__main__':
    path = getcwd.get_cwd()
    file_path = os.path.join(path, 'Excel/students.xlsx')
    yuangong=read_xlrd(excelFile=file_path)

    print(yuangong[1])
