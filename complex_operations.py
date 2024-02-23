def check_if_list_empty(numbers):
    if not numbers:
        print("The list is empty.")
        return None, None, None, None, None
    return False


def check_palindrome(str_num):
    return str_num == str_num[::-1]


def calculate_ascii_sum(str_num):
    ascii_sum = 0
    for char in str_num:
        ascii_sum += ord(char)
    return ascii_sum


def determine_ascii_sum_status(ascii_sums):
    return ["odd" if x % 2 != 0 else "even" for x in ascii_sums]


def calculate_product(sorted_numbers):
    product = 1
    for num in sorted_numbers:
        product *= num
    return product


def calculate_factorial(n):
    factorial_result = 1
    if n > 1:
        for i in range(1, n + 1):
            factorial_result *= i
    return factorial_result


def check_if_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def complex_operations(numbers, n):
    if check_if_list_empty(numbers):
        return

    sorted_numbers = sorted(numbers)
    palindromes = [check_palindrome(str(num)) for num in sorted_numbers]
    ascii_sums = [calculate_ascii_sum(str(num)) for num in sorted_numbers]
    ascii_sum_status = determine_ascii_sum_status(ascii_sums)
    total_sum = sum(sorted_numbers)
    product = calculate_product(sorted_numbers)
    factorial_result = calculate_factorial(n)
    is_prime_result = check_if_prime(n)

    return sorted_numbers, total_sum, product, factorial_result, is_prime_result, palindromes, ascii_sums, ascii_sum_status