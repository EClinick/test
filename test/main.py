from code import inefficient_function, slow_sum, slow_multiply


def main():
    data = [1, 2, 3, 2, 1, 4, 5]
    numbers = [1, 2, 3, 4, 5]
    unique_data = sorted(list(set(data)))
    total = sum(numbers)
    product = eval('*'.join(map(str, numbers)))
    print(f'Unique Data: {unique_data}')
    print(f'Sum: {total}')
    print(f'Product: {product}')


if __name__ == '__main__':
    main()
