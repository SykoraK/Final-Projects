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
print("You look around the room. Would you like to enter the kitchen?")
user_input_12 = input()
while user_input_12 != "yes":
    user_input_12 = input()
    print("Your stomach growls at you angrily. You should probably eat. Would you like to enter the kitchen?")
print("You cross to the kitchen. The sink is full of dishes and the few house plants you have in there are looking parched. Would you like to eat, do dishes, or water the plants?")
user_input_13 = input()
if user_input_13 == "eat":
    print("You open the fridge, watching the small beam of light grow on the floor. You peer into the compartment and make a list of ingredients.")
    print("Would you like to make cookies, scrambled eggs, or a grilled cheese?")
    user_input_14 = input()
    if user_input_14 == "cookies":
        print("You pull the small tub of dough out of your fridge and preheat the oven. You slowly start to scoop the dough onto the tray and snag a few pinches of the dough for yourself. The cold mix of flour, eggs, and chocolate instantly makes you feel better.")
        print("You place the tray into the oven and close the door, setting the timer. What would you like to do now? You can A, wait, or B, scroll through your phone.")
        user_input_15 = input()
        if user_input_15 == "A":
            print("You wait in the dark kitchen for a few minutes, enjoying the sound of the rain and the smell of fresh baked cookies that is growing by the moment.")
        if user_input_15 == "B":
            print("You pick up your phone and open it, scrolling through the Book of Faces. You sift past most posts and stop on one of a dog. It's a puppy golden retriever playing with a small teddy bear. Your smile grows the longer you watch it.")

        print("The timer goes off and you eagerly approach the oven, opening it and looking in at the beautiful golden disks. You pull an oven mitt over your hand before grabbing the tray, placing it on a cooling rack on the counter.")
        print("They cool off in a few minutes and you stack them on a plate before turning back to the main room. You flop back on the couch with the cookies in hand and press a few buttons on the remote. You load up an easy cartoon that brought back fond memories.")
    if user_input_14 == "eggs":
        print("You grab two eggs and a bag of shredded cheese and head to the stove. You start the repetitive motion of making the eggs, and it brings back memories of sunny Saturday mornings.")
        print("You smile to yourself as images of warm sunlight and the smell of coffee and eggs with cheese flood back. You feel yourself relaxing, comforted by the familiar smells. You finish your task and pour them onto a plate.")
        print("You enter the main room and flop onto your couch, scrolling through movie options on your television. You eventually settle on an easy cartoon that brings back fond memories.")
    if user_input_14 == "grilled cheese":
        print("You pull out all of the ingredients and set the pan onto the stove to start heating up. You put all of the ingredients together and lightly butter both sides, setting it into the pan.")
        print("you smile at the sizzling noise. That and the smell bring back fond memories from when you were younger. You flip the sandwich to reveal a perfect golden crust. You allow it to cook for a bit longer before flipping it onto a plate.")
        print("cutting into it allows the melted cheese to flow freely. You smile and walk into the main room, rolling back onto your couch. You hit a few buttons before finally settling on an easy cartoon that you watched many times when you were younger.")
if user_input_13 == "do dishes":
    print("You begin to load the dishes into the dish washer, hand washing the ones that wouldn't fit or couldn't go in. After a few minutes, you close the dishwasher and press the start button. The sink is empty now, and all of your dishes are clean. You feeel much better after doing something productive.")
