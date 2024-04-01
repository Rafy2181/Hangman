
#lesson 28/03/2024

print("Welcome to the game Hangman")
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

def Hangman(AWord):

    print()
    print(' _ '*(len(AWord)))
    
AWord=input("Enter a word between 5-10 letters : ")
if(len(AWord)<5 or len(AWord)>10):
    AWord=input("Enter a word between 5-10 letters : ")


# for i in range(len(AWord)):
#     aletter=input("enter a letter : ")
#     if(aletter==AWord(len[i])):
#         print(aletter)    



# print("""
# picture 1:
#     x-------x
# """)



# print("""  
# picture 2:
#     x-------x
#     |
#     |
#     |
#     |
#     |
# """)
    

# print("""  
# picture 3:
#     x-------x
#     |       |
#     |       0
#     |
#     |
#     |
# """)


# print("""
# picture 4:
#     x-------x
#     |       |
#     |       0
#     |       |
#     |
#     |
# """)


    
# print("""
# picture 5:
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |
#     |
# """)


# print("""
# picture 6:
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |      /
#     |
# """)
    
      
    
      
# print("""  
# picture 7:
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |      / \\
#     |
# """)