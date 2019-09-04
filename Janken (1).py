import random

def judge(player,computer):
	if player == computer:
		print("あいこです")
	elif (player ==0 and computer ==1 ) or (player ==1 and computer ==2 ) or (player==2 and computer ==0 ):
		print("コンピューターの勝ちです")
	else:
		print("あなたの勝ちです")

yourhandmark = int(input('出す手を入力してください 0:パー、1:チョキ、2:グー '))
while yourhandmark != 0 and yourhandmark != 1 and yourhandmark != 2:
	yourhandmark = int(input('もう一度入力してください'))

computerhandmark = random.randrange(3)

handmark = ["パー","チョキ","グー"]
print("あなたが出した手は"+handmark[yourhandmark]+"です")
print("コンピューターが出した手は"+handmark[computerhandmark]+"です")
judge( yourhandmark,computerhandmark )