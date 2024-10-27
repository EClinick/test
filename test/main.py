from code import inefficient_function, slow_sum, slow_multiply


def main():
    data = [1, 2, 3, 2, 1, 4, 5]
    unique_data = sorted(set(data))
    numbers = list(range(1, 6))
    total_sum_numbers = sum(numbers)
    product_numbers = eval('*'.join(map(str, numbers)))
    print(
        f'Unique Data: {unique_data}\nSum: {total_sum_numbers}\nProduct: {product_numbers}'
        )


if __name__ == '__main__':
    main()
