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

def prime_remainder( b ):
    x = str(float(b) / 4.0)[-2:]
    if x == '25':
        remainder = 1
    elif x == '75':
        remainder = 3
    return remainder

def investigate_primes( start, end ):
    solutions = {}
    for b in list_of_primes(start,end):
        remainder = prime_remainder( b )
        for i in range(0,b):
            for i2 in range(0,b):
                if i**3 == b:
                    solutions[b] = (triplcate, (i), remainder )
                elif i**3 + i2**2 == b:
                    solutions[b] = ('triplicate plus square',  (i, i2), remainder )
                elif i**3 + i**2 == b:
                    solutions[b] = ('triplicate plus square of same', b, (i), remainder )
                elif i**2 + i == b:
                    solutions[b] = ('square plus same', (i), remainder )
    return solutions

def prime_remainder( b ):
    x = str(float(b) / 4.0)[-2:]
    if x == '25':
        remainder = 1
    elif x == '75':
        remainder = 3
    return remainder

def investigate_primes( start, end ):
    solutions = {}
    for b in list_of_primes(start,end):
        remainder = prime_remainder( b )
        for i in range(0,b):
            for i2 in range(0,b):
                if i**3 == b:
                    solutions[b] = ('triplcate', (i), remainder )
                elif i**3 + i2**2 == b:
                    solutions[b] = ('triplicate plus square',  (i, i2), remainder )
                elif i**3 + i**2 == b:
                    solutions[b] = ('triplicate plus square of same', b, (i), remainder )
                elif i**2 + i == b:
                    solutions[b] = ('square plus same', (i), remainder )
    return solutions

def graph_primed_suspects( start, end ):
    primes = investigate_primes( start, end ) 
    N = len( primes )
    ticks = tuple(sorted(primes))
    t_plus_s_square1 = [primes[i][1][0] for i in sorted(primes) if primes[i][0] == 'triplicate plus square' ]
    t_plus_s_square2 = [primes[i][1][1] for i in sorted(primes) if primes[i][0] == 'triplicate plus square' ]
    #t1 = [primes[i][1][0] for i in sorted(primes) if primes[i][0] == 'triplicate' ]
    #t2 = [primes[i][1][1] for i in sorted(primes) if primes[i][0] == 'triplicate' ]
    #t_plus_same_square1 = [primes[i][1][0] for i in sorted(primes) if primes[i][0] == 'triplicate plus square of same' ]
    #t_plus_same_square2 = [primes[i][1][1] for i in sorted(primes) if primes[i][0] == 'triplicate plus square of same' ]
    #s_plus_same1 = [primes[i][1][0] for i in sorted(primes) if primes[i][0] == 'square plus same' ]
    #s_plus_same2 = [primes[i][1][1] for i in sorted(primes) if primes[i][0] == 'square plus same' ]
    
    ind = np.arange( N )
    width = 0.12

    p1 = plt.bar( ind, t_plus_s_square1, width, color = 'b' )
    p2 = plt.bar( ind, t_plus_s_square2, width, color = 'r' )
    #p3 = plt.bar( ind, t1, width, color = 'g' )
    #p4 = plt.bar( ind, t2, width, color = 'y' )
    #p5 = plt.bar( ind, t_plus_same_square1, width, color = 'k' )
    #p6 = plt.bar( ind, t_plus_same_square2, width, color = 'c' )
    #p7 = plt.bar( ind, s_plus_same1, width, color = 'm' )
    #p8 = plt.bar( ind, s_plus_same2, width, color = 'w' )

    plt.ylabel( 'Prime' )
    plt.title( 'Primes Investigation' )
    plt.xticks( ind + width/2., ticks )
    #plt.legend( (p1[0], p2[0]), ( 'Square1', 'Square2' ) )

    plt.show()
    return primes

