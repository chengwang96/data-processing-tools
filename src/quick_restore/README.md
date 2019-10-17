# quick_restore

使用 pickle 进行读写

函数封装主要为解决两个问题：如果使用 Python3，可能遇到读取 Python2 下编码的文件编码错误；如果使用 Python2，可能出现无法读取 Python3 中编码的文件