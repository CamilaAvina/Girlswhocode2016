start = '''
You are at a party that you were invited too by a friend and it was going to be held in a stranger's house. 
Your friend told you that the party was going to be funso you decided to go.
When you arrived at the house the party was at,when you entered you get this strange cold feeling but, you thought it was nothing so yor go to the living room. 
when you are in the living room you see a sign on the wall that says if you don't leave before midnight you will be stuck here forever.
So you looked at the time and it is ten at night so you have around two hours to leave so, you decide to think for a solution. 
Then you try to get out but there is only one way to reach the door but the hallway splits and you can only go left or right but there is a someone blocking the way for both sides. 
'''


print(start)
done = False 
while not done:
	user_input = input("Type 'left' to go left or 'right' to go right")
	if user_input == "left":
		print("left side")
		print("comman point")
		done = True
	elif user_input == "right":
		print("right side")
		print("comman point")
		done = True
	else:
		print("please type 'left' or 'right'")
print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
	print("You decide to go left and there is a man standing there with a saw looking at you very angry yelling to you to go away.")  
	done = True
	print("Type 'attack' to go towards him or 'hide' to not be seen.")
	user_input = input()
	if user_input == "attack":
		print("You chose to attack him and you are fighting him but he is too strong and has a saw so he decides to use it.You try to attack somehow but he is very stong so he ends up killing you.")
		done = True
	elif user_input == "hide":
		print("you chose to hide and you are in a dark room and the man with the saw looked at were you went, you locked the door but he has a saw so he was able to open the door and he came into the room and cornerd you which he ended up killing you.")
		done = True 
elif user_input == "right":
	print("You choose to go right and there is another man who has a knife and looks very tired but bothered.")
	done = True
	print("type 'talk' to talk to man with knife or 'takes' to take you somewhere safe.")
	user_input = input() 
	if user_input == "talk":
		print("You chose to talk to him and he will understand the situation because he has been facing this problem since he came to a party that happened a long time ago.Also he will help you leave because that is his only way out because you are someone new; you end up safe and survive the escape from the house.")
		done = True
	elif user_input == "takes":
		print("You chose for him to take you somewhere safe and you don't survive because he did was not able to help you because you were a stranger to him so he thought you were a threat.")
		done = True
		
		