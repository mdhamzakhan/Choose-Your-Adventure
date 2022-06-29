def start():
        print('''Game Instructions: Press 1 or 2 to choose your adventure, if at any point you want to exit press any other number the story - you went for camping with your friends at a nearby hill-station, in evening alone went to collect firewood while getting back you lost your track''')
        print('''now, you have two options 1) to continue on the track  2) to wait at this spot for help''')
        Choice_1 = int(input("press 1 0r 2 to make your choice "))
        if Choice_1 ==1 :
            print('''you continued on the track, after walking for like more than an hour, you still havent find your way, as the sun sets, it is getting more darker, you have started to feel hungry and tired''')
            choice_2 = int(input('''**make a choice** 1 = continue looking for a track, 2 = lit a fire and spend the night here and start again in the morning '''))
            if choice_2 == 1:
                print(''' you decided to move ahead, the woods are getting more darker and deeper, your mental and physical health is getting drained with each passing second, suddenly you hear some voices, you have heard from people that the camping site also have some wild animals which can be dangerous, but looking positively it can also be your friends looking for you''')
                choice_3 = int(input('''now choose, very carefully will you- 1) go and check who is making the noise or 2)  start moving in the opposite direction, enter your choice '''))
                if choice_3 == 1:
                    print('''you decided to go ahead and check, and there they were...your friends with a local policemen, you are saved! Congrats ''')
                elif choice_3 == 2:
                    print(''' you decided to move away in opposite direction, after going ahead for 200m, you have reached a dead end...you have no other choice now except to go again in the other direction after 5 mins suddenly you hear your friend's voice coming from that direction, luckily you are saved! Congrats ''')
                else:
                    print("invalid choice")
            elif choice_2 == 2:
                print(''' you decided to sit down, lit the fire and waited for morning, suddenly around 2 AM, you started to feel something moving in your sorrounding, when you around, you found a snake udner your nearby tree''')
                choice_3 = int(input('''make your choice,1 = will you try to kill the snake if its move in your direction or 2 =will you wait and let him go  '''))
                if choice_3 ==1:
                    print('''you tried to hit the snake, but it bite you first.... and then it moved away, you are now feeling ill suddenly, you start panicking and started shouting, luckily the friends were looking out for and heared your voice and come to your rescue, you are admitted to the hospital but you are safe ''')
                elif choice_3 == 2:
                    print(''' you decided to let the snake go peacefully, after one hour, you you heard your friends's voives calling for you and they come to your rescue''')
                else:
                    print("invalid choice")
                    
        elif Choice_1 ==2:
            print('''you decided to stay at your own place and await help, suddenly around 2 AM, you started to feel something moving in your sorrounding when you around, you found a snake udner your nearby tree''') 
            choice_2 = int(input('''make your choice,1 = will you try to kill the snake if its move in your direction or 2 =will you wait and let him go''' ))
            if choice_2 ==1:
                    print('''you tried to hit the snake, but it bite you first.... and then it moved away, you are now feeling ill suddenly, you start panicking and started shouting, luckily the friends were looking out for and heared your voice and come to your rescue, you are admitted to the hospital but you are safe ''')
            elif choice_2 == 2:
                    print(''' you decided to let the snake go peacefully, after one hour, you you heard your friends's voives calling for you and they come to your rescue''')
            else:
                print("invalid choice")
                
        else:
            print("invalid choice")
            


print("Welcome to your adventure")


to_start = input("press s to start, to quit press any other button\n")
if to_start.lower() == 's':
    start()
    print("Thankyou for playing")
        
else:
    print("thankyou, you have exited the program successfully") 

