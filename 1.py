numbers = []

for i in range(10):
    num = int(input())
    numbers.append(num)

new_list = []
for i in range(9):
    sum_neighbors = numbers[i] + numbers[i+1]
    new_list.append(sum_neighbors)

print(new_list)