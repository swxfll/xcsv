#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from xcsv.overflow_column_exception import OverflowColumnException


class Row:
    """
    代表一个 CSV 文件的行
    """
    __content: tuple = ()

    def __init__(self, row: tuple = ()):
        self.__content = row

    def get_content(self) -> str:
        temp: str = ""
        for i in self.__content:
            temp = temp + str(i) + ","

        if len(temp) > 0:
            return temp[:len(temp) - 1] + '\n'
        else:
            return ""

    def get_col_by_index(self, index: int) -> str | int | float | None:
        """
        获取指定行里边的某一列
        :param index: 索引, 从 0 开始
        :return: 指定单元格的数据
        """

        content_length = len(self.__content)
        if index >= content_length:
            raise OverflowColumnException("{} col is overflow.".format(index))

        return self.__content[index]

    def __str__(self):
        if self.__content[0] is None:
            return ""

        # text = "("
        #
        # for col in self.__content:
        #     text += col
        #     text += ", "
        # if len(text) > 1:
        #     text = text[:len(text) - 2]
        #
        # text += ")"

        return '(' + ','.join(self.__content) + ')'



if __name__ == '__main__':
    pass
