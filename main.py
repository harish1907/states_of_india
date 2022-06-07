from turtle import *
import pandas

screen = Screen()
image = "india.gif"
screen.addshape(image)
screen.setup(800, 800)
tim = Turtle()
tim.shape(image)
data = pandas.read_csv("states.csv")
score = []


while len(score) < 29:
    user = textinput(title="India States guess", prompt=f"{len(score)}/{len(data.states.to_list())} What is you next "
                                                        f"guess?").title()
    if user == "Exit":
        missing = [i for i in data.states.to_list() if i not in score]
        learning = pandas.DataFrame(missing)
        learning.to_csv('learn_it.csv')
        break

    if user in data.states.to_list() and user not in score:
        answer_data = data[data.states == user]
        answer = Turtle()
        answer.penup()
        answer.hideturtle()
        answer.color('blue')
        answer.goto(int(answer_data.x), int(answer_data.y))
        answer.write(user, font=('arial', 10, 'bold'))
        score.append(user)

screen.exitonclick()
