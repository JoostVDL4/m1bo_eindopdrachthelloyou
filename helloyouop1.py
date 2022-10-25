import os
def tutorial():                 
  os.system("cls") 
  choices = ["a","b",]
  print("This story is told in an first person perspective, meaning that you will experience the story from the eyes of the protaganist. You can make choices in the story, you always have 2 choices to choice from. Do you want to start\n A Yes \n B No")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        start()
    elif userInput == "b":
        quit()
    else: 
      print("Please enter a valid option.")  
def start():
  os.system("cls") 
  choices = ["a","b",]
  print("You live on a barren, desert planet, in a small village far away from civilization.  U grew up here since u were younger, so you know everyone in your village. U decide to look for your friend Joe, who you’ve known your whole life. Where will u look for him?\n A) At his parents' house\n B) At his secret hangout just outside the village  ")
  userInput = ""
  while userInput not in choices:
    print("Options: A/B")
    userInput = input()
    if userInput == "a":
        tekst3()
    elif userInput == "b":
        tekst2()
    else: 
      print("Please enter a valid option.")
def tekst2(): 
  os.system("cls") 
  choices = ["a","b",]
  print("You find your friend Joe relaxing at his hangout; however, he seems... a bit on edge, a bit nervous as well. You ask him what’s going on with him, he shrugs it off by telling you that he just had a bad night's sleep. You let it go and ask him what’s he doing today, however you both hear heavy stomping from a further distance. You see a big, armored vehicle and an army of soldiers heading towards the village, a few moments later u hear explosions and screaming. Joe runs away. What do u do?\n A) Head towards the village and help people\n B) Run with Joe    ")
  userInput = ""
  while userInput not in choices:
    print("Options: A/B")
    userInput = input()
    if userInput == "a":
        tekst4()
    elif userInput == "b":
        tekst6()
    else: 
      print("Please enter a valid option.")
def tekst3():
  os.system("cls") 
  choices = ["a","b",]
  print("U head towards his parents’ house, hoping to see him there. You knock on the door and his dad opens it. You ask him if Joe is here, he answers that he just left a few moments ago. He politely offers if u want something to drink, an offer u can’t refuse of course. You head in and sit down at the table. He asks u how’ve u been doing lately. U wanted to answer, however u both hear heavy stomping. The house is shaking, and people are shouting to get out. You both are going out and you are shocked when you see a big, armored vehicle further on the horizon, you see an army of soldiers heading for the village aswell. The big, armored vehicle shoots at the village and there are many explosions and screaming. Joe’s dad ran off to help other people. What do you do?\n A) Run and escape\n B) B Help people aswell   ")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst5()
    elif userInput == "b":
        tekst4()
    else: 
      print("Please enter a valid option.")
def tekst4():
  os.system("cls") 
  print("You help the people who got wounded, you drag the wounded people inside a house to safety to aid them to their wounds. Yet u do not have the necessary tools to help stop the severe wounds the victims have received from the explosions. You hear a kind of radio chatter outside. You peek outside the window to see a group of tall soldiers in fully black armor. They are looking for survivors to kill off. One trooper spotted you peeking through the window. The group of soldiers quickly enter the house and before u know it you were shot. U have died trying to do right.")
  print("Ending 1")
  quit()
def tekst5():
  os.system("cls") 
  choices = ["a","b",]
  print("You run away fast, trying to avoid blaster fire from the armored vehicle. U made it out of the village and ran past your friends’ hideout. You see footprints in the sand and u follow them, hoping to find Joe, one of your best friends. U see him catching his breath a bit further on. You ask him what’s going on, yet he does not know aswell. He suggests going to the big city, which is very far away, yet u do not have any other options. You accept his suggestion and move on to the city. Once you arrive in the city later in the night, your friend suggests going to a motel and getting some rest. What do you do?\n A) Keep moving \n B) Get rest at a motel")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst17()
    elif userInput == "b":
        tekst7()
    else: 
      print("Please enter a valid option.")
