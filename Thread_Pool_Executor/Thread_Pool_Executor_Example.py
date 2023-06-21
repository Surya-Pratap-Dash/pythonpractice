from time import sleep, perf_counter

def task(id):
    print(f'starting the task {id}...')
    sleep(1)
    return f'Done with task {id}'

start = perf_counter()
print(task(1))
print(task(2))

finish = perf_counter()

print(f"It took {finish-start} second(s) to finish.")