def divisibility_by_1_20( num ):
    #assert type(int(num)) == int, 'Pass a numeric value for num'
    #assert fails on large numbers
    try:
        divisibles = []
        alt_sum = alternating_sum(num)
        alt_sum_b3rl = alternating_sum_b3_right_to_left(num)
        series = [float(w) for w in str(num)[:]]
        op1 = 0
        str_num = str(num)
        if num % 2 == 0:
            divisibles.append(2)
        for i in series: op1 += i
        if op1 % 3 == 0:
            divisibles.append(3)
        if int(str(num)[-2:]) % 4 == 0:
                divisibles.append(4)
        if series[-1] in [0,5]:
            divisibles.append(5)
        if 2 in divisibles and 3 in divisibles:
            divisibles.append(6)
        if alt_sum_b3rl % 7 == 0:
            divisibles.append(7)
        str_num = str(num)
        if len(str_num) >= 3:
            running_sum = 0
            x_8 = str_num[-3:]
            x_sums = []
            for item in x_8:
                x_sums.append(int(item))
            running_sum = 0
            x_8 = str_num[-3:]
            x_sums = []
            for item in x_8:
                x_sums.append(int(item))
            y = (x_sums[0] * 4 + x_sums[1] * 2 + x_sums[2])
            if y % 8 == 0:
                 divisibles.append(8)
        elif num % 8 == 0:
            divisibles.append(8)
        running_sum = 0
        for item in [int(w) for w in str_num]: 
            running_sum += item
        if running_sum % 9 == 0:
            divisibles.append(9)
        if str_num[-1] == '0':
            divisibles.append(10)
        if alt_sum % 11 == 0:
            divisibles.append(11)
        if 2 in divisibles and 3 in divisibles:
            divisibles.append(12)
        if alt_sum_b3rl % 13 == 0:
            divisibles.append(13)
        if 2 in divisibles and 7 in divisibles:
            divisibles.append(14)
        if 3 in divisibles and 5 in divisibles:
            divisibles.append(15)
        if len(str_num) >= 4:
            sub_num_16 = int(str_num[-4:])
        if sub_num_16 % 16 == 0:
            divisibles.append(16)
        elif num % 16 == 0:
            divisibles.append(16)
        if num % 17 == 0:
            divisibles.append(17)
        if 2 in divisibles and 9 in divisibles:
            divisibles.append(18)
        if num % 19 == 0:
            divisibles.append(19)
        if int(str_num[-2:]) % 20 == 0 or str_num[-2:] == '00':
            divisibles.append(20)
        return divisibles
    except:
        print('Pass in convertable Numeric Values')

def divisibility_by3_large_numbers(num):
    assert type(int(num)) == int, 'Pass a numeric value for num'
    series = [float(w) for w in str(num)[:]]
    op1 = [w for w in series if w in [1,4,7]]
    op2 = [w for w in series if w in [2,5,8]]
    x, y, = 0, 0
    for i in op1: x += i
    for i in op2: y += i
    if (x + y) % 3 == 0:
        return 3

def alternating_sum(num):
    str_num = str(num)
    running_sum = 0
    x_sums = [int(c) for c in str_num]
    for i in range(len(x_sums)):
        if i%2 == 0:
            running_sum += x_sums[i]
        if i%2 == 1:
            running_sum -= x_sums[i]
    return running_sum

def alternating_sum_b3_right_to_left(num):
    str_num = str(num)
    running_sum = 0
    x_sums = []
    while len(str_num) > 3:
        x = str_num[-3:]
        str_num = str_num[:-3]
        x_sums.append(int(x))
    x_sums.append(int(str_num))
    for i in range(len(x_sums)):
        if i%2 == 0:
            running_sum += x_sums[i]
        if i%2 == 1:
            running_sum -= x_sums[i]
    return running_sum

def graph_divisibility(num):
    divisions = divisibility_by_1_20(num)
    div_tuples = tuple(divisions)
    values = []
    for i in divisions:
        values.append(num / i)
    sorted(values)
    N = len( divisions )
    ticks = div_tuples
    ind = np.arange( N )
    width = 0.36

    p1 = plt.bar( ind, values, width, color = 'g' )

    plt.ylabel( 'Value' )
    plt.title( 'Divsibility Pattern' )
    plt.xticks( ind + width/2., ticks )

    plt.show()
    return divisions
    