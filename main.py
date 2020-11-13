from tkinter import *
import pygame
from tkinter import filedialog
root=Tk()
root.title("")
root.geometry("1000x350")

pygame.mixer.init()

def add_song():
    song = filedialog.askopenfilename(initialdir="songs", title="Choose a Song", filetypes=(("wav Files","*.wav"),))
    song = song.replace("/home/user/Documents/python_exercises/audio_player/songs/", "")
    song = song.replace(".wav", "")
    lst_box.insert(END, song)

def play():
    song = lst_box.get(ACTIVE)
    song = f"/home/user/Documents/python_exercises/audio_player/songs/{song}.wav"

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def stop():
    pygame.mixer.music.stop()

lblframe1=LabelFrame(root,text="Song Playing")
lblframe1.pack(fill="both")
lblframe1.place()

lblframe2=LabelFrame(root,text="Playlist")
lblframe2.pack(fill="both")
lblframe2.config(bg="aqua")
lblframe2.place(x=450, y=10)
lst_box=Listbox(lblframe2, bg="grey", fg="white", width=60)
lst_box.pack(padx=20, pady=20)


lblframe3=LabelFrame(root,text="Control Panel", padx=180, pady=10)
lblframe3.pack(fill="both")
lblframe3.config(bg="red")
lblframe3.place(x = 80, y = 270)

play_btn=Button(lblframe3, text="Play Song", command=play)
play_btn.grid(row=1, column=1, padx=10)

pause_btn=Button(lblframe3, text="Pause Song", command=pause)
pause_btn.grid(row=1, column=2,padx=10)

unpause_btn=Button(lblframe3, text="Unpause", command=unpause)
unpause_btn.grid(row=1, column=3, padx=10)

stop_btn=Button(lblframe3, text="Stop",width=8, command=stop)
stop_btn.grid(row=1, column=4, padx=10)
my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add Song To Playlist", command=add_song)


root.mainloop()
