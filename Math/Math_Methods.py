#!Python
#Jesse Bacon

import matplotlib.pyplot as plt
import numpy as np

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

def pascals_triangle_sums(triangle_object):
    '''
    Return the sums for a given number of rows from pascals triangle
    in list format.
    
    example:
    
    pascals_triangle_sums(build_pascals_triangle(10))
    '''
    bits = []
    z = 0
    for i in range(len(triangle_object)):
        y = triangle_object[i]
        for num in y:
            z += num
        bits.append(z)
        z = 0
    return bits

def list_of_primes( start, end ):
    assert type(start) == int, 'input a number for start'
    assert type(end) == int, 'input a number for end'
    return [ w for w in range( 3, end) \
                     if determine_prime(w) == 'prime' and w >= start ]

def list_of_primes_from_summed_squares( start, end ):
    assert type(start) == int, 'input a number for start'
    assert type(end) == int, 'input a number for end'
    return [ w for w in range( 3, end) \
                     if determine_prime(w) == 'prime' and w >= start \
            and str(float(w) / 4.0)[-2:] == '25' ]

def squares_for_primes( start, end ):
    primes = list_of_primes_from_summed_squares( start, end )
    primes_and_squares = {}
    for i in primes:
        for i2 in range(len(range(i))):
            for i3 in range(len(range(i))):
                if i2**2 + i3**2 == i:
                    primes_and_squares[i] = (i2, i3)
    return primes_and_squares

def graph_primed_roots( start, end ):
    primes = squares_for_primes( start, end )
    N = len( primes )
    ticks = ticks = tuple(sorted(primes))
    square1 = [primes[i][0] for i in sorted(primes)]
    square2 = [primes[i][1] for i in sorted(primes)]
    ind = np.arange( N )
    width = 0.36

    p1 = plt.bar( ind, square1, width, color = 'r' )
    p2 = plt.bar( ind, square2, width, color = 'b' )

    plt.ylabel( 'prime' )
    plt.title( 'Primes with Squared Sum roots' )
    plt.xticks( ind + width/2., ticks )
    plt.legend( (p1[0], p2[0]), ( 'Square1', 'Square2' ) )

    plt.show()
    return primes
