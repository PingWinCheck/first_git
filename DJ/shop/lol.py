a = []
b = {'one': []}
print(b)
b['one'].append(5)
print(b)
b['one'].append(7)
print(b)
b['one'].append(99)
print(b)
b['one'] = b['one'].remove(7)
print(b)