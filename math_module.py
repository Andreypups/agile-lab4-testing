def factorial(n):
    # Перевіряємо, що число є цілим і невід'ємним.
    if type(n) is not int:
        raise TypeError("Число має бути цілим")

    if n < 0:
        raise ValueError("Число має бути невід'ємним")

    # Послідовно множимо числа від 1 до n.
    result = 1
    for number in range(1, n + 1):
        result = result * number

    return result
