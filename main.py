import turtle
import pandas
import time


screen = turtle.Screen()
screen.bgpic('blank_states_img.gif')

data = pandas.read_csv('50_states.csv')


state_search = screen.textinput('States', 'does april stink?').lower().capitalize()

search = (data[data['state'] == state_search])

print(search.state.tolist()[0])

def add_state(state,x,y):
    state_label = turtle.Turtle()
    state_label.penup()
    state_label.hideturtle()
    state_label.goto(int(x), int(y))
    state_label.write(state, align='center', font=('courier', 8, 'normal'))


add_state(search.state.tolist()[0], search.x, search.y)

turtle.exitonclick()