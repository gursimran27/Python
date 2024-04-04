def last():
    print('\t\t*****WEL COME TO*****')
    print('\t############  SECTION-C   FOR [INFO TECHNOLOGY]  ############')
    print('\t*********************************************************')
    sco=0
    que2=['\tWho is the Father of the Computer?',
            '\tWhat is the full form of E-Mail?',
            '\tIn the virtual world, WWW stands for',
            '\tWhat do you call a person who uses the internet to explore and communicate?',
            '\tWho invented Compact Disc?',
            '\tWhich one of the following is not an Operating System (OS)?',
            '\tWhat do you need to use to connect to the internet?',
            '\tWhat is also known as a portable computer?',
            '\tName the device that is used to take a printout of a document from a computer?',
            '\tHow much is a byte equal to?',
            '\twhat is the default chart type in Microsoft excel?',
            '\tWhich computer virus records every movement you make on the computer?',
            '\tMail merge is a component of which of the following?',
            '\tWhich keys are used to switch between programs in windows?',
            '\tWhat is the mascot of the Linux operating system?',
            '\tLaser printer resolution is specified in terms of:',
            '\tA nibble is equal to bits?',
            '\tThe instruction about booting your system is stored in:',
            '\tWhich symbol is used to separate the username of an email address from that of an ISP?',
            '\tWhat is opps?']  
    op=['a.Charles Babbage b.Thomas Edison c.Albert Einstein d.Isaac Newton',
        'a.Electric Mail b.Exchange Mail c.Electronic Mail d.Engagement Mail',
        'a.World Without Windows b.World Wide Web c.World Wide Web Applications d.World Wide Warehouse',
        'a.Citizen b.Resident c.Cybernaut d.None of the above',
        'a.JamesT.Russell b.Fujio Masuoka c.Thomas Edison d.Martin Cooper',
        'a.Windows 10 b.Linux c.DOS d.MS Exce',
        'a.Mouse b.Modem c.CPU d.Keyboard',
        'a.Laptop b.CPU c.Monitor d.Desktop',
        'a.CPU b.Mouse c.Keyboard d.Printer',
        'a.8 bits b.16 bits c.32 bits d.64 bits',
        'a.pie chart b.line chart c.surface chart d.column chart',
        'a.Malware Android b.DoS c.Key Logger d.Trapper',
        'a.MS Word b.MS Excel c.Word Press d.MS Access',
        'a.Ctrl+TAB b.Alt+TAB c.Shift+TAB d.Shift+Enter',
        'a.Bear b.Penguin c.Lion d.whale',
        'a.DPI b.LPM c.CPM d.LSI',
        'a.4 b.8 c.16 d.32',
        'a.RAM b.CPU c.BIOS d.Register',
        'a.@ b.& c.$ d.#',
        'a.object oriented programing b.operating object program c.operate oreient programing d.opex opart program']  
    an=['a','c','b','c','a','d','b','a','d','a','d','c','a','b','b','a','a','c','a','a']
    for i in range(20):
        print(que2[i]) 
        print(op[i])
        a=input("enter your choice:")
        if(an[i]==a):
            sco+=1
        else:
            sco-=1
    return sco