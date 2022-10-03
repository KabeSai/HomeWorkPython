import string


def task_function_3(N_alf, Step):
    alf = string.ascii_uppercase
    new_alf = []
    for char in range(0, len(alf), Step):
        new_alf.append(alf[char])

    for lette, num in zip(new_alf, range(len(new_alf))):
        if num < N_alf:
            yield lette
        else:
            break


for i in task_function_3(10, 2):
    print(i)
