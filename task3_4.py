"""Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей."""
# создаем словарь с вещами каждого друга

lst = {
    'Андрей': ('палатка', 'спальник', 'рюкзак', 'еда'),
    'Василий': ('палатка', 'спальник', 'еда', 'топор'),
    'Борис': ('палатка', 'спальник', 'карта', 'фонарик'),
}

common_items = set()
for key in lst:
    if not common_items:
        common_items = set(lst[key])
    else:
        common_items = common_items.intersection(set(lst[key]))
print(f'Вещи, которые взяли все три друга:', *common_items)

friends = lst.keys()
unique_items = set()
for friend in friends:
    delete = set(lst[friend])
    one_item = set()
    unique_items = set(lst[friend])
    for other_friend in friends:
        if other_friend != friend:
            unique_items = unique_items.difference(set(lst[other_friend]))
            if not one_item:
                one_item = set(lst[other_friend])
            else:
                one_item = one_item.intersection(set(lst[other_friend]))
    one_item -= delete

    if unique_items:
        print(f'Уникальные вещи каждого друга: {friend} -', *unique_items)
        if one_item:
            print(f'Вещь, которая отсутствует у {friend} -', *one_item)
