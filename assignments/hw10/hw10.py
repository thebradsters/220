def fibonacci(n):
    n_1, n_2 = 0, 1
    count = 0
    my_sum = 0
    while count < n:
        count += 1
        n_1 = n_2
        n_2 = my_sum
        my_sum = n_1 + n_2
    return my_sum


def double_investment(principle, rate):
    my_sum = 0
    count = principle
    while count < (principle * 2):
        count = count * (1 + rate)
        my_sum = my_sum + 1
    return my_sum


def syracuse(n):
    answer = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        answer.append(int(n))
    return answer


def goldbach(n):
    pass
