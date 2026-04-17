lst = list(map(int, input().split()))

command = input()

direction = command[0]
shift = int(command[1:])

if direction == 'R':
    if shift > 0:
        lst = lst[-shift:] + lst[:-shift]
elif direction == 'L':
    if shift > 0:
        lst = lst[shift:] + lst[:shift]

print(lst)