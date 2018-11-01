from collections import deque

dq = deque(range(1000))
dq.append(1)  # O(1)
print(dq[1])  # O(n)
dq.pop()  # O(1)
dq.popleft()  # O(1)
dq.insert(0, 1)  # O(n)
print(1 in dq)  # O(n)
del dq[0]  # O(1)


conjunto = set(range(8, 15))
conjunto.add(1)  # O(1)
conjunto.remove(1)  # O(1)
print(1 in conjunto)  # O(1)
conjunto_2 = set(range(10))
print(conjunto)
print(conjunto_2)
print(conjunto.union(conjunto_2))
print(conjunto.intersection(conjunto_2))
print(conjunto.difference(conjunto_2))
