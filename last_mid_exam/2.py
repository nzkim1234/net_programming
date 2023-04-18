lst = ['H','e','l','l','o',',',' ','I','o','T']
lst += ['!']
print(lst)
lst.remove('o')
print(lst)
lst[4] = 'a'
print(lst)
print(*lst)
print(sorted(lst, reverse=True))