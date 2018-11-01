lst = list(range(1000))
lst.append(1)  # O(1)
print(lst[1])  # O(1)
lst.sort()  # O(n*log(n))
lst.pop()  # O(1)
lst.insert(0, 1)  # O(n)
print(1 in lst)  # O(n)
del lst[0]  # O(1)