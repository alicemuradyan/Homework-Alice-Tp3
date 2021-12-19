def file_reader(name):
    file_name = name + '.txt'

    try:
        file = open(file_name, 'r')
    except IOError:
        return -2

    nums = []
    for i in file.read().split():
        nums.append(float(i))
    file.close()

    if not nums:
        return 0

    for i in nums:
        try:
            x = int(i)
        except ValueError:
            return -1

    return nums


def search_min(nums):
    min_num = nums[0]
    for i in nums:
        if i < min_num:
            min_num = i

    return min_num


def search_max(nums):
    max_num = nums[0]
    for i in nums:
        if i > max_num:
            max_num = i

    return max_num


def numbers_sum(nums):
    nums_sum = 0
    for i in nums:
        nums_sum += i

    return nums_sum


def numbers_multiplication(nums):
    try:
        nums_multiplication = 1
        for i in nums:
            nums_multiplication *= i
    except OverflowError:
        print('Произошла ошибка переполнения. Числа в файле слишком большие. Мы не можем вычислить их произведение.')
        return '-'

    return nums_multiplication


def body():
    print('Введите название файла с числовыми данными для рассчета.')
    name = input()
    nums = file_reader(name)
    if nums == 0:
        print('Пустой файл. Невозможно посчитать значения.')
    elif nums == 1:
        print('Файл некорректен. Проверьте, что в нем находятся числа и все они разделены одинарным пробелом.')
    elif nums == -2:
        print('Такого файла не существует. Проверьте, что он находется в той же директории, что и данная программа.')
    else:
        print('В файле:', nums)
        print('Минимальное:', search_min(nums))
        print('Максимальное:', search_max(nums))
        print('Сумма ряда:', numbers_sum(nums))
        print('Произведение ряда:', numbers_multiplication(nums))


if __name__ == '__main__':
    body()
