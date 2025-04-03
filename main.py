import time
import tkinter as tk
from tkinter import messagebox
import winsound


def show_popup(title, message):
    root=tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)

def play_sound():
    winsound.Beep(1000, 500)

def pomodoro_timer(study_time=25, break_time=5):
    while True:

        show_popup("Watunya belajar", "Fokus selama 25 menit!")
        time.sleep(study_time*60)

        show_popup("Waktunya istirahat", "Istirahat selama 5 menit!")
        time.sleep(break_time*60)

if __name__ == "__main__":
    pomodoro_timer()