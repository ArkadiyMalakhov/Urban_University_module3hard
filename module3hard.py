def calculate_structure_sum(data_structure):
    summ = 0
    for item in data_structure:
        if isinstance(item, (list, tuple, set)):
            summ += calculate_structure_sum(item)
        elif isinstance(item, dict):
            summ += calculate_structure_sum(item.keys())
            summ += calculate_structure_sum(item.values())
        elif isinstance(item, str):
            summ += len(item)
        elif isinstance(item, int):
            summ += item
    return summ


list_ = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), 'Hello', ((), [{(2, 'Urban', ('Urban2', 35))}])]
print(calculate_structure_sum(list_))






























