lst1 = list(map(int, input().split()))

lst2 = list(map(int, input().split()))

start, end = map(int, input().split())

start_index = start - 1
end_index = end - 1

elements_to_move = lst1[start_index:end_index + 1][::-1]

lst2.extend(elements_to_move)

for i in range(end_index, start_index - 1, -1):
    del lst1[i]

print(lst1)
print(lst2)