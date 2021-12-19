import pytest, random, math, os
from program import file_reader, search_min, search_max, numbers_sum, numbers_multiplication


def generate_random_mas():
    return random.sample(range(-100000, 100000), 100)


def test_search_min():
    random_mas = generate_random_mas()
    assert search_min(random_mas) == min(random_mas)


def test_search_max():
    random_mas = generate_random_mas()
    assert search_max(random_mas) == max(random_mas)


def test_numbers_sum():
    random_mas = generate_random_mas()
    assert numbers_sum(random_mas) == sum(random_mas)


def test_numbers_multiplication():
    random_mas = generate_random_mas()
    assert numbers_multiplication(random_mas) == math.prod(random_mas)


def test_file_reader():
    file = open('file.txt', 'w')
    file.write('1 2.2 abc')
    file.close()
    assert file_reader('file') == -1
    os.remove('file.txt')


if __name__ == '__main__':
    pytest.main()


