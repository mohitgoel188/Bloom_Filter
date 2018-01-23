l=31
h1=[]
h2=[]
h3=[]
for i in range(l):
    h1.append(0)
    h2.append(0)
    h3.append(0)
    
def hash1(n,u):
    i=n%l
    if u==0:
      h1[i]=1
    else:
        if h1[i]==1 :
            return 1
    return 0

def hash2(n,u):
    i=(n*n)%l
    if u==0:
      h2[i]=1
    else:
        if h2[i]==1:
            return 1
    return 0

def hash3(n,u):
    i=(n*n*n)%l
    if u==0:
      h3[i]=1
    else:
        if h3[i]==1:
            return 1
    return 0

def bfil(s=[]):
    h=0
    for i in range(len(s)):
            h=l*h+ord(s[i])
    if hash1(h,1)==1:
        if hash2(h,1)==1:
            if hash3(h,1)==1:
                return 1
    return 0

def cnum(dic=[]):
    i=0
    j=0
    h=0
    for j in range(len(dic)):
        for i in range(len(dic[j])):
            h=l*h+ord(dic[j][i])
    hash1(h,0)
    hash2(h,0)
    hash3(h,0)

try:
    while 1:
        n=input("\t\tBloom Filter\n\n1.Show Content\n2.Add Item\n3.Search String\n4.Exit\n\nEnter your choice: ")
        if n==1:
            file=open("fruits.txt")
            print(file.read())
            file.close()
        elif n==2:
            file=open("fruits.txt","a")
            s=raw_input("Enter name of item: ")
            file.write("\n%s"%(s))
            print("Item Added")
            file.close()
        elif n==3:
            file=open("fruits.txt")
            fname=file.readlines()
            cnum(fname)
            s=raw_input("Enter string to search: ")
            c=bfil(s)
            if c==1:
                print("\nString may be available.\n")
            else:
                print("\nString is not available.\n")
            file.close()    
        elif n==4:
             break;
        else:
            print("\nWrong Choice!!")
finally:
    file.close();
