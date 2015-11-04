__author__ = 'Administrator'

from collections import namedtuple,deque,defaultdict,OrderedDict,Counter

#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
PointValues = namedtuple('pointvalues',['x','y'])
pv = PointValues(1,2)
print('pv.x is : ',pv.x,' and pv.y is : ',pv.y)
#print('type(PointValues) is : ',type(PointValues))

#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print("dd['key1'] is : ",dd['key1']) # key1存在
print("dd['key2'] is : ",dd['key2']) # key1存在

#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict：
d = dict([('a', 1), ('b', 2), ('c', 3)])
print('non orderedDict is : ',d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print('used orderdDict is : ',od)

#Counter是一个简单的计数器，例如，统计字符出现的个数
counters = Counter()
for ch in 'programming':
    counters[ch] = counters[ch] + 1
print(counters)
