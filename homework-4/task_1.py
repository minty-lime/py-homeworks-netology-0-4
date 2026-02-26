"""
Задание 1.
Итератор FlatIterator для плоского представления списка списков.
"""


class FlatIterator:
    """
    Итератор для преобразования списка списков в плоскую последовательность.
    Одноразовый: для повторного обхода нужно создать новый экземпляр.
    """

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.outer_cursor = 0
        self.inner_cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.outer_cursor < len(self.list_of_list):
            if self.inner_cursor < len(self.list_of_list[self.outer_cursor]):
                item = self.list_of_list[self.outer_cursor][self.inner_cursor]
                self.inner_cursor += 1
                return item
            else:
                self.outer_cursor += 1
                self.inner_cursor = 0

        raise StopIteration


def test_1():
    """
    Тестовая функция для проверки работы FlatIterator.
    """
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_1),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    # Проверка одноразовости: повторный list() должен вернуть пустой список
    it = FlatIterator(list_of_lists_1)
    first_pass = list(it)
    second_pass = list(it)
    assert first_pass == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert second_pass == []

    print("Тест 1 пройден успешно!")


if __name__ == '__main__':
    test_1()
