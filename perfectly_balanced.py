""" 
[Easy] – Perfectly Balanced, as All Things Should Be (1 point)

Given a string containing only the characters x and y, find whether there are the same number of x’s and y’s. Input: string, output: boolean or truthy/falsy value.

Test Cases:

balanced("xxxyyy") => true
balanced("yyyxxx") => true
balanced("xxxyyyy") => false
balanced("yyxyxxyxxyyyyxxxyxyx") => true
balanced("xyxxxxyyyxyxxyxxyy") => false
balanced("") => true
balanced("x") => false 

"""


while True:
    xy_string = input('Type x & y string here (Type \'exit\' to exit): ')
    countx = 0;
    county = 0;
    
    if xy_string == 'exit':
        break

    for c in xy_string:
        if c == 'x':
            countx += 1;
        if c == 'y':
            county += 1;

    if countx == county:
        print(True);
    else:
        print(False);




