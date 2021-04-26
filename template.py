#!/usr/bin/python3
# -*- coding: utf-8 -*-
# pip3 install xlutils
import xlrd
import xlwt
from xlutils.copy import copy
import os

def saveData(dataset, output_file):
    output_file = "{}.xls".format(output_file) # this will be xls file name
    fieldnames = ["Header 1", "Header 2", "Header 3", "Header 4"] # change your header list here
    wb = xlwt.Workbook(encoding="UTF-8")
    ws = wb.add_sheet("Sheet 1")
    if os.path.exists(output_file):
        # old file, get last untouched row and start writing data
        while True:
            try:
                rb = xlrd.open_workbook(
                    output_file, formatting_info=True, on_demand=False)
                sht = rb.sheet_by_index(0)
                lastRows = sht.nrows
                wb = copy(rb)
                sheet = wb.get_sheet(0)
                pos = 0
                for data in dataset:
                    sheet.write(lastRows, pos, data)
                    pos += 1
                wb.save(output_file)
                break
            except OSError:
                pass
    else:
        # new file, create the headers
        pos = 0
        for fieldname in fieldnames:
            ws.write(0, pos, fieldname)
            pos += 1
        # now saving first row of data
        pos = 0
        for data in dataset:
            ws.write(1, pos, data)
            pos += 1
        wb.save(output_file)

if __name__ == "__main__":
    data = ["Cell data 1", "Cell data 2", "Cell data 3", "Cell data 4"]
    saveData(data, "my_sheet")
