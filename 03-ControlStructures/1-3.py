total_tasks = 20
tasks_ok = int(input('Correct tasks: '))
if tasks_ok >= total_tasks * 0.5:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')
