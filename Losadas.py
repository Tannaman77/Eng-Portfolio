import random

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm,', 'n', 'o', 'p', 'q', 'r', 's','t', 'u','v','w', 'x','y','z']
point1 = 0
point2 = 0
player1 = str(input("Whats your name player 1? "))
player2 = str(input("whats your name player 2? "))
amount = int(input("How many point you want to go to? "))


while amount <= 1000:

	word = char[random.randint(0,25)]
	pic = input("Pic a word {} ".format(player1))
	if word in pic:
		point1 += 1
		print("Its here")
		print(point1)
	
	else:
		print("Not here")
		
	pic2 = input("Pic a word {} ".format(player2))
	if word in pic2:
		point2 += 1
		print("Its here")
		print(point2)
	else:
		print("Not here")
	print("The word was {}".format(word))
	if point1 or point2 == amount:
		amount = 1001
	
print("Good Game!")