if user_input_13 == "water the plants":
    print("You grab a cup out of the sink and fill it with water. You gently tilt it into the dirt of each of the few pots until the dirt is glistening. You place the cup back into the sink.")
    print("Would you like to do the dishes or eat?")
    user_input_16 = input()
    if user_input_16 == "eat":
        print("You open the fridge, watching the small beam of light grow on the floor. You peer into the compartment and make a list of ingredients.")
        print("Would you like to make cookies, scrambled eggs, or a grilled cheese?")
    user_input_17 = input()
    if user_input_17 == "cookies":
        print("You pull the small tub of dough out of your fridge and preheat the oven. You slowly start to scoop the dough onto the tray and snag a few pinches of the dough for yourself. The cold mix of flour, eggs, and chocolate instantly makes you feel better.")
        print("You place the tray into the oven and close the door, setting the timer. What would you like to do now? You can A, wait, or B, scroll through your phone.")
        user_input_18 = input()
        if user_input_18 == "A":
            print("You wait in the dark kitchen for a few minutes, enjoying the sound of the rain and the smell of fresh baked cookies that is growing by the moment.")
        if user_input_18 == "B":
            print("You pick up your phone and open it, scrolling through the Book of Faces. You sift past most posts and stop on one of a dog. It's a puppy golden retriever playing with a small teddy bear. Your smile grows the longer you watch it.")
        print("The timer goes off and you eagerly approach the oven, opening it and looking in at the beautiful golden disks. You pull an oven mitt over your hand before grabbing the tray, placing it on a cooling rack on the counter.")
        print("They cool off in a few minutes and you stack them on a plate before turning back to the main room. You flop back on the couch with the cookies in hand and press a few buttons on the remote. You load up an easy cartoon that brought back fond memories.")
    if user_input_17 == "eggs":
        print("You grab two eggs and a bag of shredded cheese and head to the stove. You start the repetitive motion of making the eggs, and it brings back memories of sunny Saturday mornings.")
        print("You smile to yourself as images of warm sunlight and the smell of coffee and eggs with cheese flood back. You feel yourself relaxing, comforted by the familiar smells. You finish your task and pour them onto a plate.")
        print("You enter the main room and flop onto your couch, scrolling through movie options on your television. You eventually settle on an easy cartoon that brings back fond memories.")
    if user_input_17 == "grilled cheese":
        print("You pull out all of the ingredients and set the pan onto the stove to start heating up. You put all of the ingredients together and lightly butter both sides, setting it into the pan.")
        print("you smile at the sizzling noise. That and the smell bring back fond memories from when you were younger. You flip the sandwich to reveal a perfect golden crust. You allow it to cook for a bit longer before flipping it onto a plate.")
        print("cutting into it allows the melted cheese to flow freely. You smile and walk into the main room, rolling back onto your couch. You hit a few buttons before finally settling on an easy cartoon that you watched many times when you were younger.")
    if user_input_16 == "do dishes":
        print("You begin to load the dishes into the dish washer, hand washing the ones that wouldn't fit or couldn't go in. After a few minutes, you close the dishwasher and press the start button. The sink is empty now, and all of your dishes are clean. You feeel much better after doing something productive.")
        print("There's nothing else to do here. You enter the main room and sit on your couch, flipping on an easy movie that you remember watching repeatedly in your childhood.")
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
            print("You pull out all of the ingredients and set the pan onto the stove to start heating up. You put all of the ingredients together and lightly butter both sides, setting it into the pan.")
            print("you smile at the sizzling noise. That and the smell bring back fond memories from when you were younger. You flip the sandwich to reveal a perfect golden crust. You allow it to cook for a bit longer before flipping it onto a plate.")
            print("cutting into it allows the melted cheese to flow freely. You smile and walk into the main room, rolling back onto your couch. You hit a few buttons before finally settling on an easy cartoon that you watched many times when you were younger.")
    if user_input_6 == "do dishes":
        print("You begin to load the dishes into the dish washer, hand washing the ones that wouldn't fit or couldn't go in. After a few minutes, you close the dishwasher and press the start button. The sink is empty now, and all of your dishes are clean. You feeel much better after doing something productive.")
    if user_input_6 == "water the plants":
        print("You grab a cup out of the sink and fill it with water. You gently tilt it into the dirt of each of the few pots until the dirt is glistening. You place the cup back into the sink.")
        print("Would you like to do the dishes or eat?")
        user_input_9 = input()
        if user_input_9 == "eat":
            print("You open the fridge, watching the small beam of light grow on the floor. You peer into the compartment and make a list of ingredients.")
            print("Would you like to make cookies, scrambled eggs, or a grilled cheese?")
        user_input_10 = input()
        if user_input_10 == "cookies":
            print("You pull the small tub of dough out of your fridge and preheat the oven. You slowly start to scoop the dough onto the tray and snag a few pinches of the dough for yourself. The cold mix of flour, eggs, and chocolate instantly makes you feel better.")
            print("You place the tray into the oven and close the door, setting the timer. What would you like to do now? You can A, wait, or B, scroll through your phone.")
            user_input_11 = input()
            if user_input_11 == "A":
                print("You wait in the dark kitchen for a few minutes, enjoying the sound of the rain and the smell of fresh baked cookies that is growing by the moment.")
            if user_input_11 == "B":
                print("You pick up your phone and open it, scrolling through the Book of Faces. You sift past most posts and stop on one of a dog. It's a puppy golden retriever playing with a small teddy bear. Your smile grows the longer you watch it.")
            print("The timer goes off and you eagerly approach the oven, opening it and looking in at the beautiful golden disks. You pull an oven mitt over your hand before grabbing the tray, placing it on a cooling rack on the counter.")
            print("They cool off in a few minutes and you stack them on a plate before turning back to the main room. You flop back on the couch with the cookies in hand and press a few buttons on the remote. You load up an easy cartoon that brought back fond memories.")
        if user_input_10 == "eggs":
            print("You grab two eggs and a bag of shredded cheese and head to the stove. You start the repetitive motion of making the eggs, and it brings back memories of sunny Saturday mornings.")
            print("You smile to yourself as images of warm sunlight and the smell of coffee and eggs with cheese flood back. You feel yourself relaxing, comforted by t\he familiar smells. You finish your task and pour them onto a plate.")
            print("You enter the main room and flop onto your couch, scrolling through movie options on your television. You eventually settle on an easy cartoon that brings back fond memories.")
        if user_input_10 == "grilled cheese":
            print("You pull out all of the ingredients and set the pan onto the stove to start heating up. You put all of the ingredients together and lightly butter both sides, setting it into the pan.")
            print("you smile at the sizzling noise. That and the smell bring back fond memories from when you were younger. You flip the sandwich to reveal a perfect golden crust. You allow it to cook for a bit longer before flipping it onto a plate.")
            print("cutting into it allows the melted cheese to flow freely. You smile and walk into the main room, rolling back onto your couch. You hit a few buttons before finally settling on an easy cartoon that you watched many times when you were younger.")
        if user_input_9 == "do dishes":
            print("You begin to load the dishes into the dish washer, hand washing the ones that wouldn't fit or couldn't go in. After a few minutes, you close the dishwasher and press the start button. The sink is empty now, and all of your dishes are clean. You feeel much better after doing something productive.")
            print("There's nothing else to do here. You enter the main room and sit on your couch, flipping on an easy movie that you remember watching repeatedly in your childhood.")
