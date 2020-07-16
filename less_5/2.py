with open('test.txt') as f:
    lines = f.writelines()
    print('Количество строк: ', len(lines))
    for num_lines, line in enumerate(lines, start=1):
        print('{} строка содержит - {} слов'.format(num_lines, len(line.split())))
