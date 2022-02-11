def guess_range():
    """This function prompts the user for a choice of default or custom range then prompts the user for the ranges if custom is chosen, then it generates a random number within that range and returns it to main"""
    import random
    while(True):
        x = input("'1' for Default Range (1-100)\n'2' for Customized Range\nChoice: ")
        if (x == '1'):
            RNG = random.randint(1, 100)
            print("Low: 1\nHigh:100")
            return RNG
        elif (x == '2'):
            low = int(input("Enter the low number for the range: "))
            high = int(input("Enter the high number for the range: "))
            flag = True
            while(flag):
                if (low > high):
                    print("Low:",low,"\nHigh:",high)
                    low = int(input("The low number was greater than the high number, please enter another low number: "))
                else:
                    flag = False
                    print("Low:",low,"\nHigh:",high)
            RNG = random.randint(low, high)
            return RNG
        else:
            ()

def easy():
    '''easy mode, user has unlimited tries to guess the number'''
    print("""
You are now playing easy mode.
In this mode, the computer will generate a random number and you have an unlimited number of tries to guess the number.
If at any time you would like to quit, enter a negative number.
""")  
    randNum = guess_range()  
    count = 0   
    track = [] 
    a = True
    b = False
    while (a):
        x = integer()
        if (x == randNum):
            count = count + 1   
            track.append(x)     
            print("Your guesses:", track, "\nCongratulations! you guessed", x, "and that was the correct answer! \nIt took", count, "tries for you to guess the correct number. Thank you for playing", user, ":)")    #Maia, print guesses
            a = b   
        elif (x > randNum):
            count = count + 1   
            track.append(x)     
            print("Your guesses:", track, "\nSorry, that is incorrect. Your guess is too high, try again.")   
        elif (x < 0):
            print("Thanks for playing!")
            a = b
        elif (x < randNum):
            count = count + 1   
            track.append(x)     
            print("Your guesses:", track, "\nSorry, that is incorrect. Your guess is too low, try again")   

def game():
   a = True
   b = False
   while(a):
       if play == "yes":   
        print('''Hello, and thank you for playing the game''', user,".")


def Menu():
    """This function greets the user and explains the game and uses a menu"""
    
    while(True):
        x = input("Difficulty: \n'1' for Easy\n'2' for Hard\n'3' for Switch\n'4' to Quit\nChoice: ")
        if (x == '1'):
            return 'easy'
        elif (x == '2'):
            return 'hard'
        elif (x == '3'):
            return 'switch'
        elif (x == '4'):
            return 'quit'
        else:
            ()

def introduction():
    print("Hello", name,"you have entered a game where you will have lots of fun playing.")
    print("You will be guessing for numbers in the range of 0-100.")
    print("There are three modes you are able to play from.")
    print("The first mode is easy where you will be allowed unlimited tries to guess the number correctly.(try your best to guess as few as possible)")
    print("The second mode is hard, where you will be allowed only 7 guesses to get the correct answer.(A message will pop up if you couldn't get the number in 7 tries)")
    print("The final mode is switch, where you will switch places with the computer and you will choose a number from 0-100 for the computer to guess, but you don't enter the number into the program.")
    print("You are allowed to exit out the game anytime.")
    print("With all this information, you are set to have the best time of your life! Enjoy the game!")



def switching():
    no = 'no'
    l = list(range(1,100))
    low = 0
    high = len(l)
    b = 0
    while (no == 'no'):
        while low <= high:
            mid = int((low+high)/2)
            item = l[mid]
            b += 1
            print("computer guess:", l[mid])
            u = input("Did the computer guess the number right?(yes/high/low): ")
            if u == 'yes':
                print("computer guess:", l[mid])
                return mid
            elif u == 'high':
                high = mid - 1
            elif u == 'low':
                low = mid + 1
            else:
                ()


    print("The computer guessed your number, how much fun is that :-)")
    l = list(range(0,100))
    print("Hi there, you have chosen the game mode switch. The computer and you have switched spots and the computer will try to guess your number.")

def appending(g):
    guesslist =[]
    usernumber = input("your number guess: ")
    guesslist.append(g)
    print("This,", usernumber,"is a incorrect guess")
    



def answer():
    ''' Compares the guess to random number and says if it is correct or not'''
    x = guess_range()   
    guess = int(input("Enter guess: "))     
    if guess == x:  
        print("Congratualations! You guessed", guess, "and the correct answer was", x,"!")
    else:   
        print("Sorry, that is not the correct answer.")





#MAIN

   

name = input("Welcome to python's guessing game, please a provide a username for the game: ")
introduction()

flag = True
while(flag):
    x = Menu()
    if (x == 'easy'):
        n = guess_range()
        easy()       
    elif(x == 'hard'):
        n = guess_range()
        final = hard(n)
        if (final == n):
            print("Correct! The answer was: ", n)
        else:
            print("Incorrect! The answer was: ", n)
        print()
    elif(x == 'switch'):
        n = guess_range()
        switching()
        print()
    elif(x == 'quit'):
        print("Thanks for playing!")
        flag = False
    else:
       ()