print("You watch through your movie and before you know it the credits scenes are rolling. You glance at the clock in your kitchen and read that it's 11:37. You slowly stand while yawning and stretching.")
print("You turn the television off and watch ass all the light blinks offThe absense of that sound allows you to hear that the storm outside is still going strong. Rain is slamming against your window and wind howls through the streets.")
print("You yawn again, eye lids drooping to half mast. Fatigue pulls at your limbs. Would you like to go to bed?")
user_input_11 = input()
while user_input_11 != "yes":
    print("You feel more drained by the second. You should really go to bed. Would you like to go to the bedroom?")
    user_input_11 = input()
print("You shuffle to your bedroom, turning off lights as you go. You shut your bedroom door and walk to the joined bathroom where you brush your teeth ")
print("You re enter your room and ungracefully throw yourself onto the bed. You crawl beneath the covers and curl up tight. The rain is still pounding at the windows above your bed and you fall asleep to the rhythmic thumping.")
print("You wake up later than you usually would. You sit up and look at the muted light coming in through the windows. The storm from last night has passed, leaving only a slight drizzle and a thin layer of gray clouds.")
print("You yawn and stretch, feeling your shoulders and back crack with satisfying pops. Would you like to get out of bed?")
user_input_19 = input()
if user_input_19 == "yes":
    print("You stand and shiver slightly as your bare feet hit the cold ground. You walk out of your room and to the kitchen. Would you rather have coffee or tea?")
    user_input_20 = input()
    if user_input_20 == "coffee":
        print("You press a few buttons on the coffee machine and watch as it hypnotically flows into your cup. The smell makes you want to drink it straight from the machine.")
    if user_input == "tea":
        print("You fill a mug with water and place it in the microwave. While it's heating up, you select a teabag. The microwave beeps at you and you carefully pull out the mug, allowing the tea to steep. The soft steam coming off of the drink brings a small smile to your lips.")
    print("You leave the kitchen with your drink and walk into the main room to sit on the couch.")
