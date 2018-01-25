l=31
h1=[]
h2=[]
h3=[]
filename='fruits.txt'
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

def bfil(s):
    h=0
    for i in range(len(s)):
            h=l*h+ord(s[i])
    if hash1(h,1)==1:
        if hash2(h,1)==1:
            if hash3(h,1)==1:
                return 1
    return 0

def cnum(word):
    h=0
    for letter in word:
        h=l*h+ord(letter)   #ord(x) Returns integer value of x
    hash1(h,0)
    hash2(h,0)
    hash3(h,0)

try:
    while 1:
        try:
            n=int(input("\t\tBloom Filter\n1.Add Item\n2.Search String\n3.Show Content\n4.Flush file\n5.Exit\n\nEnter your choice: "))
            if n==1:
                file=open(filename,"a")
                s=input("Enter name of item: ")
                file.write(f'\n{s}')
                cnum(s)
                print("Item Added")
                file.close()
            elif n==2:
                s=input("Enter string to search: ")
                if bfil(s):
                    print("\nString may be available.\n")
                else:
                    print("\nString is not available.\n")
                file.close()
            elif n==3:
                try:
                    file=open(filename)
                    print(file.read())
                    file.close()
                except:
                    print('No content to show yet!!!')
            elif n==4:
                try:
                    file=open(filename,'w')
                    file.close()
                    print('File Flushed.')
                except:
                    print("File don't exist yet!!!")    
            elif n==5:
                 break;
            else:
                print("\nEnter your CHOICE correctly!!!\n")
        except:
            print('\nEnter your CHOICE correctly!!!\n')
finally:
    file=open(filename)
    file.close();
