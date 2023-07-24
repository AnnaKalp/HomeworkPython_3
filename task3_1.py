"""Дан список повторяющихся элементов. Вернуть список с дублирующимися
элементами. В результирующем списке не должно быть дубликатов."""

my_list = [1, 2, 3, 2, 4, 3, 5, 6, 1]
new_list = []
for el in my_list:
    if my_list.count(el) > 1:
        new_list.append(el)
print(list(set(new_list)))
