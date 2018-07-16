# Random Python cheat notes

# list of dict
for i, movie in enumerate(sorted(a_list, key=lambda r: (r['rating'], r['year']), reverse=True)):
    if i >= 4: break
    print(str(i) + " "),
    pretty(movie)

from operator import itemgetter
m_list = sorted(a_list, key=itemgetter('rating','year'))

rows.sort(key=itemgetter('rating'))
for date, items in itertools.groupby(rows, keys=itemgetter('date')):
    print(date) ; for i in items: print('    ', i)

data = [1,2,3,4] ; name, shares, price, date = data ; name
first, *middle, last = grades ; return avg(middle)
record = ('S', 's@tg.com', '818-406-xxxx', '650-xxx-xxxx')
name, email, *phone = record

import heapq
nums = [1,2,3,4,4,5]
print(heapq.nlargest(3, nums)) ; print(heapq.nsmallest(3, nums))
# list of dict
cheap_list = heapq.nsmallest(3, a_list, key=lambda s: s['price'])

# dict keys in common, in a not b, k,v pairs in common
a.keys() & b.keys() # { 'x', 'y' }
a.keys() - b.keys() # { 'z' }
a.items() & b.items() # { 'y', 2 }
# remove some keys into new dict
c = {key:a[key] for key in a.keys() - { 'z', 'w' }}

[n for n in a_list if n > 0]
pos = (n for n in a_list if n > 0)
for x in pos: print(x)

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))

p1 = { key:value for key, value in prices.items() if value > 200 }

if any(name.endswith('.py') for name in files): print('yes')

s = sum(x * x for x in nums)

'aljfkjkldjfklj'.replace('a', 'b')
'abc'.ljust(20).rjust(20).center(20)
'{:<10s} {:>20s} {:10.2f}'.format(a, b, c)
'{:0,.1f}'.format(1234.56789) # 1,234.6
round(1.23, 1) # 1.2
round(1.27, 1) # 1.3
round(1.25361, 3) # 1.254
round(1627731, -1) # 1627730

int has bin(), oct() and hex()

random.choice([])
random.sample([], 3)
random.shuffle([])
random.randint(0,10)
random.random() # float between 0 and 1
random.getrandbits(200) # int returned with 200 random bits

with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f) ; print(line, end='')
    except StopIteration:
        pass

reversed([])

for p in itertools.permutations(['a','b','c']): print(p) # ('a','b','c')\n('b','c','a')

with open('file', 'rt', encoding='ascii', errors='ignore') as f:
    data = f.read() or for line in f:

# file write mode 'x' will FileExistsError if file exists

with open('a.csv') as f:
    f_csv = csv.reader(f, delimiter='\t')
    headers = next(f_csv)
    for row in f_csv: print(row)

with fileinput.input('/etc/passwd') as f:
    for line in f: print(line, end='')

def is_valid(address):
    try:
        socket.inet_aton(address)
    except socket.error:
        return False
    return True

funcs = [a_func]
funcs[0](2, 3)
func_dict = {
    'cond_a': handle_a,
    'cond_b': handde_b
}
func_dict.get(cond, handle_default)()
def disp_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y
    }.get(operator, lambda: None)()

s.issubset(t) # every s element in t
s.issuperset(t) # every t in s
s.union(t) # new set with s and t elements
s.intersection(t) # new set with common s and t
s.symmetric_difference(t) # new set with elements of s and t not in both
s.remove(x) # KeyError if not present
s.discard(x) # remove if exists
s.pop() # KeyError if empty
s.clear() # wipe out set

del(a_dict[key])

list.append / extend / insert(i,x) / remove(x) / pop(i) / clear() (del a[:]) / count(x) / sort(key=None, reverse=False) / reverse() / copy()

# lambda 1-line function
# no def nor return keywords (implicit)

lambda x: x * 2
def double(x):
    return x * 2

lambda x, y: x + y
def add(x, y):
    return x + y

mx = lambda x, y: x if x > y else y
def mx(x, y):
    if x > y:
        return x
    else:
        return y
print(mx(8, 5))

# map runs function against each element of a list
# returns the modified list
# [m, n, p] mapped with f() -> [f(m), f(n), f(p)]
n = [4, 3, 2, 1]
print(list(map(lambda x: x**2, n)))
# map(function, list)
# print(list(map(square, n))) for square()
print([x**2 for x in n])

# filter filters items from a list
# returns list
n = [4, 3, 2, 1]
print(list(filter(lambda x: x > 2, n)))
print([x for x in n if x > 2])

# reduce runs function against every pair of elements in a list
# multiple a bunch of numbers together
def mult(lst1):
    prod = lst1[0]
    for i in range(1, len(lst1)):
        prod *= lst1[i]
    return prod
n = [4, 3, 2, 1]
print(reduce(lambda x, y: x * y, n))

# Generators
def sq_nums(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result
my_nums = sq_nums([1, 2, 3, 4, 5])
def sq_nums_2(nums):
    for i in nums:
        yield(i*i)
my_nums = sq_nums_2([1, 2, 3, 4, 5])
# that returns a generator object
# does not hold all results in memory
print next(my_nums)
print next(my_nums)
# StopIteration error if next cannot pull another result
for num in my_nums:
    print(num)
# no exception
my_nums = [x*x for x in [1, 2, 3, 4, 5]]
my_nums = (x*x for x in [1,2,3,4,5])
print(list(my_nums))

mem_profile.memory_usage_resource()
t1 = time.clock()
run this
t2 = time.clock()
"{} s".format(t2-t1)

my_list = [n for n in nums]

my_list = filter(lambda n: n%2 == 0, nums)

my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}

[i * j for i in range(3) for j in range(3)]
# [0, 0, 0, 0, 1, 2, 0, 2, 4]
[i * j for i, j in itertools.product(range(3), range(3))]
# [0, 0, 0, 0, 1, 2, 0, 2, 4]
