import pandas
import turtle
from playsound import playsound



#set the screen
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


#read the csv using pandas and create list that containing all the states
data = pandas.read_csv("50_states.csv")
state_names = data["state"].to_list()

#function that return the location of state in the map
def location(x,y):
    state = turtle.Turtle()
    state.penup()
    state.hideturtle()
    state.goto(x,y)
    return state

#list for store correctly guessed states
guessed_states = []

#loop that execute until  user guess all the states
#check the correctness and track the points
while len(guessed_states)<50:
    answer = turtle.textinput(f"{len(guessed_states)}/50 States correct", "What's the name of the state?").title()

    #if user enter exit, create a csv file that contain the missing states
    if  answer == "Exit":
        missing_states=[]
        for i in state_names:
            if i not in guessed_states:
                missing_states.append(i)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for i in state_names:
        if answer == i:
            row = data[data.state == i].iloc[0]
            x_cor = row.x
            y_cor = row.y
            correct_state = location(x_cor, y_cor)
            correct_state.write(i,align="center", font=("Arial", 10, "bold"))
            guessed_states.append(i)
            playsound("sounds/correct.mp3")

    if answer not in state_names:
        playsound("sounds/wronganswer.mp3")

screen.mainloop()



