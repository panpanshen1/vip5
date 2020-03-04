a = [11,13,5,7,0,56,23,34,72]

print(min(a),max(a),len(a))
print(a.index(56))
a.append(7)
print(a)
a.pop(4)
print(a)
a.sort()
print(a)


b=[66,67,68,0]
a.extend(b)
print(a)