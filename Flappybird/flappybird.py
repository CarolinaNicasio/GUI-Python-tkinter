from PIL import Image, ImageTk
import tkinter as tk 
from pygame import mixer 
import random

mixer.init() 
window = tk.Tk()
window.geometry('1100x700')
window.title('Flappy Bird')

#Background (Fondo)
canvas = tk.Canvas(window, highlightthickness=0, bg= '#78ECF8')
canvas.place(relwidth = 1, relheight=1)

#Images 

img_blue_bird = Image.open('images/bird.png')
img_blue_bird = ImageTk.PhotoImage(img_blue_bird)

img_tube_down = Image.open('images/pipe.png')           
img_tube_top = img_tube_down.rotate(180)

img_tube_down = ImageTk.PhotoImage(img_tube_down)
img_tube_top = ImageTk.PhotoImage(img_tube_top)

img_gameover = Image.open('images/gameover.png')
img_gameover = ImageTk.PhotoImage(img_gameover)

#Score text (Texto del puntaje)

scoreText = canvas.create_text(50,50, text= '0', fill='white', font=('Impact', 40))


x = 200
y = 350
score = 0
speed = 15
game_over = False

bluebird = canvas.create_image(x,y, anchor = 'nw', image =img_blue_bird)
tube_top = canvas.create_image(1300, -650, anchor= 'nw', image = img_tube_top)
tube_down = canvas.create_image(1300, 650, anchor= 'nw', image = img_tube_down)


#Motion bird (movimiento)

def move_bird_key(event):
	global x,y
	if not game_over:
		y -=35
		canvas.coords(bluebird, x,y)
		mixer.music.load('audio/flap.mp3')
		mixer.music.play(loops= 0)


window.bind( "<space>", move_bird_key)


def move_bird():
	global x,y
	y +=4
	canvas.coords(bluebird, x,y)
	if y<0 or y> window.winfo_height():
		game_end()

	if not game_over:
		window.after(50, move_bird)
		
#Move tube

def move_tube():
	global score, game_over, speed
	canvas.move(tube_top, -speed, 0)
	canvas.move(tube_down, -speed, 0)
	if canvas.coords(tube_down)[0] < -100:
		score += 1
		speed += 1
		canvas.itemconfigure(scoreText, text = str(score))
		h = window.winfo_height()
		num = random.choice([i for i in range(160,h, 160)])
		canvas.coords(tube_down, window.winfo_width(), num+160)
		canvas.coords(tube_top, window.winfo_width(), num-900)

	if 0 < canvas.coords(tube_down)[0]<160:
		channel = mixer.Channel(1)
		channel.set_volume(1.0)
		sound = mixer.Sound('audio/point.mp3')
		channel.play(sound, loops= 0)

	if canvas.coords(tube_down):
		if canvas.bbox(bluebird)[0] < canvas.bbox(tube_down)[2] and canvas.bbox(bluebird)[2]> canvas.bbox(tube_down)[0]:
			if canvas.bbox(bluebird)[1] < canvas.bbox(tube_top)[3] or canvas.bbox(bluebird)[3]> canvas.bbox(tube_down)[1]:
				game_end()
	if  not game_over:
		window.after(50, move_tube)

#Reset (Reiniciar juego)
def reset_game():
	global x,y,score, speed, game_over
	x = 150
	y = 300
	score = 0
	speed = 10
	game_over = False
	canvas.coords(bluebird, x,y)
	canvas.coords(tube_top, 1200,-550)
	canvas.coords(tube_down, 1200, 550)
	canvas.itemconfigure(scoreText, text ="0")
	btReset.place_forget()
	move_bird()
	move_tube()

	mixer.music.load('audio/sound.mp3')
	mixer.music.play(loops= 0)

def game_end():
	global game_over
	game_over = True
	btReset.place(relx = 0.5, rely = 0.7, anchor ='center')
	mixer.music.load('audio/hit.mp3')
	mixer.music.play(loops= 0)
	while mixer.music.get_busy():
		continue
	mixer.music.load('audio/die.mp3')
	mixer.music.play(loops= 0)

btReset = tk.Button(window, border = 0, image= img_gameover, activebackground='#78ECF8', bg= '#78ECF8', command = reset_game)

window.after(50, move_bird)
window.after(50, move_tube)

#IconPhoto(imagen de icono)

window.call('wm', 'iconphoto', window._w, img_blue_bird) 

window.mainloop()

