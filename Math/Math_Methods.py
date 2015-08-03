#!Python
#Jesse Bacon

def determine_prime(number):
    '''
    determines prime numbers
    
    example:
    determine_prime(7)
    '''
    for i in range(2,number):
        if number % i == 0:
            return('not prime')
        else:
            continue
    return('prime')

def fibonacci_sequence1(start, end):
    '''
    pass in the number to start with and the length of the sequence

    example:

    fib_sequence = fibonacci_sequence(1, 13)
    '''
    fibs = [1,1]
    sub_fibs = []
    while len(sub_fibs) <= end:
        i = fibs[-2] + fibs[-1]
        fibs.append(i)
        if i >= start:
            sub_fibs.append(i)
    if start >= 2:
        return sub_fibs
    else:
        return fibs
    
    def build_pascals_triangle(rows):
    '''
    Build a Pascal's Triangle to the number of rows specified in Dict Form.
    Starts at row 0
    
    example:
    
    build_pascals_triangle(10)
    '''
    pt0 = [1]
    pt1 = [1,1] 
    pascals_triangle = {0:pt0, 1:pt1}
    for num in range(rows - 2):
        x = len( pascals_triangle )
        y = len( pascals_triangle ) - 1
        row = []
        row.append(1)
        passes = range(len(pascals_triangle[y]))
        for i in passes:
            if i < passes[-1]:
                a = pascals_triangle[y][i] + pascals_triangle[y][i + 1]
                row.append(a)
        row.append(1)
        pascals_triangle[len(row)-1] = row
    return pascals_triangle