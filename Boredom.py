print("For you, school ended two weeks ago. It's endlessy hot and all of your friends are off doing their own things. Both of your parents are working so you're home alone, forced to deal with this boredom yourself.")
print("Sure, the first week of summer had been great. Sleeping in and staying up late, going out with your friends every day, and just hanging at home in the air-conditioned bliss. That, however, ended quickly. You woke well into the day coated in sweat with a headache.")
print("No one was home. Your friends were on vacation, and your phone lay silent. You wrack your brain for something, anything to do, but come up empty. You silently wish for anything that can hold your attention for more than 30 seconds before falling back asleep.")
print("A few hours later, you crack your eyes open and yawn, feeling your chapped lips crack. You really need some water. You try to open your eyes further but are stopped by a painful ray of sun, shining directly at your face. You groan and attempt to roll but stop as you begin to fully wake up.")
print("The first thing you notice is that you are most definitely not in bed anymore. Not even on the floor. No, the ground you are lying on is dirt.You scramble up, panicked, and cast your gaze around the area. The first thing you notice is a flock of what you barely recognize as toucans looking directly at you. Chills travel up your spine. Do you want to continue looking around at your current area?")

if user_input == "no":
	print("You curl back up on the ground, adrenaline long gone and leaving you exhausted. A few nervous tears make their way to the ground as you fall back asleep and hope it was all a dream. Unfortunately, while you are resting your sleep becomes unconciousnes as dehydration takes your body. You failed to find water soon enough and your path ends here.")
	print ("Game over!")
	exit()

if user_input == "yes":
	print("You take a calming breath and look around. The trees around you are laden down with large, round fruits. Mangoes, perhaps? You reach up and pull one from its stem, ignorning the unnerving toucans to take a bite. You instantly feel better as its juices begin to rehydrate your body. While eating the fruit you notice a dirt path ahead of you and follow it. You walk slowly and cautiously until you reach a fork in the path.  Before you can choose, you hear a voice behind you. 'So, you finally arrived'.")
	print ("You turn quickly, eyes not finding another person for as far as you can see. A small toucan hops down from a branch and lands in front of you. You shake your head and turn back around, deciding you have begun hearing things as the voice shouts at you again.'Hey! You! It is incredibly rude to ignore someone talking to you, you know?' You turn again, crouching down to look at the bird. 'Was that you, little birdy?' You chuckle to yourself as you reach out a finger to stroke its beak")
print ("You pull back as it snaps at you, wings flaring out. 'Of course it was!' it squacks at you. 'Is there anyone else you see?' You swallow and shake your head. 'What ever. It is time for you to choose' it says, spreading its wings to point down each path. You stare at it for a moment, slowly trying to process everything. The toucan sighs, clearly exhasperated. 'You wanted adventure, right? Well, you got it. Now, please. Which way would you like to go?''")

user_input = input()

if user_input == "left":
	print("You go left notice the bird is tailing you. You walk in silence for a while before reaching a large stone cliff face straight ahead of you. It's far to steep to climb, even if you had the upper body strength. You sigh and turn back, following the right path.")

elif user_input == "right":
	print("You move to walk down the right path and notice the bird tailing you.")

print("You walk for a little while, taking in your surroundings. It's hot and muggy, and clearly tropical. You can hear rushing water somewhere ahead of you. You and the bird walk a bit farther in silence as the noise gets louder and louder until you finally break out of a bunch of wound vines and are suddenly standing on the river bank. The water is all you can hear. A small bridge spreads its way across the raging river and you slowly make your way towards it.")

print ("Fate, however, doesn't want to make things easy for you. Another toucan, this one much larger than the one following you, swoops down onto the path before you. You let out a small cry of alarm and step back before noticing what exactly the bird is doing. You cannot make your way past it, and it does not seem eager to move. You glance back at the bird following you and it does what seems to be a nod. You look back at the larger bird and sigh. It looks you in the eye before opening its beak to talk. 'You may pass me and this bridge safely... for a small fee.")
print ("you groan and the bird holds up a wing to silence you. 'You must prove yourself mentally worthy of the great treasure that lies ahead. Are you sure you're capable of that?' it asks in a condescending tone. You are not sure how to respond. Were you just insulted by a bird? Are you really going to take that?")

user_input = input()

if user_input == "no":
	print("You flip the bird the bird and walk away. You can't put up with this stuff today. As you're walking, you feel nausea and fatigue start to pull at your body. A stabbing headache forces you to stop and fall to your knees. You barely begin to understand what extreme dehydration can do to the body as unconsiousnes envelops you. Unfortunately, your journey ends here. Maybe next time you should trust the random giant talking bird.")
	print ("Game over!")
	exit()

