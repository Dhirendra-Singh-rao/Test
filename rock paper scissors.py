player1=input("player1 ")
player2=input("player2 ")
if player1=="rock"and player2=="scissor":
	print("player1 is winner")
elif player1=="paper"and player2=="scissor":
	print("player2 is winner")
elif player1=="scissor"and player2=="rock":
	print("player2 is winner")
elif player1=="scissor"and player2=="paper":
	print("player1 is winner")
elif player1=="rock"and player2=="paper":
	print("player2 is winner")
elif player1=="paper"and player2=="rock":
	print("player1 is winner")	
elif player1=="rock"and player2=="rock":
	print("match is tie")
elif player1=="paper"and player2=="paper":
	print("match is tie")
elif player1=="scissor"and player2=="scissor":
	print("match is tie")
else:
	print("syntax error")