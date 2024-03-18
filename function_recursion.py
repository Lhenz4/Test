def sum_of_digits(n):
    if n < 10:
        return n
    else:
        last_degit = n % 10
        remaining_degit = n // 10

        return last_degit + sum_of_digits(remaining_degit)
    
print(sum_of_digits(123))