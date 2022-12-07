#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from xcsv.header import Header
from xcsv.row import Row


class CSVUtil:
    """
    CSV 文件实用程序
    """

    __csv_file = None
    __cached_header = None

    def read(self) -> Row:
        """
        读取 CSV 数据并返回为 Python 对象, 每调用一次，就会读取一行新的数据
        :return: Row
        """
        # 如果读的是表头，就让指针往下移一行
        if self.__csv_file.tell() == 0:
            self.__csv_file.readline()

        line = self.__csv_file.readline()
        line_object = self.__parse_csv_string_line(line=line)

        return Row(row=line_object)

    def write(self, row: Row) -> None:
        # TODO 实现写入一行 CSV 数据追加到文件中
        # 文件指针移到末尾
        self.__csv_file.seek(0, 2)
        # writer = csv.writer(self.__csv_file)
        # writer.writerow(row.get_content())
        self.__csv_file.write(row.get_content())

    def write_all(self, rows: list) -> None:
        # 文件指针移到末尾
        self.__csv_file.seek(0, 2)
        self.__csv_file.writelines(rows)

    def open(self, filename: str = None) -> None:
        """
        打开 CSV 文件，将打开的CVS对象保存到 __csv_file
        :param filename: 文件位置
        :return: None
        """

        if (filename is None) or (len(filename) <= 0):
            return

        if os.path.exists(filename):
            self.__csv_file = open(filename, 'r+', encoding="UTF-8", newline='')
            # self.__csv_file = self.__csv_file.replace("\r\n", "")

    def close(self) -> None:
        """
        关闭 CSV 文件
        :return: None
        """
        if not self.__csv_file.closed:
            self.__csv_file.close()

    def read_header(self, cache: bool = False) -> Header:
        """
        读取 CSV 文件头部
        :param cache: 是否利用缓存加速
        :return: CSV 头部
        """

        if cache:
            if self.__cached_header:
                return self.__cached_header

        # TODO 存在一个文件指针位置问题
        # 判断文件指针是否在第一行，如果在第一行就无须记录指针的位置了
        is_first_read = True
        current_file_pointer_position = -1
        if self.__csv_file.tell() != 0:
            is_first_read = False
            current_file_pointer_position = self.__csv_file.tell()  # tell() 方法返回文件的当前位置，即文件指针当前位置。
            self.__csv_file.seek(0)

        line = self.__csv_file.readline()

        cols = self.__parse_csv_string_line(line=line)

        header = Header()
        header.fill_content(content=cols)

        if not is_first_read:
            self.__csv_file.seek(current_file_pointer_position)

        self.__cached_header = header

        return header

    def read_all(self) -> list:
        # TODO 实现将 CSV 文件中的全部数据打包成一个 Row 类型的 list
        lists: list[Row] = []
        self.__csv_file.seek(0)
        self.__csv_file.readline()  # 跳过表头
        for i in self.__csv_file:
            line_object = self.__parse_csv_string_line(line=i)
            lists.append(Row(row=line_object))
        return lists

    def __parse_csv_string_line(self, line: str) -> tuple:
        """
        将 CSV 字符串解析为 Python 对象， 将字符串转列表再转元组
        :param line: CSV 字符串数据
        :return: Python 对象
        """

        if (len(line) <= 0) or (line is None):
            return ()

        tmp = []

        line = line.strip()
        cols = line.split(",")

        for col in cols:
            if (len(col) <= 0) or (col is None):
                tmp.append(None)
            else:
                tmp.append(col.strip())

        return tuple(tmp)

    def row_generator(self) -> Row:
        """
        Row 生成器，每次迭代，可以返回一个 Row 对象
        :return: Row
        """
        self.__csv_file.seek(0)
        self.__csv_file.readline()  # 跳过表头
        for line in self.__csv_file:
            line_object = self.__parse_csv_string_line(line=line)
            yield Row(row=line_object)


if __name__ == '__main__':
    pass
