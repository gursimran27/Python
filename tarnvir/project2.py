def math():
    print('\t\t*****WEL COME TO*****')
    print('\t############  SECTION-B   FOR [MATHEMATICS]  ############')
    print('\t*********************************************************')
    s=0
    que1=['\tWhat is the sum of 130+125+191?',
        '\tIf we minus 712 from 1500, how much do we get?',
        '\t 50 times of 8 is equal to:?',
        '\t110 divided by 10 is?',
        '\t20+(90÷2) is equal to?',
        '\tThe product of 82 and 5 is:?',
        '\tFind the missing terms in multiple of 3: 3, 6, 9, __, 15',
        '\tSolve 24÷8+2.',
        '\tSolve: 300 - (150*2)',
        '\tThe product of 121 x 0 x 200 x 25 is',
        '\t What is the next prime number after 5?',
        '\tThe circumference of the circle is also called:',
        '\t90 - 35 is equal to',
        '\t8 raised to the power 0 is equal to:',
        '\tHow many sides does a decagon have?',
        '\tThe largest 4 digit number is:',
        '\tThe square root of 5 is?',
        '\tWhat is the area of rectangle?',
        '\tThe smallest 4-digit number is:',
        '\tIf a is the side of cube, then the volume of the cube is:']
    option=['a. 335  b. 456 c. 446 d. 426',
            'a. 788 b. 778 c. 768 d. 758',
            'a. 80 b. 400 c. 800 d. 4000',
            'a. 11 b. 10 c. 5 d. None of these',
            'a. 50 b. 55 c. 65 d. 60',
            'a. 400 b. 410 c. 420 d. None of these',
            'a. 10 b. 11 c. 12 d. 13',
            'a. 5 b. 6 c. 8 d. 12',
            'a. 150 b. 100 c. 50 d. 0',
            'a. 1500 b. 0 c. 4000 d. None of these',
            'a. 6 b. 7 c. 9 d. 11',
            'a. perameter of a circle b. diameter of a circle c.radii of circle d. None of these',
            'a. 55 b.52 c.90 d.56',
            'a. 0 b. 8 c. 1 d.64',
            'a. twenty b. two c. three d. ten',
            'a. 999 b. 9999 c.10000 d. 1000',
            'a. 2.45 b. 2.2 c. 1.50 d. 2.23',
            'a. Length*Breadth b. 4*sides c. Breadth*Height d. Side+Side',
            'a. 1111 b. 9999 c. 1000 d. 0000',
            'a. 2*a b. a*3 c. a2 d. a*4']
    answers=['c','a','b','a','c','b','c','a','d','b','b','a','a','c','d','b','d','a','c','b']
    for i in range(20):
        print(que1[i]) 
        print(option[i])
        a=input("enter your choice:")
        if(answers[i]==a):
            s+=1
        else:
            s-=1
    return s