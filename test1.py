test_done = False
input("Welcome to test number 1(click Enter to continue)")
input("This test will test you on the sun, try not too look back(click Enter to continue)")
input("Good Luck! (click Enter to continue)")
while test_done == False:
    score = 100
    a = input("what is the distance of the sun to earth? a. 8 light-years b. 3 light-minutes c. 1 Nanoseconds d. 8 light-minutes: ").lower()
    if a == "d":
        print(f"correct! score: {score}")
    else:
        score -= 10
        print(f"incorrect score: {score}")
    b = input("what is the true color of the sun? a. white b. yellow c. orange d. red: ").lower()
    if b == "a":
        print(f"correct! score: {score}")
    else:
        score -= 10
        print(f"incorrect score: {score}")
    c = input("About how many earth would it take to fill up the sun? a. 10003 earths b. 1 billion earths c. 1.3 million d. 1.3 Novemnonagintillion: ").lower()
    if c == "c":
        print(f"correct! score: {score}")
    else:
        score -= 10
        print(f"incorrect score: {score}")
    d = input("What is the radius of the sun in METERS? a. 1 trillion meters b. 1 billion SOMETHING c. 696,265,000 meters d. 575,398,066 meters: ").lower()
    if d == "c":
        print(f"correct! score: {score}")
    else:
        score -= 10
        print(f"incorrect score: {score}")

    e = input("what is the sun's suface and the sun's core in FARENHEIT? a. IDK farenheit b. 1000 farenheit and 27 million farenheit c. 75368756874 foots d. 1000 farenhiet and 29 million: ").lower()
    if e == "b":
        print(f"correct! score: {score}")
    else:
        score -= 10
        print(f"incorrect score: {score}")

    f = input("how old is the sun? a. 4.6 billion years old b. 5.6 billion years old c. 4.8 billion years old d. 4.6 million years old: ").lower()
    if f == "a":
        print(f"correct! score: {score}")
    else:
        score -= 10
        print(f"incorrect score: {score}")
    g = input("Does the sun have a heartbeat, if yes tell how long per beat, if no you just no? a. IDK b. yes, 1 time every 11 years c. no d. yes, 30 - 40 per day: ").lower()
    if g == "b":
        print(f"correct! score: {score}")
    else:
        score -= 10
        print(f"incorrect score: {score}")

    h = input("how much time does it take light to reach?, a. 4 years b. 8 days and 3 hours c.53 days d. 8 minutes and 30 seconds: ").lower()
    if h == "d":
        print(f"correct! score: {score}")
    else:
        score -= 10
        print(f"incorrect score: {score}")
    i = input("how much tons of hydrogen gets converted into helium every second?, a.600 million errors  b. 84 billion tons c. 37 million earths d. 600 million: ").lower()
    if i == "d":
        print(f"correct! score: {score}")
    else:
        score -= 10
        print(f"incorrect score: {score}")

    print(f"You got {score}")
    if score < 50:
        print("you falied")
    else:
        test_done = True
        print("You Passed")