import turtle
import pandas


screen = turtle.Screen()
screen.bgpic('blank_states_img.gif')

data = pandas.read_csv('50_states.csv')

state_list = data.state.tolist()
print(state_list)

def add_state(state,x,y):
    state_label = turtle.Turtle()
    state_label.penup()
    state_label.hideturtle()
    state_label.goto(int(x), int(y))
    state_label.write(state, align='center', font=('courier', 8, 'normal'))


game_on = True

while game_on:
    state_search = screen.textinput('States', 'enter the name of a state?').lower().title()
    if state_search in data.values:
        search = (data[data['state'] == state_search])
        add_state(search.state.tolist()[0], search.x, search.y)
        state_list.remove(state_search)
        print(state_list)

turtle.exitonclick()