elif user_input == "yes":
    print("You sigh and nod your head, swallowing down the anger. 'Good. Now, you have to answer a few riddles. Let's start easy.'")

print("are you ready to hear it?")

question = "Big as a mountain, small as a pea, swimming through an endless, waterless sea. What am I?"

user_input = input()
while user_input != "yes":
	print("Let me know when you are ready.")
	user_input = input()

print(question)

answer = "an asteroid"
Question2 = "I am a king who is good at measuring things. What am I?"

answer2 = "a ruler"

user_input = input()

while user_input != answer:
	print("Try again!")
	user_input = input()

print("Good job.")
print(Question2)

Question3 = "The more you take, the more you leave behind. What are they?"

answer3 = "fingerprints"

user_input = input()

if user_input == "exit":
	exit()

while user_input != answer2:
	print("Come on, this isn't that hard!")
	user_input = input()
print("Hmm... perhaps you are not as dull as I assumed")
print(Question3)

user_input = input()
while user_input != answer3:
	print("Come now, this is the last one. Just think!")
	user_input = input()


print("Congratulations. You may pass to retrieve the treasure.")

print("The bird moves to the side, falling in line behind you as you cross the bridge slowly. When you collapse onto the other bank you see that the path continues winding into the forest.")
print("You walk tiredly through the woods, stepping across the occasional root. You're enjoying the pattern made on the ground caused by the light moving through the leaves when you walk face first into a stone wall.")
print("You stumble back, cursing under your breath and hearing the two toucans behind you squack with laughter. You glare up at whatever you just walked into and sigh. Cracked stone bricks are piled together, forming a doorway that leads into a small pyramid.")
print("Would you like to enter the pyramid?")
user_input = input()
if user_input == "no":
	print("You leave the pyramid and the strange feeling that came with it behind. However, the feeling gets worse. You feel a tugging in the pit of your stomach that grows until it's painful. You close your eyes to try and allow the nausea to pass. When you re open your eyes, you're standing at the temple yet again. You leave and turn the other way this time, only for the same resuts to happen. You sigh, defeated.")
if user_input == "yes":
	print("You enter the pyramid.")

print(" As you walk through the small doorway, you feel the temperature drop.It's dark inside, and you take a moment to allow your eyes to adjust. In this moment, a horrible grinding noise reaches your ears.")
print("Do you A, turn to see what it is, or B, ignore it and continue on your way?")
user_input = input()
if user_input == "A":
	print("You watch in horror as the door slowly dissapears behind you, vanishing in a small sliver of light. You attempt to pull on the door, but to no avail. The door is shut, and your only hopes of escape lie ahead.")
if user_input == "B":
	print("You continue on your way deeper into the cave, almost slipping a few times on the slick ground.")

print("While you're walking, you hear one of the birds start screeching for you to stop. Do you listen to it?")
user_input = input()
if user_input == "no":
	print ("You continue walking, ignoring the screaming bird behind you. After a minute of walking through the darkness he stops screeching, muttering something about a joke under his breath. You roll your eyes, glad you didn't take the bait.")
if user_input == "yes":
	print("You jolt to a stop, adrenaline spiking. 'What? What is it?' you ask in a panic, expecting the worst. Instead of grim or scared looks, both birds collapse in a fit of laughter. Your face burns and your anger spikes as you turn back around, stomping down the hallway.")

print("You continue your way through the pyramid, having to duck a few times to keep from slamming your head into something. After a few minutes of walking in silence, one of the birds starts screaming again. This time, however, the other promptly joins in.")
print("Do you, A, stop, or B, keep going?")
user_input = input()
if user_input == "A":
	print("Your feet act before your mind does and you stop suddenly. Thank goodness you did, too. You feel your toes just barely start to tilt forward, wriggling over nothing. It was so dark that you didn't notice the deep canyon formed in the grond. You gulp nervously and step back.")
if user_input == "B":
	print("You keep walking, annoyance eating at the corner of you mind. However, between the darkness and your preoccupied mind, you don't notice as you take a step off into ni=othing. Your journey ends here.")
	print("Game over")
	exit()
print("You step back from the edge, glad you listened to the birds. You whisper a quiet thanks to them before scanning the area, eyes just barely picking up on a rope dangling across. You cross to it, leaning over the crevice to grab it.")
print("You tug on the rope a few times and it seems sturdy enough. Would you like to trust the rope?")
user_input = input()
if user_input == "yes":
	print("You grip the rope tightly, feeling brave. You take a few steps back and run, leaping into the oblivion. Everything is great for a second until you remember your lack of upper body strength. The rope slips from your grasp and you fall. Your journey ends here.")
	print("Game over")
	exit()
