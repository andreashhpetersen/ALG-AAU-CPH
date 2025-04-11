import random
from collections import defaultdict
from datetime import datetime, timedelta

names = []
with open('./names.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        name, _ = line.split(' - ')
        names.append(name)


def random_name():
    return names[random.randint(0, len(names)-1)]


def parse_date(date_string, time_format='%d/%m/%Y'):
    return datetime.strptime(date_string, time_format).date()

def parse_str(dt, time_format='%d/%m/%Y'):
    return datetime.strftime(dt, time_format)

def get_random_date(start, end):
    end = end - timedelta(1)
    return start + random.random() * (end - start)

def get_random_interval(start, end):
    q1 = get_random_date(start, end)
    q2 = get_random_date(q1, end)
    return (q1, q2)

def binary_search(el, arr):
    p, r = 0, len(arr)
    i = (p + r) // 2

    while arr[i][1] != el and not i == p:
        if el < arr[i][1]:
            r = i
        else:
            p = i

        i = (p + r) // 2

    return i


def find_popular(data, i, j):
    count = defaultdict(int)
    popular = None
    for name, dob in data[i:j]:
        count[name] += 1
        if count[name] > count[popular]:
            popular = name

    while data[i][0] == popular and i < j:
        i += 1

    if i != j:
        data[i] = (popular, data[i][1])
        count[popular] += 1
    return popular, count[popular]


def random_date(start, end, time_format='%d/%m/%Y', as_datetime=False):
    """Get a time at a proportion of a range of two formatted times.
    """

    stime = datetime.strptime(start, time_format)
    etime = datetime.strptime(end, time_format) - timedelta(days=1)

    ptime = stime + random.random() * (etime - stime)

    if as_datetime:
        return ptime
    else:
        return datetime.strftime(ptime, time_format)


def random_interval(start, end):
    q1 = random_date(start, end)
    q2 = random_date(q1, end)

    return q1, q2




"""
Task 1: Most popular name in given range
Task 2: Select name of rank k
"""

def new_make_data_task1(n, m):
    start, end = parse_date('01/01/1900'), parse_date('31/12/1999')

    data = []
    for _ in range(n):
        data.append((random_name(), get_random_date(start, end)))

    data.sort(key=lambda x: x[1])

    intervals = [get_random_interval(start, end) for _ in range(m)]
    for start, end in intervals:
        i, j = binary_search(start, data), binary_search(end, data) + 1
        popular, count = find_popular(data,i,j)
        import ipdb; ipdb.set_trace()


def make_data_task1(n):
    start, end = '01/01/1900', '31/12/1999'
    q1, q2 = random_interval(start, end)


    n1 = random.randint(1, n // 2)

    data = []
    popular = None
    counter = defaultdict(int)
    for i in range(0, n1):
        name = random_name()
        dob = random_date(q1, q2)
        data.append((name, dob))
        counter[name] += 1

        if counter[name] > counter[popular]:
            popular = name

    # add an extra to avoid ties
    data.append((popular, random_date(q1,q2)))
    counter[popular] += 1

    for _ in range(n1+1, n):
        if random.random() < 0.5:
            dob = random_date(start, q1)
        else:
            dob = random_date(q2, end)
        data.append((random_name(), dob))

    if not len(data) == n:
        import ipdb; ipdb.set_trace()
    random.shuffle(data)
    with open(f'./data/task1_{n}.txt', 'w') as f:
        f.write(f'{n}\n')
        for name, dob in data:
            f.write(f'{name} {dob}\n')

        f.write(f'{q1} - {q2}')

    with open(f'./data/task1_{n}_solution.txt', 'w') as f:
        f.write(f'{popular} {counter[popular]}')


def make_data_task2(n):
    start, end = '01/01/1900', '31/12/1999'

    q1 = random_date(start, end)
    rank = random.randint(1,  2*n // 3)

    data = []
    for _ in range(0, rank):
        dob = random_date(start, q1)
        data.append((random_name(), dob))

    correct = random_name()
    data.append((correct, q1))

    dt = datetime.strptime(q1, '%d/%m/%Y')
    dt = (dt + timedelta(days=1)).strftime('%d/%m/%Y')

    for _ in range(rank+1, n):
        dob = random_date(dt, end)
        data.append((random_name(), dob))

    random.shuffle(data)
    with open(f'./data/task2_{n}.txt', 'w') as f:
        f.write(f'{n}\n')
        for name, dob in data:
            f.write(f'{name} {dob}\n')
        f.write(f'{rank}')

    with open(f'./data/task2_{n}_solution.txt', 'w') as f:
        f.write(f'{correct} {q1}')


if __name__ == '__main__':
    sizes = [5, 10, 20, 50, 100, 1000, 10_000, 100_000, 1_000_000]

    new_make_data_task1(5,2)

    # for n in sizes:
    #     make_data_task1(n)
    #     make_data_task2(n)
