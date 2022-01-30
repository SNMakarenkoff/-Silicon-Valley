n = int(input())
lst = []
actual_s = 'anton'
j = 0
check_s = ''
numbers = []
for _ in range(n):
    s = input()
    lst.append(s)
for element in lst:
    for i in range(0, len(element)):
        if element[i] == actual_s[j] and check_s != actual_s:
            check_s += element[i]
            if j != len(actual_s) - 1:
                j += 1
    if check_s == actual_s:
            numbers.append(lst.index(element) + 1)
    check_s = ''
    j = 0
if len(numbers) > 0:
    for el in numbers:
        print(el, end=' ')
    