if user_input == "no":
	print("You step back from the edge again, deciding to find another way across. You search through the shadowy corners of the room, coming up mostly empty. However, by the end of your search, you come up with a strong plank of wood about the length of your arm and another piece of rope.")
print("You can either A, try to attach the wood to the already hanging rope or B, attempt to make another, sturdier way of getting across.")
user_input = input()
if user_input == "A":
	print("You tie a firm knot at the base of the rope before attaching the plank of wood. You stretch the rope across and make another knot at the top. You repeat the proccess a few times until your foothold is sturdy.")
	print("You take a few steps back, oe foor on the wood. you use your other foot to push off from the ground before bringing it up to meet the other. Wind whips past your face and you cling to the rope. The next thing you know, your body hits something solid and you lower one foot, allowing it to get caught on a rock and bringing you to a stop on the other side. Congratulations.")
if user_input == "B":
	print("While looking up, you notice a thick steel hook hanging from the ceiling. You tie a knot at one end of your rope and throw it, attempting to connect them. It takes you a few tries but you finally are able to hook them together.")
	print("Using the other end of the rope, you tie a few knots around the wood until you have a solid foothold. You test it a few times before deciding it'll have to work.")
	print("You take a few steps back, oe foor on the wood. you use your other foot to push off from the ground before bringing it up to meet the other. Wind whips past your face and you cling to the rope. The next thing you know, your body hits something solid and you lower one foot, allowing it to get caught on a rock and bringing you to a stop on the other side. Congratulations.")
print("You make your way across the other side of the canyon, watching enviously as the birds flap over to you. While running your hands across the cold rock wall, you notice an unusual divot in the wall. It forms a rectangle, and the shape and size resemble a door. Your hands flit around the area until you find a small switch. Press it?")
user_input = input()
while user_input != "yes":
	print("You go back to searching the area. You find nothing, not so much as a misshaped rock. Would you like to press the button?")
	user_input = input()
print("You flip the switch and the door next to you rumbles to life. Light floods out through the opening and you enter, squinting. The room inside is very similar to all the others, but this one hosts a small pedistal. You walk to it and the light quivers.")
print("Would you like to grab the light?")
user_input = input()
while user_input != "yes":
	print("There is nothing else to do in the room. Would you like to grab the light?")
	user_input = input()
print("You reach out and encompass the light in your hands. It glows bright and warm before fading. When you open your hands again, all that is inside them is a tiny clear crystal. You hear the noise of rock grinding against rock and look up. Daylight floods he room as the birds flock out infront of you. You follow in a daze and stop outside, enjoying the feeling of sunlight on your face.")
print("Both birds look at you appreciatively. 'See you later, kid' is all the larger one says before sleep suddenly overwhelms you.")
print("You wake a few hours later, curled in bed. You sit up, casting your gaze around the room. Nothing is out of place. You just barely hear the sound of your garage door opening and your mothers car door opening and then closing.")
print("That dream felt real. Startlingly so. You laugh to yourself at your overactive imagination before getting out of bed to greet your mother. The ground swoons around you, as you realize you definitely need some water. You pad out of your room, stretching. Your muscles feel sore as you stretch them. Your mom is in the kitchen, setting a few bags on the counter. She seems tired.")
print("Would you like to tell her about your dream?")
user_input = input()
if user_input == "yes":
	print("You regail your mother with your story of toucans and magic. She laughs with you at some parts and hums curiously at the riddles. When you finish, she places a hand on your head and laughs.")
	print("'you sure have some imagination in there. You must be bored out of your mind to dream that up. I'm sorry. You know, I've been meaning to keep this a secret, but you'll need to know sooner or later.")
	print("We're going to be going on a vacation soon. Nothing too big, we're just flying up to Washington to visit some family for a few weeks. There should be enough to keep you occupied, though.")
	print("You smile and thank her. This will definitely be an exciting development, and you'll have to start packing as soon as possible.")
if user_input == "no":
	print("You smile at her and she smiles back warily. Neither of you speaks for a while and you watch silently as she puts away groceries.")
	print("'Your father and I have something to tell you tonight over dinner.' she says in a bored tone. You nod and head back into your room, scrolling through your phone until dinner.")
	print("You hear your mom calling for you a few hours later and flop off of the bed. You leave your room and make your way to the dining table. You share some hello's with your father and you all eat. Eventually, your mother sets her fork down and you look up.")
	print("'we're going to leave in a few days for a small vacation. We're going up to Washington to see some family. We'll be up there for a few weeks, so it should be fun.' You nod and finish dinner.")
	print("You re enter your room after being excused from dinner to pack. This will definitely be an exciting development.")
print("The end! Thank you for playing our game!")
exit()
