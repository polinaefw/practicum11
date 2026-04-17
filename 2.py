numbers = list(map(int, input().split()))

new_list = [x for x in numbers if x != 3]

print(new_list)