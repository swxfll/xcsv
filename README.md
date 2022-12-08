# XCSV

<div style="text-align: center;">
<img src="assets/logo.png" style="height: 25%; width: 25%;">
</div>


<div style="text-align: center;"><h3>用于高性能的读写 CSV 数据文件，支持生成器操作。</h3></div>

# 可用方法

## CSV Util 的全部方法

- `read`: 读取一行 CSV 数据（不包括表头）。
- `read_all`: 读取全部的 CSV 数据（不包括表头）。
- `write`: 保存一行 CSV 数据到文件。
- `write_all`: 保存若干的 CSV 数据到文件。
- `open`: 用于打开一个 CSV 数据文件。
- `close`: 关闭当前的 CSV 数据文件，可以重复关闭。
- `read_header`: 读取 CSV 文件的头部，如果该 CSV 文件没有头部，那么会返回第一行 CSV 数据。
- `row_generator`: 返回一个 Row 读取生成器。

## Header 类的全部方法

## Row 类的全部方法


# 示例

## 使用 Row 行生成器读取10行数据

```python
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
count = 10
for row in csv_util.row_generator():
    count -= 1
    print(row)

    if count <= 0:
        break
```

## 写入2行数据到 movies.csv

```python
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
csv_util.write(Row((1, 2, 3, '土豆1号', '电影评价', 4, 5, 6, time.strftime('%Y-%m-%d %H:%M:%S'))))
csv_util.write(Row((1, 2, 3, '土豆2号', '电影评价', 4, 5, 6, time.strftime('%Y-%m-%d %H:%M:%S'))))

# OR
rows = [Row((1, 2, 3, '土豆3号', '电影评价', 4, 5, 6, time.strftime('%Y-%m-%d %H:%M:%S'))),
        Row((1, 2, 3, '土豆4号', '电影评价', 4, 5, 6, time.strftime('%Y-%m-%d %H:%M:%S')))]
csv_util.write_all(rows)
```


# 许可条款 

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)