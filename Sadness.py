print("This will be a very dialogue heavy game, designed to help calm and bring you to a better place. This game is in no way a substitute for professional help. If you are dealing with serious problems, please seek help from a medical prefessioanl. Are you ready to proceed?")
user_input = input()
while user_input != "yes":
    print("Take your time and simply type 'yes' when you are ready.")
    user_input = input()
print("Welcome to our game to help deal with sadness. You get home late on Friday. You make your way up the steps to your apartment before opening the door and heading inside. It's dark and rain splatters against the window panes. You flick on a single lamp to help dilute the darkness. You're cold, wet, and sad.")
print("Where would you like to go? the bedroom, bathroom, kitchen, or stay here?")
user_input = input()
if user_input == "bedroom":
    print("You walk into your bedroom and peel off your wet clothing, leaving it in a soggy pile in the corner. Would you like to go to the bathroom for a shower or get dressed?")
    user_input_2 = input()
    if user_input_2 == "shower":
        print("You walk into the small, tile room and flick on the lights. You turn the shower on as hot as it can get and step into the spray. It burns for a moment as it makes contact with your chilled skin but quickly begins to feel better. Steam is slowly curling up into the ceiling. You wash your hair slowly, savoring the feeling of being clean. You step out from under the spray a few minutes later and towel off before getting dressed in some clean pajamas. You feel better already.")
    if user_input_2 == "get dressed":
        print("You pull on a pair of clean pajamas over your still damp skin, but you're still cold. You feel slightly better.")
print("You exit into the main room.")
if user_input == "bathroom":
    print("You walk into the bathroom and flick on the lights. You can wash your face, shower, or leave.")
    user_input_3 = input()
    if user_input_3 == "shower":
        print("You peel off your wet clothing and turn on the shower. You step under the spray and flinch as it burns your chilled flesh for a second. After a moment you relax into the heat. You scrub at your face and hair before stepping out and toweling off. You feel much better already.")
    if user_input_3 == "wash your face":
        print("You bend in front of the sink and splash warm water into your face, scrubbing with some soap. You enjoy the coldness from the bitter wind outside seeping away under the gentle heat of the water. You gently pat your face dry with a soft hand towel and smile, feeling better.")
        print("Would you like to shower or leave?")
        user_input_5 = input()
        if user_input_5 == "shower":
            print("You peel off your wet clothing and turn on the shower. You step under the spray and flinch as it burns your chilled flesh for a second. After a moment you relax into the heat. You scrub at your face and hair before stepping out and toweling off. You feel much better already. Would you like to leave?")
        user_input_4 = input()
        while user_input_4 != "yes":
            print("There isn't anything else to do in here. Would you like to leave?")
            user_input_4 = input()
        if user_input_5 == "leave":
            print("You exit into the main room.")
print("You enter the main room and look around. What now?")
if user_input == "kitchen":
    print("You cross to the kitchen. The sink is full of dishes and the few house plants you have in there are looking parched. Would you like to eat, do dishes, or water the plants?")
    user_input_6 = input()
    if user_input_6 == "eat":
        print("You open the fridge, watching the small beam of light grow on the floor. You peer into the compartment and make a list of ingredients.")
        print("Would you like to make cookies, scrambled eggs, or a grilled cheese?")
        user_input_7 = input()
        if user_input_7 == "cookies":
            print("You pull the small tub of dough out of your fridge and preheat the oven. You slowly start to scoop the dough onto the tray and snag a few pinches of the dough for yourself. The cold mix of flour, eggs, and chocolate instantly makes you feel better.")
            print("You place the tray into the oven and close the door, setting the timer. What would you like to do now? You can A, wait, or B, scroll through your phone.")
            user_input_8 = input()
            if user_input_8 == "A":
                print("You wait in the dark kitchen for a few minutes, enjoying the sound of the rain and the smell of fresh baked cookies that is growing by the moment.")
            if user_input_8 == "B":
                print("You pick up your phone and open it, scrolling through the Book of Faces. You sift past most posts and stop on one of a dog. It's a puppy golden retriever playing with a small teddy bear. Your smile grows the longer you watch it.")

            print("The timer goes off and you eagerly approach the oven, opening it and looking in at the beautiful golden disks. You pull an oven mitt over your hand before grabbing the tray, placing it on a cooling rack on the counter.")
            print("They cool off in a few minutes and you stack them on a plate before turning back to the main room. You flop back on the couch with the cookies in hand and press a few buttons on the remote. You load up an easy cartoon that brought back fond memories.")
        if user_input_7 == "eggs":
            print("You grab two eggs and a bag of shredded cheese and head to the stove. You start the repetitive motion of making the eggs, and it brings back memories of sunny Saturday mornings.")
            print("You smile to yourself as images of warm sunlight and the smell of coffee and eggs with cheese flood back. You feel yourself relaxing, comforted by the familiar smells. You finish your task and pour them onto a plate.")
            print("You enter the main room and flop onto your couch, scrolling through movie options on your television. You eventually settle on an easy cartoon that brings back fond memories.")
        if user_input_7 == "grilled cheese":
            print("")
    if user_input_6 == "do dishes":
        print("You begin to load the dishes into the dish washer, hand washing the ones that wouldn't fit or couldn't go in. After a few minutes, you close the dishwasher and press the start button. The sink is empty now, and all of your dishes are clean. You feeel much better after doing something productive.")
    if user_input_6 == "water the plants":
        print("You grab a cup out of the sink and fill it with water. You gently tilt it into the dirt of each of the few pots until the dirt is glistening. You place the cup back into the sink.")
