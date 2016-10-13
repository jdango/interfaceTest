#encoding:utf-8
'''
@note:该文件用于创建xls的日志分析结果文件
@author: eason.sun
@organization: csb
@copyright: weiyao
'''
import os
from Libs import xlwt

EXCEL_CELL_MAX_LENGTH = 32767

def CreateLogAnalysisResultFile(file_path, content, isSplit = True):
    """
    @author: eason.sun
    @param file_path:生成文件的路径
    @param content:生成内容
    @return: None
    @summary: 用于生成日志分析结果文件
    """
    if os.path.exists(file_path):
        os.remove(file_path)
    newFile = open(file_path, 'w')
    newFile.close()
    baseStyleStr = 'font:height 160,name Microsoft YaHei;borders:top dashed, bottom dashed, left dashed, right dashed;align: wrap on, vert centre, horiz left'
    style = xlwt.easyxf(baseStyleStr)
    wbk = xlwt.Workbook()
    w_worksheet = wbk.add_sheet('sheet 1')
    index = 0
    for item in content:
        if len(item) > EXCEL_CELL_MAX_LENGTH:
            item = item[:EXCEL_CELL_MAX_LENGTH-10]
        w_worksheet.write(index, 0, item.decode('utf8'), style)
        index += 1
        if index % 3 == 2 and isSplit:
            w_worksheet.write(index, 0, "")
            index += 1
    # 设置第一列的宽度
    w_worksheet.col(0).width = 0x0d00 + 30000
    wbk.save(file_path)