"""
Задание 2.
Генератор flat_generator для плоского представления списка списков.
"""
import types


def flat_generator(list_of_lists):
    """
    Генератор для преобразования списка списков в плоскую последовательность.
    """
    for sublist in list_of_lists:
        for item in sublist:
            yield item


def test_2():
    """
    Тестовая функция для проверки работы flat_generator.
    """
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
        flat_generator(list_of_lists_1),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

    print("Тест 2 пройден успешно!")


if __name__ == '__main__':
    test_2()
