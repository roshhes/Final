from tkinter import *
def base():
  from tkinter import Tk
  import tkinter as tk
  def default_player():
    from default import MusicPlayer
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
  def bloody_player():
    from bloody import MusicPlayer
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
  def cute_player():
    from cute import MusicPlayer
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
  def summer_player():
    from summer import MusicPlayer
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
  def sea_player():
    from sea import MusicPlayer
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
  def alien_player():
    from alien import MusicPlayer
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
  def pastel_player():
    from pastel import MusicPlayer
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
  def winter_player():
    from winter import MusicPlayer
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
  # Creating TK Container
  root=Tk()
  #
  root.title("PLAYLIST")
  #icon
  #root.iconbitmap(r'n1.ico')
  # Window Geometry
  root.geometry("400x400")
  # Disable resizing
  root.resizable(False,False)
  # Frame for radio buttons
  alien=PhotoImage(file='D:/final/real/alien.png')
  summer=PhotoImage(file='D:/final/real/summer.png')
  pastel=PhotoImage(file='D:/final/real/pastel.png')
  cute=PhotoImage(file='D:/final/real/cute.png')
  sea=PhotoImage(file='D:/final/real/sea.png')
  winter=PhotoImage(file='D:/final/real/winter.png')
  dark=PhotoImage(file='D:/final/real/dark.png')
  blood=PhotoImage(file='D:/final/real/blood.png')
  buttonframe = LabelFrame(root,text="Choose A Theme",bg="lavender",fg="black",bd=5,relief=FLAT)
  buttonframe.place(x=0,y=0,width=400,height=400)
      # Inserting Play Button
  default_btn = Button(buttonframe,image=dark,command=default_player,relief=FLAT, activebackground="#ff92ed").grid(row=0,column=5,padx=20,pady=15)
  bloody_btn = Button(buttonframe,image=blood,command=bloody_player ,relief=FLAT, activebackground="#ff92ed").grid(row=0,column=15,padx=10,pady=15)
  cute_btn = Button(buttonframe,image=cute,command=cute_player,relief=FLAT, activebackground="#ff92ed").grid(row=3,column=5,padx=10,pady=15)
  summer_btn = Button(buttonframe,image=summer,command=summer_player,relief=FLAT, activebackground="#ff92ed").grid(row=3,column=15,padx=10,pady=15)
  sea_btn = Button(buttonframe,image=sea,command=sea_player,relief=FLAT, activebackground="#ff92ed").grid(row=5,column=5,padx=10,pady=15)
  alien_btn = Button(buttonframe,image=alien ,command=alien_player,relief=FLAT, activebackground="#ff92ed").grid(row=5,column=15,padx=10,pady=15)
  pastel_btn = Button(buttonframe,image=pastel,command=pastel_player,relief=FLAT, activebackground="#ff92ed").grid(row=7,column=5,padx=10,pady=15)
  winter_btn = Button(buttonframe,image=winter,command=winter_player,relief=FLAT, activebackground="#ff92ed").grid(row=7,column=15,padx=10,pady=15)
  # Root Window Looping
  root.mainloop()