def tekst6():
  os.system("cls") 
  choices = ["a","b",]
  print("You both run away, hoping to not get spotted. U ask your friend what to do next. He suggests going into the city, a big city. It is going to be a very long walk, yet it remains your only option. Once you arrive later that night your friend suggests taking a motel to rest.\n A) Keep moving \n B) Get rest at a motel ")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst17()
    elif userInput == "b":
        tekst7()
    else: 
      print("Please enter a valid option.")      
def tekst7():
  os.system("cls") 
  choices = ["a","b",]
  print("You get rest at a cheap motel. Your room is dirty and stinks. Your friend is in a room next to yours. You are trying to adjust to the city sounds, you have trouble getting used to them. They all sound very weird to you since u have never been outside your village before. You try and get some rest. You wake up early to noise outside the motel, u peek through the window to find a vehicle there with soldiers in it. U wonder if your friend is aware of the noise outside. You hear knocking on the doors. What do you do?\n A)Check on Joe \n B)Escape ")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst8()
    elif userInput == "b":
        tekst10()
    else: 
      print("Please enter a valid option.")
def tekst8():
  os.system("cls") 
  choices = ["a","b",]
  print("U try to contact Joe by knocking on the wall, hoping to hear something back. U hear nothing and decide to check his room by quietly moving to his room. You knock on the door, hoping to get let in fast before you get spotted. While you knock, you notice that the door is already open. U go in and notice that there’s nobody here. You get nervous and you take another peek through the window. You see Joe getting escorted to the vehicle in handcuffs. You wonder why they didn’t get you, and how they knew we would be here. You hear someone shouting that someone went into the captive’s room. What do you do?\n A) You hide \n B) You burst through the back window and run ")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst9()
    elif userInput == "b":
        tekst10()
    else: 
      print("Please enter a valid option.")    
def tekst9():
  os.system("cls") 
  choices = ["a","b",]
  print("You hide under the bed, hoping they won’t find you. 3 soldiers went bursting through the room, now slowly searching the room, looking for you. The back window is closed, says one trooper. He must be around here somewhere. You get stressed as they slowly approach the bed. You see a trooper crouching down, saying “found you”. You take a hit to the face and get knocked out...  You later wake up in the vehicle with Joe sitting opposite to you, with 2 soldiers sitting next to you both. You ask where we are going to be brought too. The trooper says “Haha, you are going to prison mate”. The other trooper laughs while you and Joe look at each other with an uneased expression. A few hours later you arrive at prison, you and Joe get prison clothes and get escorted to your cells. You feel uneasy in an unfamiliar environment like this, people are loud, it’s small and dehumanizing. You feel very uneasy and want to get out. You both get a lunch break and Joe suggests we make up an escape plan./n A) Listen to Joe’s plan/n B) Say we should wait things out  ")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst11()
    elif userInput == "b":
        tekst12()
    else: 
      print("Please enter a valid option.")
def tekst10():
  os.system("cls") 
  choices = ["a","b",]
  print("You sprint through the window and heavily land on the ground. You hear screaming from the soldiers. You get up and try to run away, however the soldiers were too quick for you. You get tackled from behind and go knock out. Eventually u wake up in the vehicle with Joe sitting opposite you, with 2 soldiers sitting next to you both. You ask where we are going to be brought too. The trooper says “Haha, you are going to prison mate”. The other trooper laughs while you and Joe look at each other with an uneasy expression. A few hours later you arrive at prison, you and Joe get prison clothes and are escorted to your cells. You feel uneasy in an unfamiliar environment like this, people are loud, it’s small and dehumanizing. You feel very uneasy and want to get out. You both get a lunch break and Joe suggests we make up an escape plan.\n A)Listen to Joe’s plan \n B)Say we should wait things out ")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst11()
    elif userInput == "b":
        tekst12()
    else: 
      print("Please enter a valid option.")
def tekst11():
  os.system("cls") 
  choices = ["a","b",]
  print("You decide to listen to Joe’s plan, it’s sound rubbish. He suggests we stage a fight, attract the guards and a crowd. Then when the guards are close enough, you try to take them out. And run away quickly with the keys. You have a lot of doubt in this plan, since you both do not have any experience in combat. Joe asks what you think of it\n A) Suggest we wait things out\n B)Execute Joe’s plan ")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst12()
    elif userInput == "b":
        tekst14()
    else: 
      print("Please enter a valid option.") 
