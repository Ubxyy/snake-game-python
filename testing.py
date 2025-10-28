def spam():
    global eggs
    print(eggs)
    eggs = 'spam local'
    global eggs
    print(eggs)

eggs = 'global'
spam()