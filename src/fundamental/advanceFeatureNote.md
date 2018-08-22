## 高级特性

### 1、切片 do_slice.py

    a = ['aaa','bbb','ccc']
    print(a[:])

### 2、迭代 do_iter.py

    如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        print(key)

    dict的存储不是按照list的方式顺序排列，默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。

    使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。

    通过collections模块的Iterable类型判断一个对象是可迭代对象
    from collections import Iterable
    isinstance('abc', Iterable)

    如果要对list实现类似Java那样的下标循环
    Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)

### 3、列表生成式 do_listcompr.py

    运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
    列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
    list(range(1, 11))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
    [x * x for x in range(1, 11)]
    写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，
    for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
    [x * x for x in range(1, 11) if x % 2 == 0]
    还可以使用两层循环，可以生成全排列：
    [m + n for m in 'ABC' for n in 'XYZ']
    ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

### 4、列出当前目录下的所有文件和目录名

    import os # 导入os模块，模块的概念后面讲到
    [d for d in os.listdir('.')]
    使用两个变量来生成list
    d = {'x': 'A', 'y': 'B', 'z': 'C' }
    [k + '=' + v for k, v in d.items()]
    list中所有的字符串变成小写
    L = ['Hello', 'World', 'IBM', 'Apple']
    [s.lower() for s in L]

### 5、生成器 do_generator.py

    通过列表生成式，可以直接创建一个列表。但是，受到内存限制，列表容量是有限的。
    当创建一个包含100万个元素的列表，占用很大的存储空间，如果仅需要访问前面几个元素，绝大多数元素占用的空间都浪费了。
    用列表元素按照某种算法推算出来，在循环的过程中不断推算出后续的元素,这样就不必创建完整的list，从而节省大量的空间。
    在Python中，这种一边循环一边计算的机制，称为生成器：generator。
    要创建一个generator，有很多种方法。
    第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
    L = [x * x for x in range(10)]
    print(L)
    g = (x * x for x in range(10))
    print(next(g))
    generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，
    没有更多的元素时，抛出StopIteration的错误。
    不断调用next(g)实在是太变态了，使用for循环，因为generator也是可迭代对象：
    g = (x * x for x in range(10))
    for n in g:
        print(n)

### 6、迭代器 do_iter2.py

    可以直接作用于for循环的对象统称为可迭代对象：Iterable
    可以使用isinstance()判断一个对象是否是Iterable对象
    from collections import Iterable
    isinstance([], Iterable)

    生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到抛出StopIteration错误,无法继续返回下一个值了。
    可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
    可以使用isinstance()判断一个对象是否是Iterator对象
    from collections import Iterator
    isinstance((x for x in range(10)), Iterator)

    生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
    把list、dict、str等Iterable变成Iterator可以使用iter()函数：
    isinstance(iter([]), Iterator)
    isinstance(iter('abc'), Iterator)

    小结：凡是可作用于for循环的对象都是Iterable类型；凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；






