import turtle
import pandas

guessed_states = []
states = []

text = turtle.Turtle()
text.penup()
text.speed('fastest')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
for state in data.state:  # 2 way of the code on the left
    states.append(state)  # states = data.state.to_list()

data_dict = data.to_dict()

while len(guessed_states) != 50:
    text.home()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                             "name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        list_of_missed_states = [state for state in states if state not in guessed_states]
        final_data = pandas.DataFrame(list_of_missed_states)
        final_data.to_csv("states_to_learn.csv")
        break

    if answer_state.title() in states:
        if answer_state.title() in guessed_states:
            pass
        else:
            guessed_states.append(answer_state)
            guessed_data = data[data.state == answer_state]  # 2 way: guessed_data = data[data.state == answer_data]
            x = guessed_data.x  # text.goto(int(guessed_data.x), int(guessed_data.y))
            y = guessed_data.y
            x = int(x)
            y = int(y)
            text.goto(x, y)
            text.write(f"{answer_state}", align='center')  # 2 way: text.write(answer_state)
            # or     text.write(guessed_data.state.item())

screen.exitonclick()

