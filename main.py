import turtle
import pandas

screen = turtle.Screen()
screen.title("INDIA State Game")
image = "india state.gif"
screen.setup(500, 400)
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("state_data.csv")
all_state = data.state.to_list()
guess_state = []

while len(guess_state) < 31:
    ans_state = screen.textinput(title=f"{len(guess_state)}/30 State correct",
                                 prompt="What's another state's name ").title()
    # TODO : use comprehension
    if ans_state == "Exit":
        missing_states = [state for state in all_state if state not in guess_state ]
    # if ans_state == "Exit":
    #     missing_states = []
    #     for state in all_state:
    #         if state not in guess_state:
    #             missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_learn.csv")
        break

    if ans_state in all_state:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

# #(down)this for mark and click , give x , y axis in click
# def det_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(det_mouse_click_coor)
# turtle.mainloop()


################
# state to learn csv