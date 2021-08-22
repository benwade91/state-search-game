import turtle
import pandas


screen = turtle.Screen()
screen.bgpic('blank_states_img.gif')
screen.setup(width=800, height=500)
data = pandas.read_csv('50_states.csv')

state_list = data.state.tolist()

def add_state(state,x,y):
    state_label = turtle.Turtle()
    state_label.penup()
    state_label.hideturtle()
    state_label.goto(int(x), int(y))
    state_label.write(state, align='center', font=('courier', 8, 'normal'))


game_on = True

while game_on:
    state_name = screen.textinput('States', 'enter the name of a state?').title()

    if state_name in data.values:
        search = (data[data['state'] == state_name])
        add_state(search.state.tolist()[0], search.x, search.y)
        if state_name in state_list:
            state_list.remove(state_name)
    elif state_name == 'Exit':
        break


states_dict = {
    'State Name': state_list
}

states_dataframe = pandas.DataFrame(states_dict)
states_dataframe.to_csv('states_to_study.csv')

turtle.exitonclick()