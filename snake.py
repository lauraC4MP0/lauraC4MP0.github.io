import turtle
import time
import random
#from playsound import playsound
import winsound
from tkinter import messagebox

postpone=0.1
score=0
high_score=0

wn=turtle.Screen()
wn.title("SNAKE")
wn.bgcolor("#f55e64")
wn.setup(width=600, height=600)
wn.tracer(False)

head=turtle.Turtle()
head.speed(False)
head.shape("square")
head.penup()
head.goto(0,0)
head.direction="stop"
head.color("#68f55e")

food=turtle.Turtle()
food.speed(False)
food.shape("circle")
food.penup()
food.goto(150,30)
food.color("#fff34a")

"""def sound():
	winsound.PlaySound(r"E:\PYTHON\turtle\CRMN.mp3", winsound.SND_ASYNC)
	s=playsound(r"E:\PYTHON\turtle\CRMN.mp3")"""
'''
def image():
	k=turtle.Screen()
	khloe=turtle.Turtle()
	photo=r"E:\PYTHON\turtle\20200717_112331.gif"
	k.addshape(photo)
	khloe.shape(photo)
	khloe=turtle.Screen()
	khloe.bgpic(r"E:\PYTHON\turtle\WhatsApp Image 2020-08-16 at 7.46.04 PM.gif")
	khloe.setup(width=600,height=600)
	time.sleep(0)'''
khloe=turtle.Screen()

seg=[]

text=turtle.Turtle()
text.speed(False)
text.penup()
text.hideturtle()
text.goto(0,200)
text.color("#0c1e53")
text.write("SCORE: "+str(score)+"\nHIGH SCORE: "+str(high_score), align="center", font=("verdana", 24, "bold"))

def move():
	if head.direction=="up":
		y=head.ycor()
		head.sety(y+20)
	if head.direction=="down":
		y=head.ycor()
		head.sety(y-20)
	if head.direction=="left":
		x=head.xcor()
		head.setx(x-20)
	if head.direction=="right":
		x=head.xcor()
		head.setx(x+20)

def up():
	head.direction="up"

def down():
	head.direction="down"

def right():
	head.direction="right"

def left():
	head.direction="left"

wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

