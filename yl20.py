b = ''

while not b.isnumeric():
    b = input('Sisesta tegur: ')

# b = input('Sisesta tegur: ')
# if not b.isnumeric():
#     b = input('Sisesta tegur: ')

b = int(b)

for a in range(0, 13):
    print(b, 'x', a, '=', a * b)