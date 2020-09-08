print("Made by Aryan")
print("Rock, Paper, Scissors : version--1.0")
lives = 5
score = 0
draw = 0
computer_lives = 7

while True:
      print("To begin, Enter Following Details")
      username = input("please enter username")
      password = input("please enter password")
      if username=="admin" and password =="admin":
            print("You can Play")
            print("Live rules")
            print("You will start with",lives,"lives")
            print("If you win, you will get a extra life")
            print("If you loose, your one life will be deducted")
            print("If drawn, Lives stays same")
            print("-----------------------------")
            print("DON'T USE CAPITALS")
            print("-----------------------------")
            print("To see Rules, Type rules")
            print("-----------------------------")
            print("Want to see Score, Type - display score")
            print("Want to see Draw, Type - display draw")
            print("At any point, if you wanna leave, Type exit")
            print("-----------------------------")
            print("the computer has lives as well")
            print("Can you beat the Computer....Let's See")
            print("Good Luck...!!")
            while True:
                  rps = input('Rock, Paper, Scissors?')
                  import random
                  computer = ('rock', 'paper', 'scissors')
                  computer = random.choice(computer)
                  #ROCK
                  if rps=="rock" and computer =="paper":
                        print("The Computer Choose",computer)
                        print("")
                        print("Loose")
                        print("")
                        print("")
                        lives-=1
                  if rps=="rock" and computer =="scissors":
                        print("The Computer Choose",computer)
                        print("")
                        print("Win")
                        print("")
                        print("")
                        computer_lives-=1
                        score+=1
                  #PAPER
                  if rps=="paper" and computer =="rock":
                        print("The Computer Choose",computer)
                        print("")
                        print("Win")
                        print("")
                        print("")
                        computer_lives-=1
                        score=+1
                  if rps=="paper" and computer =="scissors":
                        print("The Computer Choose",computer)
                        print("")
                        print("Loose")
                        print("")
                        print("")
                        lives-=1
                  #ROCK
                  if rps=="scissors" and computer =="paper":
                        print("The Computer Choose",computer)
                        print("")
                        print("Win")
                        print("")
                        print("")
                        computer_lives-=1
                        score=+1
                  if rps=="scissors" and computer =="rock":
                        print("The Computer Choose",computer)
                        print("")
                        print("Loose")
                        print("")
                        print("")
                        lives-=1
                  #DRAW
                  if rps=="rock" and computer =="rock":
                        print("The Computer Choose",computer)
                        print("")
                        print("Drawn")
                        print("")
                        print("")
                        draw+=1
                  if rps=="paper" and computer =="paper":
                        print("The Computer Choose",computer)
                        print("")
                        print("Drawn")
                        print("")
                        print("")
                        draw+=1
                  if rps=="scissors" and computer =="scissors":
                        print("The Computer Choose",computer)
                        print("")
                        print("Drawn")
                        print("")
                        print("")
                        draw+=1
                  #system
                  if rps == "rules":
                        print("-----------------------------------------")
                        print("RULES")
                        print("-----------------------------------------")
                        print("Rock win against Scissors")
                        print("Rock loose against Paper")
                        print("Paper win against Rock")
                        print("Paper loose against Scissors")
                        print("Scissors win against Paper")
                        print("Scissors loose against Rock")
                        print("-----------------------------------------")
                  if rps == "display lives":
                        print(lives)
                  if rps == "display score":
                        print(score)
                  if rps == "display drawn":
                        print(draw)
                  #lives
                  if lives == 0 or rps=='test':
                        print("Thanks for Playing")
                        print("You got",score,"correct")
                        print("You drawn",draw,"times")
                        stop = input("Press Enter to Exit")
                        import time
                        time.sleep(900)

                  if computer_lives == 0:
                        print("Thanks for Playing")
                        print("Computer Lost All Lives")
                        print("You got",score,"correct")
                        print("You drawn",draw,"times")
                        stop = input("Press Enter to Exit")
                        import time
                        time.sleep(900)
                  #exit
                  if rps == "exit":
                        break
      else:
            print("Username/Password is incorrect")










            
