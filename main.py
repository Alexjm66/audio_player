from tkinter import *
import pygame
from tkinter import filedialog
root=Tk()
root.title("")
root.config(bg="aqua")
root.geometry("950x340")

pygame.mixer.init()

def add_song():
    song = filedialog.askopenfilename(initialdir="songs", title="Choose a Song", filetypes=(("wav Files","*.wav"),))
    song = song.replace("/home/user/Documents/python_exercises/audio_player/songs/", "")
    song = song.replace(".wav", "")
    lst_box.insert(END, song)

def play():
    song = lst_box.get(ACTIVE)
    song1 = f"/home/user/Documents/python_exercises/audio_player/songs/{song}.wav"

    pygame.mixer.music.load(song1)
    pygame.mixer.music.play(loops=0)
    display['text']=song

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def stop():
    pygame.mixer.music.stop()

def exit():
    root.destroy()

display = Label(root,text="", relief="groove", bg="grey", fg="white")
display.pack()
display.config(width=48, height=4)
display.place(x = 5, y = 80)

lblframe1=LabelFrame(root,text="Playlist")
lblframe1.pack(fill="both")
lblframe1.config(bg="red")
lblframe1.place(x=410, y=10)
lst_box=Listbox(lblframe1, bg="grey", fg="white", width=60)
lst_box.pack(padx=20, pady=20)

lblframe2=LabelFrame(root,text="Control Panel", padx=130, pady=10)
lblframe2.pack(fill="both")
lblframe2.config(bg="red")
lblframe2.place(x = 10, y = 260)

play_btn=Button(lblframe2, text="Play Song", command=play)
play_btn.grid(row=1, column=1, padx=10)

pause_btn=Button(lblframe2, text="Pause Song", command=pause)
pause_btn.grid(row=1, column=2,padx=10)

unpause_btn=Button(lblframe2, text="Unpause", command=unpause)
unpause_btn.grid(row=1, column=3, padx=10)

stop_btn=Button(lblframe2, text="Stop", command=stop)
stop_btn.grid(row=1, column=4, padx=10)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add Song To Playlist", command=add_song)

exit_btn=Button(root,text="Exit Program", width=24, height=2, command=exit)
exit_btn.pack()
exit_btn.place(x = 710, y = 275 )

root.mainloop()
