#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

from xcsv.csv_util import CSVUtil
from xcsv.row import Row

if __name__ == '__main__':
    csv_util = CSVUtil()
    csv_util.open(filename="assets/2017_m_c.csv")

    print(f"获取row: {csv_util.read()}")

    print(f"获取head: {csv_util.read_header().parse()}")

    print(f"获取row: {csv_util.read()}")

    print("###################read_all()获取前5行#######################")
    all_row = csv_util.read_all()
    for i in range(len(all_row)):
        if i > 4:
            break
        print(all_row[i])

    print("###################生成器获取前5行#######################")
    count = 5
    for row in csv_util.row_generator():
        count -= 1
        print(row)

        if count <= 0:
            break

    print("###################单行写入#######################")
    csv_util.write(Row((1, 2, 3, '土豆1号', '电影评价', 4, 5, 6, time.strftime('%Y-%m-%d %H:%M:%S'))))
    csv_util.write(Row((1, 2, 3, '土豆2号', '电影评价', 4, 5, 6, time.strftime('%Y-%m-%d %H:%M:%S'))))

    print("###################多行写入#######################")
    rows = [Row((1, 2, 3, '土豆3号', '电影评价', 4, 5, 6, time.strftime('%Y-%m-%d %H:%M:%S'))).get_content(),
            Row((1, 2, 3, '土豆4号', '电影评价', 4, 5, 6, time.strftime('%Y-%m-%d %H:%M:%S'))).get_content()]
    csv_util.write_all(rows)

    csv_util.close()
