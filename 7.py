numbers = list(map(int, input().split()))

sum_even = 0
sum_odd = 0

for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print(sum_even)
print(sum_odd)