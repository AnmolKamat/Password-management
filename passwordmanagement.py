import random,string,shelve,sys,getpass
mai=shelve.open("main")
pswddb=shelve.open("passworddb")
def passwordgenerator():
    def lowerf():
        lower=list(string.ascii_lowercase)
        return random.choice(lower)
    def upperf():
        upper=list(string.ascii_uppercase)
        return random.choice(upper)
    def numberf():
        numbers=[0,1,2,3,4,5,6,7,8,9]
        return str(random.choice(numbers))
    def specialf():
        special=list(string.punctuation)
        return random.choice(special)
    while(True):
        length=int(input("enter the password length ( 8-64 ): "))
        if length>64 or length<8:
            print("invalid lenght")
        else:
            password=list()
            func=[lowerf(),upperf(),numberf(),specialf()]
            lis=[]
            for l in range(0,length):
                password=[str(i) for i in[j for j in func]]
                for k in password:
                    if len(lis)<length:
                        lis.append(str(k))
                func=[lowerf(),upperf(),numberf(),specialf()]
            break
    random.shuffle(lis)
    return("".join(lis))
def passwordadder(url,username,password):          
    pswddb[url]=[username,password]

def main():
    print("************ PASSWORD MANAGEMENT SYSTEM ************")
    while True:
        print(" 1) add password \n 2)show all password\n 3)search passwords\n 4)delete password \n 5)exit\n \n enter your choice :\n")
        choice=int(input())
        if choice==1:
            url=input("enter the website/application :")
            username=input("enter the user name/email/mobile.no : \n")
            password=passwordgenerator()
            passwordadder(url,username,password)
        elif choice==2:
            for item in pswddb:
                print(item,":")
                print("username : ",pswddb[item][0])
                print("password : ",pswddb[item][1],"\n")
        elif choice==3:
            url=input("enter the website/application: ")
            for item in pswddb:
                if item.startswith(url):
                    print("username : ",pswddb[item][0])
                    print("password : ",pswddb[item][1])
        elif choice==4:
            url=input("enter the website/application: ")
            del pswddb[url]
        elif choice==5:
            sys.exit()

user="use"
while True:
    mainpswd=getpass.getpass()
    if mai[user]==mainpswd:
        main()
        break
    else:
        print("invalid password")
pswddb.close()
mai.close()