if user_input_19 == "no":
    print("You decide you need just a little bit more sleep and fall back onto your pillow, falling back asleep quickly. You wake about an hour later, feeling a bit more ready to face the day.")
    print("You get out of bed and shiver as your feet hit the cold ground. You make your way to the kitchen, needing something to drink. Would you rather have coffee or tea?")
    user_input_21 = input()
    if user_input_21 == "coffee":
        print("You press a few buttons on the coffee machine and watch as it hypnotically flows into your cup. The smell makes you want to drink it straight from the machine.")
if user_input == "tea":
    print("You fill a mug with water and place it in the microwave. While it's heating up, you select a teabag. The microwave beeps at you and you carefully pull out the mug, allowing the tea to steep. The soft steam coming off of the drink brings a small smile to your lips.")
print("You leave the kitchen with your drink and walk into the main room to sit on the couch.")
print("You sit there for a few minutes, sipping your drink and listening to the light pinging of the rain on your windows. It's very peaceful, and you wouldn't want to be anywhere else.")
print("The silence is broken by your phone ringing. You jump at the unexpected sound and pick it up, groaning when you see it's your boss calling.")
print("Would you like to answer it?")
user_input_22 = input()
if user_input_22 == "yes":
    print("You put on your best happy voice and answer, asking them chipperly what they're calling you for. They respond in the same gravelly voice they always do, saying that they need you to show up early on monday to help train a new employee.")
    print("Do you accept?")
    user_input_23 = input()
    if user_input_23 == "yes":
        print("You accept through gritted teeth. Your boss mutters a quick 'good' and hangs up.")
    if user_input == "no":
        print("you politely explain that you cannot come early. Your boss mutters a few things you can't wuite make out followed by 'fine!' before hanging up. You sigh and set your phone down, going back to your silent contemplation of the outside clouds.")
if user_input_22 == "no":
    print("You decide to let this one go to voicemail to avoid any extra stress.")
print("Too soon, your drink is gone and you're staring at the bottom of your cup. You stand and walk into the kitchen, placing it in the sink. Would you like to make breakfast?")
user_input_24 = input()
if user_input_24 == "yes":
    print("You decide to keep it simple for today and pop a few pieces of bread into the toaster. They pop out a few minutes later, a perfect golden brown. You spread some jelly onto them and place them on a plate.")
    print("You walk back to the couch and sit, munching on the toast and scrolling through your phone. There's not much to see, just the usual updates. A few people have posted pictures of their dogs. You appreciate those ones the most.")
    print("You stay like that until your toast is gone. You get up and go to put away your plate. You're bored, as there isn't much for you to do other than watch tv or scroll through your phone.")
    print("You decide to go and take a walk around your neighborhood.")
if user_input_24 == "no":
    print("you aren't feeling too hungry, so you just sit on your couch and scroll through your phone until you're bored. You place your phone down and think about what to do. After a few minutes, you decide to take a walk around your neighborhood.")
print("You walk to your room and grab your shoes. You put them on and tie the laces tight before getting up and leaving your apartment. You double check that you have your key before locking the door.")
print("The rain has stopped, leaving a thin layer of mist on the ground. The sky is still overcast, but you don't mind. You walk around the block, enjoying the bit of breeze hitting your face.")
print("There's not many people on the streets today, so you walk with your eyes up, scanning all of the different patterns the clouds are making. You barely keep yourself from falling when you feel something hit your foot. You stumble and look back.")
print("A dog is lying across the sidewalk. It's on its side, breathing heavily out of its mouth. You see a splotch of blood staining the golden fur.")
print("Would you like to help the dog?")
user_input_25 = input()
while user_input_25 != "yes":
    user_input_25 = input()
    print("The dog looks at you sadly out of the corner of its eye, continuing to breathe heavily. Do you help the dog?")
print("You crouch next to the dog. It's small enough to carry, but there's no animal hospitals in your town. You have a first aid kit at home. Do you take the dog home?")
user_input_26 = input()
while user_input_26 != "yes":
    user_input_26 = input()
    print("You stand and make to move away. The dog whimpers at you as its eye rolls back. Its breathing begins to slow.")
