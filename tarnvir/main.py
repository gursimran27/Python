import project0
import project2
import project3
t=project0.gk()
if(t>=15):
    s=project2.math()
    if(s>=15):
        sco=project3.last()
        print(t+s+sco,'out of 60')
    else:
        print("your score is",s,'in section b')
else:
    print("your score is",t,'in section a')