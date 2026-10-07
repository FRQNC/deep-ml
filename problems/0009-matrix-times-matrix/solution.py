def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    
    b = [list(row) for row in zip(*b)]
    c = [[sum(el * val for el, val in zip(row_a, row_b)) for row_b in b] for row_a in a]
	
    return c