print("You wrap the dog in your arms, lifting carefully. It lets out a whine but slumps against you as you make your way back home.")
print("You get back to the apartment and are somehow able to unlock and open the door without trouble. You take the dog to the bathroom and spread out a towel using your feet as best you can. When it's spread, you crouch and slowly lower the dog.")
print("The first aid kit is under the sink, so you throw open the cabinet and pull it out. You open it and look at the materials you have.")
print("Would you rather work with the gauze, bandages, or disinfectant first?")
user_input_27 = input()
if user_input_27 == "gauze":
    print("You grab the gauze and measure it against the wound. You snip a piece off and place it to the side for later.")
    print("Would you rather move on to the bandages or disinfectant?")
    user_input_28 = input()
    if user_input_28 == "bandages":
        print("You pull out the bandages and start unwinding them, making sure you have enough to wrap around the dogs side a few times. You set them aside to use later.")
    if user_input_28 == "disinfectant":
        print("you pull out the tube of disinfectant.")
if user_input_27 == "bandages":
    print("You pull out the bandages and start unwinding them, making sure you have enough to wrap around the dogs side a few times. You set them aside to use later.")
    print("Do you move on to the gauze or disinfectant?")
    user_input_29 = input()
    if user_input_29 == "gauze":
        print("You grab the gauze and measure it against the wound. You snip a piece off and place it to the side for later.")
    if user_input_29 == "disinfectant":
        print("you pull out the tube of disinfectant.")
if user_input_27 == "disinfectant":
    print("You pull out the tube of disinfectant.")

print("You open the tube and squeeze a small amount of the paste onto your finger. Very carefully, you begin to apply the paste to the wound. The dog flinches at first, but relaxes.")
print("After there's a layer of medicine, you grab the gauze and place it onto the paste. It sticks and you apply a slight pressure. You start to slowly wind the bandages around the dogs midsection to keep everything secure.")
print("The dogs breaths even out and so do yours. You stand and make your way to the kitchen. Do you get the dog water, food, or both?")
user_input_30 = input()
if user_input_30 == "water":
    print("You fill a shallow bowl with cool water and carry it back to the bathroom. You place it next to the dog and help him move to the point that he's lying upright. He laps eagerly at the water and looks at you gratefully.")
if user_input_30 == "food":
    print("You look in your fridge and find some of a left over sandwich from a few days ago. You put it onto a plate and carry it back into the bathroom. You set it on the floor and help the dog up, so that he's now lying in an upright position. He eats the sandwich and looks at you gratefully.")
if user_input_30 == "both":
    print("You grab a bowl and fill it with water. You place that on your counter while you search your fridge. You find half of a sandwich you had left over from a few days ago and put it on a plate.")
    print("you re enter the bathroom and gently place down the bowl and plate. You carefully help the dog up, so he's lying in an upright position. He lunges for the sandwich and eats it in a few bites. He goes for the water next and laps it up. He looks up at you gratefully after it's finished.")
print("You pat the dog on the head and it nuzzles into the touch. He seems happer now, and he pulls himself onto your lap, placing his head onto your stomach. He falls asleep quickly, and you'd feel too bad to wake him.")
print("You stroke his head and think about how you found him. He doesn't have a collar, and judging by how he'd been hurt and how hungry he'd seemed, he can only be a stray. Even his fur is dirty and matted.")
print("A thought hits you. The more you think about it, the better it seemed. You were in a dog friendly apartment and you lived on the second floor. It'd be easy to run him outside. There's a field of grass surrounding the building that you're sure he'd like.")
print("Do you want to keep the dog?")
user_input_31 = input()
while user_input_31 != "yes":
    user_input_31 = input()
    print("You feel a pang of guilt as the thought hits you. He doesn't have anyone, and you've always waned to have a dog. Do you want to keep him?")
print("You stroke the dogs head as you reach your decision. You'll need to go shopping soon to get him some stuff, but he'll be fine for now. He wiggles a bit in his sleep, a leg sticking out and ficking aroung, like he's running.")
print("His eyes flick oepn after a moment. They meet yours, and his mouth splits into a wide grin, with his tounge hanging out. You can't help but laugh and smile back at him. You couldn't be happier to have a friend to come back to every day.")
print("The end! Thank you for playing our game!")
