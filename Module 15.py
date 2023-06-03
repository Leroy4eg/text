world_list = []
counts = [0, 0, 0]

for i in range (3):
    print('Введите', i + 1, 'слово:', end=' ')
    world = input()
    world_list.append(world)

text = input('Слово из текста: ')

while text != 'end':
    for index in range(3):
        if world_list[index] == text:
            counts[index] += 1
    text = input('Слово из текста: ')

print('\nПодсчет слов в тексе')
for i in range(3):
    print(world_list[i], ':', counts[i])