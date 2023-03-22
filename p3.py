def sum_to(n:int):
    if n == 1: return 1
    else:return n+sum_to(n-1)