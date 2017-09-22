# 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：
# >>> print('\\\t\\')
# \       \
# >>> print(r'\\\t\\')
# \\\t\\

# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容，可以自己试试：
# >>> print('''line1
# ... line2
# ... line3''')
# line1
# line2
# line3

# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：

# >>> 9 / 3
# 3.0
# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数：

# >>> 10 // 3
# 3

# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言，例如：

# >>> print('包含中文的str')
# 包含中文的str
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：

# >>> ord('A')
# 65
# >>> ord('中')
# 20013
# >>> chr(66)
# 'B'
# >>> chr(25991)
# '文'

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

# Python对bytes类型的数据用带b前缀的单引号或双引号表示：

# x = b'ABC'
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

# 在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：

# >>> 'Hello, %s' % 'world'
# 'Hello, world'
# >>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
# 'Hi, Michael, you have $1000000.'
# 你可能猜到了，%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

# 常见的占位符有：

# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
# 其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：

# >>> '%2d-%02d' % (3, 1)
# ' 3-01'
# >>> '%.2f' % 3.1415926
# '3.14'
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：

# >>> 'Age: %s. Gender: %s' % (25, True)
# 'Age: 25. Gender: True'
# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：

# >>> 'growth rate: %d %%' % 7
# 'growth rate: 7 %'