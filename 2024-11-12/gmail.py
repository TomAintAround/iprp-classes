import turtle

def rect(ladoMaior, ladoMenor, angulo):
	for _ in range(2):
		turtle.forward(ladoMaior)
		turtle.right(90 * angulo)
		turtle.forward(ladoMenor)
		turtle.right(90 * angulo)
	
def mover(x, y):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()

def gmailLogo():
	headings = [180, 270, 45, 45]
	positions = [(102, 100), (5, 100), (-2, 0), (100, 0)]
	colors = ['orange', 'green', 'blue', 'red']
	for i in range(len(headings)):
		turtle.setheading(headings[i])
		mover(positions[i][0], positions[i][1])
		turtle.left(45)
		turtle.color(colors[i])
		turtle.begin_fill()
		if i == 0:
			rect(100, 10, -1)
		else:
			rect(100, 10, 1)
		turtle.end_fill()

if __name__ == "__main__":
	gmailLogo()