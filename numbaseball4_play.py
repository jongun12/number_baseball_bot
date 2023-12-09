import random as rd

while True:
    num = [1,2,3,4,5,6,7,8,9]
    check = []
    guess = []
    ans = 0
    end = 0
    score = 0
    again = 0
    for i in range(4):
        check.append(num.pop(rd.randint(0, len(num)-1)))
    
    while not end:
        right = 0
        while not right:
            guess = []
            ans = input("Please enter four different digits:")
            right = 1
            for i in ans:
                try: guess.append(int(i))
                except:
                    right = 0
            for i in guess:
                if guess.count(i) >= 2:
                    right = 0
                if len(guess) != 4:
                    right = 0
                if 0 >= i:
                    right = 0
                    print("Zero should not be included.")
        score += 1
        strike = 0
        ball = 0
        for i in range(len(check)):
            if check[i] == guess[i]:
                strike += 1
            elif guess[i] in check:
                ball += 1
        
        if strike == 0 and ball == 0:
            print("Out")
        elif strike == 4:
            print("That's correct!")
            print("You got it in", score," times!")
            end = 1
        elif strike == 0:
            print(ball,"Ball")
        elif ball == 0:
            print(strike,"Strike")
        else :
            print(strike,"Strike",ball,"Ball")

    again = input("One more time?(YES:1, NO:0) :")
    if again != "1" and again != "yes" and again != "Yes" and again != "YES":
        print("Bye Bye")
        break