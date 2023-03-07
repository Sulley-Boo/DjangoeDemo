from typing import List
from collections import Counter
from collections import deque
from collections import defaultdict
from collections import OrderedDict
import array
import heapq as hq

'''
    Counter:统计次数的类
'''
mylist = [1, 3, 2, 1, 1, 5, 6, 5, 10]
count = Counter(mylist)
print(count)  # 统计各个元素出现次数
print(len(set(count)))  # 统计序列中有多少个不同元素
print("{0}:{1}".format(count.keys(), count.values()))
print(count.most_common(3))

'''
    deque:双端队列
    支持线程安全
'''
print("======")
deque = deque([3, 4, 5, 6])
deque.append(7)
deque.append(8)
print(deque)
deque.pop()
print(deque)
deque.appendleft(2)
deque.appendleft(1)
print(deque)
deque.popleft()
print(deque)

'''
    defaultdict:当查找一个不存在的键操作发生时，它的default_factory会被调用，提供一个默认的值，并且将这对键值存储下来
'''
print("======")
s = "the quick brown fox jumps over the lazy dog"
words = s.split()
dict1 = defaultdict(list)
for v, k in enumerate(words):
    # dict1[k].append(v)
    dict1.setdefault(k, []).append(v)
print(dict1)

'''
    array:定义了一个很像list的新对象类型，不同之处在于它限定了这个类型只能装一种类型的元素。array元素的类型是在创建并使用的时候确定的
'''
print("======")
arr1 = array.array("i", [1, 2, 3, 4, 5])
print(arr1)
arr2 = array.array(arr1.typecode, (3 * x for x in arr1))
print(arr2)

'''
    heapq:优先级队列，默认是小根堆
'''
print("======")
array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
heap = []
# hq.heapify(array)
# print(array)
# print([array[0]])
for i in array:
    hq.heappush(heap, i)
print(heap)

'''
    OrderedDict:有序表
'''
ordered_dict = OrderedDict()
ordered_dict["1"] = 1
ordered_dict["4"] = 4
ordered_dict["3"] = 3
ordered_dict["2"] = 2
print(ordered_dict)
