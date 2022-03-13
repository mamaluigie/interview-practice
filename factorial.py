import helper_functions as hf
# import pdb

def factorial(n):
    # pdb.set_trace()
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return factorial(n - 1) + factorial(n - 2)

for i in range(1000):
    print(f'fac of {i}\ntime: {hf.time_for_func_to_run(factorial, i)} Seconds\n\n')


# 0, 1, 1, 