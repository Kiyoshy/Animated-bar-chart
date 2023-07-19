from sjvisualizer import DataHandler, Canvas, BarRace, StaticImage
import json

EXCEL_FILE = "data/avocado.xlsx"
FPS = 25
DURATION = 0.6

# Reading colors
with open("colors.json") as f:
	colors = json.load(f)

# load the data into a data frame
df = DataHandler.DataHandler(excel_file=EXCEL_FILE, number_of_frames=FPS*DURATION*90).df

# creatig the canvas animation
canvas = Canvas.canvas()

# adding decoration with TkInter
line = canvas.canvas.create_line(585, 30, 585, 140, width=8, fill=Canvas._from_rgb((75, 75, 155)))
tons = canvas.canvas.create_text(1050, 960, text="Tons of avocado", font=("Arial", 18), fill=Canvas._from_rgb((120,120,120)))
source = canvas.canvas.create_text(1600, 1050, text="Source: Food and Agriculture Organization of the UN (FAO)", font=("Arial", 14), fill=Canvas._from_rgb((120,120,120)))

# adding the racing bar chart
bar_chart = BarRace.bar_race(df=df, canvas=canvas.canvas, colors=colors, width=1400, height=700 , x_pos=250)
canvas.add_sub_plot(bar_chart)

# adding a title
canvas.add_title("Worldwide Avocado Production", color=(0,0,0))
canvas.add_sub_title("From 1961 - 2020", color=(150,150,150))

# adding a time
canvas.add_time(df=df, time_indicator="year")

# adding a static image
img = StaticImage.static_image(canvas=canvas.canvas, file="avocado.png", x_pos=470, y_pos=20, width=125, height=125)
canvas.add_sub_plot(img)

# adding a logo
# canvas.add_logo(logo="logo.png")

# play the animation
canvas.play(fps=FPS)