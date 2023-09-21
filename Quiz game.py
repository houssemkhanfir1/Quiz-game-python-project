#Quiz game
import random
def hello(name):
	print("hello"+" "+name)
quiz={'A':'A1','B':'A2','C':'A3','D':'A4'}
question=quiz.keys()
answer=quiz.values()
question1=list(question)
answer1=list(answer)
def game(score):
	name=input("what is u name??: ")
	hello(name)
	for i in range(len(question1)-2):
		q=question1[i]
		print(q)
		x=input("what is u answer???").upper()
		if x in answer1 and x==answer1[i]:
			score=score+10
		print("next question")
	for i in range(len(question1)-2,len(question1)-1):
		q=question1[i]
		print(q)
		x=input("what is u answer???").upper()
		print("next quetsion")
		if x in answer1 and x==answer1[i]:
			score=score+10
	print(question1[len(question1)-1])
	x=input("what is u answer???").upper()
	if x in answer1 and x==answer1[len(question1)-1]:
		score=score+10
	print("checking results..")
	return score
while True:
	score=0
	score=game(score)
	print("your score is : ",score)
	if score==(len(answer1)*10):
		print("you are brillant")
	elif score>=((len(answer1*10))/2):
		print("not bad")
	elif score<((len(answer1*10))/2):
		print("you suck")
	t=input("would you want to try again??(y/n)")
	if t=="n":
		break		

	
	

