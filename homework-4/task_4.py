"""
Задание 4 (необязательное).
Генератор flat_generator для обработки списков с любым уровнем вложенности.
"""
import types
from collections.abc import Iterable


def flat_generator(list_of_list):
    """
    Генератор для преобразования вложенных итерируемых объектов любого уровня
    в плоскую последовательность.
    Поддерживает list, tuple, set и другие Iterable (кроме строк и байтов).
    """
    for item in list_of_list:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flat_generator(item)
        else:
            yield item


def test_4():
    """
    Тестовая функция для проверки работы flat_generator с любым уровнем вложенности.
    """
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
        flat_generator(list_of_lists_2),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)

    # Проверка работы с кортежами и смешанными структурами
    mixed_data = [
        ('a', 'b'),
        [('c',), ['d', 'e']],
        (1, [2, (3,)]),
    ]

    assert list(flat_generator(mixed_data)) == ['a', 'b', 'c', 'd', 'e', 1, 2, 3]

    # set не гарантирует порядок, поэтому проверяем через множество
    data_with_set = [
        [1, 2],
        {3, 4},
        [5],
    ]
    result = list(flat_generator(data_with_set))
    assert set(result) == {1, 2, 3, 4, 5}
    assert len(result) == 5

    print("Тест 4 пройден успешно!")


if __name__ == '__main__':
    test_4()
