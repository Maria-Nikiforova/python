with open('sal.txt') as f:
    sal = []
    lines = f.readlines()
    for line in lines:
        name, salary = line.split(' - ')
        sal.append(int(salary))
        if int(salary) < 20000:
            print(line, end='')
    print('\nСредняя зп:', sum(sal)/len(sal))