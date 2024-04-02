print("You wake up in a forest with no recollection of how you got there.")
print("All you know is- you want to go home!")
option1 = input("You see a village in the distance, but a sudden chill makes you shiver. You realise you're butt-naked! Do you want to find some clothes first or go straight to the village? (Clothes/Village)")
while True:
    if option1.lower() == "clothes":
        print("You didn't manage to find clothes since you're in the wild. But hey, at least you found some big leaves to make do!")
        print("Now you carefully make your way to the village. Once near, you see a man walking about and calls out to him.")
        print("For whatever reason, the man speaks English(thankfully!). He welcomes you to the village and get you all introduced. You're practically a celebrity now!")
        option2 = input("You ask the man how to get home, and the man explains that you have been kidnapped by the evil dragon to this world. You have to defeat the evil dragon in order to go home. You're not sure whether fighting a dragon is a good idea... Do you want to take up the quest to slay the evil so you can get home?(Yes/No)")
        if option2.lower() == "yes":
            option3 = input("Horray! You set off on the journey to the dragon's lair. Before that though, you have to pick a weapon. Do you want to pick the sword or the bow?(Sword/Bow)")
            if option3.lower() == "sword":
                print("You travel for many months and finally find the dragon. Whilst the dragon is sleeping, you creep up to it and slay its head! Then you got teleported back home! Congratulations! You beat the game!")
                break
            elif option3.lower() == "bow":
                print("You travel for many months and finally find the dragon. Whilst the dragon is sleeping, you draw your bow and aim for its head. Whoosh! The arrow hits dead-center... but it bounces off the dragon's hard scales. The dragon wakes up angrily and eats you. Game over!")
                break
            else:
                option3 = input("Not a valid answer! Sword or Bow!")
        elif option2.lower() == "no":
            print("Of course you're not going to try and fight a dragon! That'd be ludicrous!")
            print("You politely decline the quest. You've given up hope on going home now so you plan to just live in the village.")
            print("Though apparently, God didn't like that choice so the next day you got struck by lightning and died. Game over!(The world is a cruel place to cowards...)")
            break
        else:
            option2 = input("Not a valid answer! Yes or No!")
    elif option1.lower() == "village":
        print("You trudge up to the village. Suddenly, a man pops out of nowhere and is so startled to see you naked, he accidently shoots you with a bow! Game over!")
        break
    else:
        option1 = input("Not a valid answer! Clothes or Village!")