import pytest, time, random, math, os
from program import file_reader, search_min, search_max, numbers_sum, numbers_multiplication


def generate_random_mas():
    return random.sample(range(-1000000000, 1000000000), 100)


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


def test_time():
    random_mas = generate_random_mas()
    random_mas_str = []
    for i in random_mas:
        random_mas_str.append(str(i))
    random_str = ' '.join(random_mas_str)

    file_1 = open('file1.txt', 'w')
    file_2 = open('file2.txt', 'w')
    file_1.write(random_str)
    file_2.write(random_str * 1000)
    file_1.close()
    file_2.close()

    time1_start = time.time()
    nums1 = file_reader('file1')
    search_min(nums1)
    search_max(nums1)
    numbers_sum(nums1)
    numbers_multiplication(nums1)
    time1_end = time.time() - time1_start

    time2_start = time.time()
    nums2 = file_reader('file2')
    search_min(nums2)
    search_max(nums2)
    numbers_sum(nums2)
    numbers_multiplication(nums2)
    time2_end = time.time() - time2_start

    os.remove('file1.txt')
    os.remove('file2.txt')

    assert time2_end > time1_end


def test_file_reader():     # Custom test
    file = open('file.txt', 'w')
    file.write('1 2.2 abc')
    file.close()
    assert file_reader('file') == -1
    os.remove('file.txt')


if __name__ == '__main__':
    pytest.main()