while True:
	wn.update()

	if head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-280:
		time.sleep(0)
		head.goto(0,0)
		head.direction="stop"
		high_score=high_score
		text.clear()
		text.write("SCORE: "+str(score)+"\nHIGH SCORE: "+str(high_score), align="center", font=("verdana", 24, "bold"))
		postpone=0.1
		if score>1000:
			messagebox.showwarning("LOSER", "You're a loser and khloé is the best.\n\nAtt Khloe xoxo")
		score=0
		khloe.clear()
		wn=turtle.Screen()
		wn.title("SNAKE")
		wn.bgcolor("#f55e64")
		wn.setup(width=600, height=600)
		wn.tracer(False)

		head=turtle.Turtle()
		head.speed(False)
		head.shape("square")
		head.penup()
		head.goto(0,0)
		head.direction="stop"
		head.color("#68f55e")

		food=turtle.Turtle()
		food.speed(False)
		food.shape("circle")
		food.penup()
		food.goto(150,30)
		food.color("#fff34a")

		seg=[]

		text=turtle.Turtle()
		text.speed(False)
		text.penup()
		text.hideturtle()
		text.goto(0,200)
		text.color("#0c1e53")
		text.write("SCORE: "+str(score)+"\nHIGH SCORE: "+str(high_score), align="center", font=("verdana", 24, "bold"))

		def move():
			if head.direction=="up":
				y=head.ycor()
				head.sety(y+20)
			if head.direction=="down":
				y=head.ycor()
				head.sety(y-20)
			if head.direction=="left":
				x=head.xcor()
				head.setx(x-20)
			if head.direction=="right":
				x=head.xcor()
				head.setx(x+20)

		def up():
			head.direction="up"

		def down():
			head.direction="down"

		def right():
			head.direction="right"

		def left():
			head.direction="left"

		wn.listen()
		wn.onkeypress(up, "Up")
		wn.onkeypress(down, "Down")
		wn.onkeypress(left, "Left")
		wn.onkeypress(right, "Right")



		for i in seg:
			i.goto(1000,10000)
		seg.clear()

	if head.distance(food)<20:
		#sound()
		x=random.randint(-280,280)
		y=random.randint(-280,280)
		food.goto(x,y)
		new=turtle.Turtle()
		new.speed(0)
		new.shape("square")
		new.penup()
		new.goto(0,0)
		new.color("#68f55e")
		seg.append(new)

		score+=20

		if score>high_score:
			high_score=score
			if head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-280:
				score=0
			else:
				score=score

		if score>=500:
			postpone=0.050
			textk=turtle.Turtle()
			textk.speed(0)
			textk.hideturtle()
			textk.goto(0,0)
			textk.color("#f92929")
			#textk.write("Khloé is the best, \nit's a fact bitch. xoxo", align="center", font=("helvetica", 30, "bold"))
			#khloe.bgpic(r"C:\Users\Laura Campo\Documents\0\snake\WhatsApp Image 2020-08-16 at 7.46.04 PM.gif")
		elif score>=1000:
			postpone=0

		text.clear()

		text.write("SCORE: "+str(score)+"\nHIGH SCORE: "+str(high_score), align="center", font=("verdana", 24, "bold"))

	total=len(seg)
	for index in range(total -1,0,-1):
		x=seg[index-1].xcor()
		y=seg[index-1].ycor()
		seg[index].goto(x,y)
	if total>0:
		x=head.xcor()
		y=head.ycor()
		seg[0].goto(x,y)
	move()

	for i in seg:
		if i.distance(head)<20:
			head.goto(0,0)
			head.direction="stop"
			text.clear()
			text.write("SCORE: "+str(score)+"\nHIGH SCORE: "+str(high_score), align="center", font=("verdana", 24, "bold"))
			postpone=0.1
			if score>1000:
				messagebox-showwarning("LOOSER", "Everybody loves Khloé <3")
			score=0
			khloe.clear()
			wn=turtle.Screen()
			wn.title("SNAKE")
			wn.bgcolor("#f55e64")
			wn.setup(width=600, height=600)
			wn.tracer(False)

			head=turtle.Turtle()
			head.speed(False)
			head.shape("square")
			head.penup()
			head.goto(0,0)
			head.direction="stop"
			head.color("#68f55e")

			food=turtle.Turtle()
			food.speed(False)
			food.shape("circle")
			food.penup()
			food.goto(150,30)
			food.color("#fff34a")

			seg=[]

			text=turtle.Turtle()
			text.speed(False)
			text.penup()
			text.hideturtle()
			text.goto(0,200)
			text.color("#0c1e53")
			text.write("SCORE: "+str(score)+"\nHIGH SCORE: "+str(high_score), align="center", font=("verdana", 24, "bold"))

			def move():
				if head.direction=="up":
					y=head.ycor()
					head.sety(y+20)
				if head.direction=="down":
					y=head.ycor()
					head.sety(y-20)
				if head.direction=="left":
					x=head.xcor()
					head.setx(x-20)
				if head.direction=="right":
					x=head.xcor()
					head.setx(x+20)

			def up():
				head.direction="up"

			def down():
				head.direction="down"

			def right():
				head.direction="right"

			def left():
				head.direction="left"

			wn.listen()
			wn.onkeypress(up, "Up")
			wn.onkeypress(down, "Down")
			wn.onkeypress(left, "Left")
			wn.onkeypress(right, "Right")


			for i in seg:
				i.goto(9000,8000)
			seg.clear()
	time.sleep(postpone)

turtle.getscreen()._root.mainloop()