def tekst12():
  os.system("cls") 
  choices = ["a","b",]
  print("Joe sighs and says that it is probably our best move, since we are in an unfamiliar environment with no experience of living in a place like this. While waiting things out Joe says he’s going to go to the toilet. You think nothing of it and eat your meal, while eating your meal suddenly the alarm goes off. Everyone is being escorted away, however the exit is now unguarded. Joe is still away. However, this might be your only chance, what do you do?\n A)Try your luck out\n B) Wait for Joe and get in line ")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst15()
    elif userInput == "b":
        tekst13()
    else: 
      print("Please enter a valid option.")
def tekst13():
  os.system("cls") 
  choices = ["a","b",]
  print("You wait for Joe, yet he never comes. You are forced to get in line by a guard. You are escorted to a safe, fireproof zone. You try to look for Joe through the crowd, yet you can’t find him. U worry for him, hoping to see him somewhere. A fight breaks out, and the guards at the exit leave to attend to the fight, one guard unknowingly drops the key. This is probably your last chance to escape. What do you do?\n A)Escape \n B)Stay in line ")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst15()
    elif userInput == "b":
        tekst16()
    else: 
      print("Please enter a valid option.")     
def tekst14():                 
  os.system("cls") 
  choices = ["a","b",]
  print("You and Joe are staging a fight, he keeps pushing and shouting at you. 2 guards0 approach and u nod to Joe to let him know they are coming. Joe turns around and knocks out one guard while you tackle the other guard and knock him out. Joe says to you that he has got the keys. He runs to the exit, and you follow him. Joe unlocks the door and you both go through it. The exit is not the exit what you thought it was, the ‘prison’ u was in was just a part of it. The prison itself is massive, it goes up vertically, and if you look up to the ceiling you can see a bit of sunlight, noticing that you are very much down at the bottom of the prison. You and Joe look at each other speechless. You notice a lift to your right, but there is also one to your left\n A) Left'\n B) Right")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst18()
    elif userInput == "b":
        tekst19()
    else: 
      print("Please enter a valid option.")
def tekst15():                 
  os.system("cls") 
  choices = ["a","b",]
  print("You run towards the exit and snatch the key from the ground which the guard dropped, you go through the door, and you notice you are not done yet. You hear somebody running towards you, it’s Joe.  The prison you were in was a part of a bigger prison. It goes up vertically and is gigantic. U notice there are 2 lifts, one left and one right. Which one do you pick\n A) Left\n B) Right")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst18()
    elif userInput == "b":
        tekst19()
    else: 
      print("Please enter a valid option.")   
def tekst16():                 
  os.system("cls") 
  choices = ["a","b",]
  print("You stay in line, and you get escorted to your cell. Joe never shows up again. A few days later you hear other inmates talking about how the guards shot a prisoner who tried to escape. You ask if they know who it was. They give you a description of the prisoner, which is very familiar to Joe. Joe is dead and you are stuck for eternity in prison, your future will be behind bars")
  print("Prison ending")
def tekst17():                 
  os.system("cls") 
  choices = ["a","b",]
  print("You keep moving and notice a police patrol passing by. It has its flashlights on and passes it on to you and Joe. The police car’s sirens turn on, telling you to put your hands in the air. You are surrounded in a few moments. You and Joe are both detained and put in a police car and escorted to prison. While in prison you get a lunch break, Joe suggests a plan. What do you do\n A)Listen to the plan\n B) Suggest we wait things out ")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst11()
    elif userInput == "b":
        tekst12()
    else: 
      print("Please enter a valid option.")
def tekst18():                 
  os.system("cls") 
  choices = ["a","b",]
  print("You take the left elevator; it closes automatically when you enter. It takes a while before the lift reaches its destination. Once the doors open you notice you are not in the prison anymore, but somewhere else entirely. Joe acts weird and walks a few feet ahead of you. You ask him what’s going on. He looks at you, relieved and stressed at the same time somehow. You get an uneasy feeling from him. He is... fading away.\n A)Run towards him \n B)Keep your distance ")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst20()
    elif userInput == "b":
        tekst21()
    else: 
      print("Please enter a valid option.")
