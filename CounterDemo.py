from collections import Counter

d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}

c1=Counter(d1)
c2=Counter(d2)

combine=c1+c2

print(combine)