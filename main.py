import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pd.read_csv("50_states.csv")
countries = data.state.to_list()

t = turtle.Turtle()
t.penup()
t.hideturtle()

guess_state = []
scor = 0

while len(guess_state) < 50:
    answer = screen.textinput(title=f"{scor}/50. Guess the state", prompt="Write a state:").title()

    if answer == "Exit":
        break

    if answer in countries:
        scor += 1
        country_row = data[data["state"] == answer]
        t.goto(int(country_row.x), int(country_row.y))
        t.write(answer)
        guess_state.append(answer)
    else:
        pass

t.goto(0, 0)
t.write(f"You have made {len(guess_state)} out of 50!", align = "center", font = ("courier", 20, "normal"))
turtle.time.sleep(1)

countries_to_learn = []

# for country in countries:
#     if country not in guess_state:
#         countries_to_learn.append(country)
countries_to_learn = [country for country in countries if country not in guess_state]

df = pd.DataFrame(countries_to_learn)

# Write the DataFrame to a CSV file
df = df.reset_index(drop=True)
df.index += 1
df.to_csv('countries_to_learn.csv', index=True, header=False)



turtle.mainloop()