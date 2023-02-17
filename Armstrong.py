class Armstrong():
    def __init__(self,n,a):
        self.n=n
        self.a=a
    def arm(self,n,a):
        assert n==int(n),"Enter an integer number"
        if(n>0):
            q=n%10
            w=q**3
            a=+w
            print("A:",a)
            f.arm(n//10,a)
n=153
a=0           
f=Armstrong(n,a)        
f.arm(n,a)
if(a==n):
    print("Armstrong")
else:
    print("Not Armstrong")
    
'''def arm(n):
    a=0
    b=str(n)
    for i in b:
        p=int(i)**3
        a+=p
    print(a)
    if(a==n):
        print("Yes")
    else:
        print("NO")
n=153
arm(n)
    '''