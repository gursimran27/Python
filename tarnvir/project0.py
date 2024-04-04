def gk():
    t=0
    print('***********INSTRUCTIONS***********')
    print("FOR EVERY CORRECT ANSWER THERE IS ONE POINT")
    print("FOR EVERY INCORRECT ANSWER YOU LOST  YOUR ONE POINTS")
    print("YOU HAVE TO GET 15 POINTS IN EACH SECTION")
    print('############  SECTION-A   FOR [general knowledge]  ############')
    que=["\tWhat is the capital of Portugal?",
        "\tWhat is the capital of America?",
        "\tWhat is the capital of Canada?",
        '\tWhat is the capital of France?',
        "\tWhat is the capital of India?",
        "\tWhat is the capital of Australia?",
        "\tWhich is the smallest state in India?",
        "\tWhich is the largest state in India?",
        "\tWhich is the national bird of America?",
        "\tWhich is the national animal  of India?",
        "\tWhen first world war end?",
        "\tWhere does the American baseball team the Tampa Bay Rays play their home games?",
        "\tWhen did William Shakespeare born?",
        "\tIn which year was The Godfather first released?",
        '''\tWhat is the name of the 2015 film about a frontiersman on a fur trading expedition in the 1820s 
        \tand his fight for survival after being mauled by a bear?''',
        '\tIn which film did Hugh Jackman star as a rival magician of the character played by Christian Bale?',
        '\tWhen did the Second World War ends?',
        '\tThe Battle of Plassey was fought in?',
        '\tThe members of the Rajya Sabha are elected by?',
        "\t'OS' computer abbreviation usually means?"]
    options=[["a.Paris","   b.Texas","    c.Ottawa","     d.Lisbon"],
            ["a.Indiana","   b.Washington d.c.","    c.California","     d.Paris"],
            ["a.paris","   b.Tronto","    c.Ottawa","     d.Lisbon"],
            ["a.paris","   b.New york","    c.Ottawa","     d.Sydney"],
            ["a.Delhi","   b.New york","    c.Mumbai","     d.Sydney"],
            ["a.Arizona","   b.Canberra","    c.Thailand","     d.Sydney"],
            ["a.Goa","   b.Punjab","    c.Rajasthan","     d.Utter Pradesh"],
            ["a.Goa","   b.Tamil Nadu","    c.Rajasthan","     d.Himachal Pradesh"],
            ["a.Emu","   b.Angry Bird","    c.peacock","     d.Bald Eagle"],
            ["a.Lion","   b.Tiger","    c.Bull","     d.Snow Monkey"],
            ["a.1945","   b.1890","    c.1964","     d.1918"],
            ["a.Tropicana Field","   b.Hamilton","    c.Brampton","     d.Russia"],
            ["a.1843","   b.2002","    c.1564","     d.1560"],
            ["a.1972","   b.2000","    c.1964","     d.1960"],
            ["a.The Inception","   b.The Revenant","    c.The Prestige","     d.God Father"],
            ["a.The Inception","   b.The Revenant","    c.The Prestige","     d.God Father"],
            ["a.1945","   b.1890","    c.1944","     d.1942"],
            ["a.1745","   b.1790","    c.1744","     d.1757"],
            ["a.elected members of the legislative assembly","   b.President","    c.Lok Sabha","     d.the people"],
            ["a.Order of Significance","   b.Operating System","    c.Optical Sensor","     d.Open software"]]
    ans=['d','b','c','a','a','b','a','c','d','b','d','a','c','a','b','c','a','d','a','b']
    for i in range(20):
        print(que[i])
        print(options[i])
        a=input("enter your choice:")
        if(ans[i]==a):
            t+=1
        else:
            t-=1
    return t