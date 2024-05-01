
#lesson 28/03/2024

print("***Welcome to the game Hangman***")
print()
AWord=input("Enter a word between 5-10 letters : ")
if(len(AWord)<5 or len(AWord)>10):
    AWord=input("Enter a word between 5-10 letters : ")

def space(spRow):            #spaces function for covering the above
    while(spRow>0):
        print(" ")
        spRow-=1

space(spRow=8)         #covering function
print("""                          
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
""")
space(spRow=8)         #covering function

def Hangman(c):
    if c==0:
        return("excellent")
    if c==1:
        return("""

x-------x
        """)
        
    if c==2:
        return("""  

x-------x
|
|
|
|
|
        """)
    
    if c==3:
        return("""  

x-------x
|       |
|       0
|
|
|
        """)

    if c==4:
        return("""

x-------x
|       |
|       0
|       |
|
|
        """)


    if c==5:
        return("""

x-------x
|       |
|       0
|      /|\\
|
|
        """)

    if c==6:
        return("""
              
x-------x
|       |
|       0
|      /|\\
|      /
| 
        """)
    
      
    
    if c==7:
        return("""
x-------x
|       |
|       0
|      /|\\
|      / \\
|
***GAME OVER***   
        """)


#### main ####   
ezer='_'*(len(AWord))
print(ezer, (len(AWord)),"letters")
print()
c=0                    #count of mistaks
t=len(AWord)           #count of correct answers
while(c<7 and t>0):
    aletter=input("""Enter a letter :
              
""")
    while(len(aletter)<1 or len(aletter)>1):
        aletter=input("Enter a single letter : ")
    theWord=""
    n=0
    for i in range(len(AWord)):
        if(ord(ezer[i])!=ord("_")):         #check if the letter already evealed
           theWord=theWord+(chr(ord(ezer[i])))
        elif(ord(aletter)!=ord(AWord[i])):
           theWord=theWord+(chr(95))
        elif(ord(aletter)==ord(AWord[i])):
           theWord=theWord+chr(ord(aletter))
           n+=1                         #not a mistak adding
           t-=1                         #count of correct answers
    ezer=theWord
    if(n==0):                           #mistaks adding
        c+=1                            #count of mistaks
    print()
    print("***"+theWord+"***")
    print()
    print(Hangman(c))
    if(t==0):
        print("***you won***")
    space(spRow=10)