number = int(input())

divisors = []
abs_number = abs(number)

for i in range(1, int(abs_number ** 0.5) + 1):
    if abs_number % i == 0:
        divisors.append(i)
        if i != abs_number // i:
            divisors.append(abs_number // i)

if number < 0:
    negative_divisors = [-d for d in divisors]
    divisors = negative_divisors + divisors

print(divisors)