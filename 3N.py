names = ['oleg', 'ivan', 'anna']
names2 = []
for n in names:
    names2.append(n.title())
salary = [10000, 25000, 500000]
salary2 = list(filter(lambda x: x < 500000, salary))
file_salary = zip(names2, salary2)
file = open('salary.txt', 'w', encoding='utf-8')
for key in file_salary:
    file.write("%s - %s\n" % (key))
file.close()