def tekst19():                 
  os.system("cls") 
  choices = ["a","b",]
  print("You and Joe take the right elevator. After a very long wait it reaches its destination. Once the doors open you notice that the environment looks different. A man is standing in front of you. He looks dissatisfied. You were this close he says. Joe walks away and vanishes. The man says you are being tested for the 56th time. He says you have died long ago, and your brain has been copied to the cloud for immortality. All the things you have experienced where to test if you are aware and sharp enough for the life beyond death. Yet your last choice was a mistake, as you will no longer be allowed to go beyond. He says it is a shame, yet he must delete your online version of yourself for the safety of the people who made it to the beyond. You lose your feelings slowly and you see yourself fading away. All the effort you made... It was almost worth it.")
  print("Bad ending")
  quit()
def tekst20():                 
  os.system("cls") 
  choices = ["a","b",]
  print("As you run towards him it is already too late, he seems to have vanished into nothingness. You hear a man talking behind you. “You made it he” says, “you have completed the test to go to beyond death”.  “It took you a while, but you made it”. “Everything that has happened here was a simulation, you, in fact have died a long time ago. “Then we made an engram from your brain and well, we’ve tested it until you were ready for live beyond death" "I am sorry about your friend, but I did what I had to do”. He opens a portal, “Are you ready” he says. You are fuming with rage after what happened to your friend, you want to attack him. What do you do?\n A) Attack him\n B) Go into the portal")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst23()
    elif userInput == "b":
        tekst22()
    else: 
      print("Please enter a valid option.")
def tekst21():                 
  os.system("cls") 
  choices = ["a","b",]
  print("As you keep your distance, your friend fades away very fast. He is nowhere to be seen. You hear a man talking behind you. “You made it he” says, “you have completed the test to go to beyond death”.  “It took you a while, but you made it”. “Everything that has happened here was a simulation, you, in fact have died a long time ago, lucky for you were rich. “So, then we made an engram from your brain and well, we’ve tested it until you were ready for life beyond death" "I am sorry about your friend, but I did what I had to do”. He opens a portal, “Are you ready” he says. You are fuming with rage after what happened to your friend, you want to attack him. What do you do?\n A) Attack him\n B) Go into the portal")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst23()
    elif userInput == "b":
        tekst22()
    else: 
      print("Please enter a valid option.")
def tekst22():                 
  os.system("cls") 
  choices = ["a","b",]
  print("While fuming with rage, you head toward the portal and enter it. All you can see is white, and then suddenly you can see it again. You are in a beautiful place, full of life and people. Your rage about Joe slowly disappears, as you’ve just entered a new part of your life, a new start. The man pops out of nowhere in front of you, telling you what you can do and what opportunities there are. He reassures you that things will become okay, better. Your new life has just begun.")
  print("Good ending")
  quit()   
def tekst23():                 
  os.system("cls") 
  choices = ["a","b",]
  print("You rush towards the man, trying to throw a punch, he dodges with ease. “Oh, you want to fight”? Two swords drop out of nowhere. “Let's do this then" "I will do what I must” you say.  You are fuming with rage, yet you cannot even scratch the man. He just stands there, yet you are already exhausted. “Give up and I shall give you another chance to enter the next part of your life. He opens the portal, “Are you ready?”\n A) Give up and enter the portal \n B) Continue fighting ")
  userInput = ""
  while userInput not in choices:
    print("Options: a/b")
    userInput = input()
    if userInput == "a":
        tekst22()
    elif userInput == "b":
        tekst24()
    else: 
      print("Please enter a valid option.")
def tekst24():                 
  os.system("cls") 
  print("You continue fighting, it seems like a wasted effort. The man says he’s disappointed in you and stabs you right in the stomach. “All that effort, yet u cannot contain your emotions. What a waste”. The man walks away, and your vision turns to black. The fight is done, yet you did not win.")
  print("Bad ending")
  quit()   
tutorial()
start()                                                  

     

       

