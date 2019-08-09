#returns count of numbers leeading up to n that have a greatest common divisor of 1
#repeats #1-99

def phi(n): 
    #at least 1 relative prime number since gcd of 1 and any number is 1
    #returns count of numbers where gcd==1
    count = 1
    for i in range(2, n): 
        if (greatest_common_divisor(n,i) == 1): 
            count += 1
    return count

def greatest_common_divisor(x, y): 

    # gcd(210,45)
    '''Divide 210 by 45, and get the result 4 with remainder 30, so 210=4·45+30.
    Divide 45 by 30, and get the result 1 with remainder 15, so 45=1·30+15.
    Divide 30 by 15, and get the result 2 with remainder 0, so 30=2·15+0.
    The greatest common divisor of 210 and 45 is 15.
    '''
    #if the numbers divide together without remainder, return the lesser number
    if (x%y==0): 
        return y
    else:
        #gcd(x,y) = gcd(old divisor, old remainder) 
        return greatest_common_divisor(y, x%y)

if __name__ == '__main__':
    print([phi(n) for n in range(1, 100)])
            
