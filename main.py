import threading
import multiprocessing
import time
from datetime import datetime
import os
from git_data import GitData
from tkinter import Tk, LabelFrame, Label, Button, Entry, filedialog, StringVar
from tkinter.ttk import Progressbar, Style
from PIL import Image, ImageTk
import openpyxl

with open(f"data.dat", "r") as io:
    raw = io.read().split(',')

width, height = 1366, 768
g_data = GitData()
date, month_year = str(int(datetime.now().strftime("%d"))), datetime.now().strftime("%B %Y").split(" ")



class PTG:
    def __init__(self, window):

        self.data = {}
        self.data_name = []
        self.main = window
        self.frame_1 = LabelFrame(self.main, bg="white", fg="black", bd=0)
        self.main.geometry(newGeometry=f"{width}x{height}+{int((self.main.winfo_screenwidth() - width) / 2)}+"
                                       f"{int((self.main.winfo_screenheight() - height) / 2) - 20}")
        self.main.title("C P T")

        self.main.bind('<Button-1>', self.click)
        self.notification = Label(self.main, fg="black", bg="white", font=("Segoe UI", 12), relief="solid",
                                  bd=0, anchor="s")
        self.notification.place(x=width - 100, y=height - 20, width=100, height=20)
        self.sync()
        self.main.protocol('WM_DELETE_WINDOW', self.exit)

    def fetch_data(self):
        self.data = str(requests.get("http://anodicpassion.pythonanywhere.com/").content)[2:].split("|")

    def progress(self):
        self.frame_1 = LabelFrame(self.main, bg="white", fg="black", bd=0)
        self.cnt = 1

        def close_progress():
            self.frame_1.destroy()

        self.frame_1.place(x=0, y=0, width=width, height=height)
        Button(self.frame_1, text="↼", fg="black", bg="white", font=("calibre", 25), foreground="black",
               background="white", relief="solid", bd=0, command=close_progress).place(x=0, y=0, width=50, height=50)
        style = Style()
        style.theme_use('alt')
        style.configure("pg_1.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pg_2.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pg_3.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pg_4.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pg_5.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pg_6.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pg_7.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pg_8.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pg_9.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pg_10.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pg_11.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pg_12.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pg_13.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pg_14.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")

        style.configure("pgr_1.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pgr_2.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pgr_3.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pgr_4.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pgr_5.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pgr_6.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pgr_7.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pgr_8.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pgr_9.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pgr_10.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pgr_11.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pgr_12.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pgr_13.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")
        style.configure("pgr_14.Horizontal.TProgressbar", troughcolor="white",
                        bordercolor="black", background="orange", lightcolor="white",
                        darkcolor="white")

        pg_1 = Progressbar(self.frame_1, style="pg_1.Horizontal.TProgressbar")
        pg_1.place(x=308, y=50, width=300, height=30)
        pg_2 = Progressbar(self.frame_1, style="pg_2.Horizontal.TProgressbar")
        pg_2.place(x=308, y=100, width=300, height=30)
        pg_3 = Progressbar(self.frame_1, style="pg_3.Horizontal.TProgressbar")
        pg_3.place(x=308, y=150, width=300, height=30)
        pg_4 = Progressbar(self.frame_1, style="pg_4.Horizontal.TProgressbar")
        pg_4.place(x=308, y=200, width=300, height=30)
        pg_5 = Progressbar(self.frame_1, style="pg_5.Horizontal.TProgressbar")
        pg_5.place(x=308, y=250, width=300, height=30)
        pg_6 = Progressbar(self.frame_1, style="pg_6.Horizontal.TProgressbar")
        pg_6.place(x=308, y=300, width=300, height=30)
        pg_7 = Progressbar(self.frame_1, style="pg_7.Horizontal.TProgressbar")
        pg_7.place(x=308, y=350, width=300, height=30)
        pg_8 = Progressbar(self.frame_1, style="pg_8.Horizontal.TProgressbar")
        pg_8.place(x=308, y=400, width=300, height=30)
        pg_9 = Progressbar(self.frame_1, style="pg_9.Horizontal.TProgressbar")
        pg_9.place(x=308, y=450, width=300, height=30)
        pg_10 = Progressbar(self.frame_1, style="pg_10.Horizontal.TProgressbar")
        pg_10.place(x=308, y=500, width=300, height=30)
        pg_11 = Progressbar(self.frame_1, style="pg_11.Horizontal.TProgressbar")
        pg_11.place(x=308, y=550, width=300, height=30)
        pg_12 = Progressbar(self.frame_1, style="pg_12.Horizontal.TProgressbar")
        pg_12.place(x=308, y=600, width=300, height=30)
        pg_13 = Progressbar(self.frame_1, style="pg_13.Horizontal.TProgressbar")
        pg_13.place(x=308, y=650, width=300, height=30)
        pg_14 = Progressbar(self.frame_1, style="pg_14.Horizontal.TProgressbar")
        pg_14.place(x=308, y=700, width=300, height=30)

        pgr_1 = Progressbar(self.frame_1, style="pgr_1.Horizontal.TProgressbar")
        pgr_1.place(x=956, y=50, width=300, height=30)
        pgr_2 = Progressbar(self.frame_1, style="pgr_2.Horizontal.TProgressbar")
        pgr_2.place(x=956, y=100, width=300, height=30)
        pgr_3 = Progressbar(self.frame_1, style="pgr_3.Horizontal.TProgressbar")
        pgr_3.place(x=956, y=150, width=300, height=30)
        pgr_4 = Progressbar(self.frame_1, style="pgr_4.Horizontal.TProgressbar")
        pgr_4.place(x=956, y=200, width=300, height=30)
        pgr_5 = Progressbar(self.frame_1, style="pgr_5.Horizontal.TProgressbar")
        pgr_5.place(x=956, y=250, width=300, height=30)
        pgr_6 = Progressbar(self.frame_1, style="pgr_6.Horizontal.TProgressbar")
        pgr_6.place(x=956, y=300, width=300, height=30)
        pgr_7 = Progressbar(self.frame_1, style="pgr_7.Horizontal.TProgressbar")
        pgr_7.place(x=956, y=350, width=300, height=30)
        pgr_8 = Progressbar(self.frame_1, style="pgr_8.Horizontal.TProgressbar")
        pgr_8.place(x=956, y=400, width=300, height=30)
        pgr_9 = Progressbar(self.frame_1, style="pgr_9.Horizontal.TProgressbar")
        pgr_9.place(x=956, y=450, width=300, height=30)
        pgr_10 = Progressbar(self.frame_1, style="pgr_10.Horizontal.TProgressbar")
        pgr_10.place(x=956, y=500, width=300, height=30)
        pgr_11 = Progressbar(self.frame_1, style="pgr_11.Horizontal.TProgressbar")
        pgr_11.place(x=956, y=550, width=300, height=30)
        pgr_12 = Progressbar(self.frame_1, style="pgr_12.Horizontal.TProgressbar")
        pgr_12.place(x=956, y=600, width=300, height=30)
        pgr_13 = Progressbar(self.frame_1, style="pgr_13.Horizontal.TProgressbar")
        pgr_13.place(x=956, y=650, width=300, height=30)
        pgr_14 = Progressbar(self.frame_1, style="pgr_14.Horizontal.TProgressbar")
        pgr_14.place(x=956, y=700, width=300, height=30)

        lbl_1 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbl_1.place(x=8, y=50, width=300, height=30)
        lbl_2 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbl_2.place(x=8, y=100, width=300, height=30)
        lbl_3 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbl_3.place(x=8, y=150, width=300, height=30)
        lbl_4 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbl_4.place(x=8, y=200, width=300, height=30)
        lbl_5 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbl_5.place(x=8, y=250, width=300, height=30)
        lbl_6 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbl_6.place(x=8, y=300, width=300, height=30)
        lbl_7 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbl_7.place(x=8, y=350, width=300, height=30)
        lbl_8 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbl_8.place(x=8, y=400, width=300, height=30)
        lbl_9 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbl_9.place(x=8, y=450, width=300, height=30)
        lbl_10 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbl_10.place(x=8, y=500, width=300, height=30)
        lbl_11 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbl_11.place(x=8, y=550, width=300, height=30)
        lbl_12 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbl_12.place(x=8, y=600, width=300, height=30)
        lbl_13 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbl_13.place(x=8, y=650, width=300, height=30)
        lbl_14 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbl_14.place(x=8, y=700, width=300, height=30)

        lbr_1 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbr_1.place(x=624, y=50, width=300, height=30)
        lbr_2 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbr_2.place(x=624, y=100, width=300, height=30)
        lbr_3 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbr_3.place(x=624, y=150, width=300, height=30)
        lbr_4 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbr_4.place(x=624, y=200, width=300, height=30)
        lbr_5 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbr_5.place(x=624, y=250, width=300, height=30)
        lbr_6 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbr_6.place(x=624, y=300, width=300, height=30)
        lbr_7 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbr_7.place(x=624, y=350, width=300, height=30)
        lbr_8 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbr_8.place(x=624, y=400, width=300, height=30)
        lbr_9 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbr_9.place(x=624, y=450, width=300, height=30)
        lbr_10 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbr_10.place(x=624, y=500, width=300, height=30)
        lbr_11 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbr_11.place(x=624, y=550, width=300, height=30)
        lbr_12 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbr_12.place(x=624, y=600, width=300, height=30)
        lbr_13 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbr_13.place(x=624, y=650, width=300, height=30)
        lbr_14 = Label(self.frame_1, bg="white", fg="black", font=("Segoe UI", 20))
        lbr_14.place(x=624, y=700, width=300, height=30)

        def show_data(val: int = 0, std_name=""):

            if 0 < val <= 4:
                color = "#02231c"
            elif 4 < val <= 8:
                color = "#004d25"
            elif 8 < val <= 15:
                color = "#11823b"
            elif 15 < val <= 20:
                color = "#48bf53"
            else:
                color = "#91f086"
            if 0 <= self.cnt <= 14:
                pg_name = "pg_" + str(self.cnt)
            else:
                pg_name = "pgr_" + str(self.cnt)
            style.configure(f"{pg_name}.Horizontal.TProgressbar", background=color)
            # print("pgname: ", pg_name)
            if pg_name == "pg_1":
                pg_1['value'] = val
                lbl_1.config(text=std_name)
            elif pg_name == "pg_2":
                pg_2["value"] = val
                lbl_2.config(text=std_name)
            elif pg_name == "pg_3":
                pg_3["value"] = val
                lbl_3.config(text=std_name)
            elif pg_name == "pg_4":
                pg_4["value"] = val
                lbl_4.config(text=std_name)
            elif pg_name == "pg_5":
                pg_5["value"] = val
                lbl_5.config(text=std_name)
            elif pg_name == "pg_6":
                pg_6["value"] = val
                lbl_6.config(text=std_name)
            elif pg_name == "pg_7":
                pg_7["value"] = val
                lbl_7.config(text=std_name)
            elif pg_name == "pg_8":
                pg_8["value"] = val
                lbl_8.config(text=std_name)
            elif pg_name == "pg_9":
                pg_9["value"] = val
                lbl_9.config(text=std_name)
            elif pg_name == "pg_10":
                pg_10["value"] = val
                lbl_10.config(text=std_name)
            elif pg_name == "pg_11":
                pg_11["value"] = val
                lbl_11.config(text=std_name)
            elif pg_name == "pg_12":
                pg_12["value"] = val
                lbl_12.config(text=std_name)
            elif pg_name == "pg_13":
                pg_13["value"] = val
                lbl_13.config(text=std_name)
            elif pg_name == "pg_14":
                pg_14["value"] = val
                lbl_14.config(text=std_name)
            elif pg_name == "pgr_1":
                pgr_1["value"] = val
            elif pg_name == "pgr_2":
                pgr_2["value"] = val
            elif pg_name == "pgr_3":
                pgr_3["value"] = val
            elif pg_name == "pgr_4":
                pgr_4["value"] = val
            elif pg_name == "pgr_5":
                pgr_5["value"] = val
            elif pg_name == "pgr_6":
                pgr_6["value"] = val
            elif pg_name == "pgr_7":
                pgr_7["value"] = val
            elif pg_name == "pgr_8":
                pgr_8["value"] = val
            elif pg_name == "pgr_9":
                pgr_9["value"] = val
            elif pg_name == "pgr_10":
                pgr_10["value"] = val
            elif pg_name == "pgr_11":
                pgr_11["value"] = val
            elif pg_name == "pgr_12":
                pgr_12["value"] = val
            elif pg_name == "pgr_13":
                pgr_13["value"] = val
            elif pg_name == "pgr_14":
                pgr_14["value"] = val

            self.cnt = self.cnt + 1

        for inte, i in enumerate(self.data):
            s_name, contrib = i.split("->")
            if "No" in contrib:
                val = 0
            else:
                val = int(contrib.split(">")[-1].split(" ")[0])
            print(val, s_name)
            show_data(val, s_name)
            if len(self.data)-2 == inte:
                break

    def click(self, event):
        if 557 > event.x > 457 and 270 < event.y < 370:
            self.progress()
        elif 557 > event.x > 457 and 435 < event.y < 535:
            print("event 2 triggered")
        elif 734 > event.x > 634 and 270 < event.y < 370:
            print("event 3 triggered")
        elif 734 > event.x > 634 and 435 < event.y < 535:
            print("event 4 triggered")
        elif 910 > event.x > 810 and 270 < event.y < 370:
            print("event 5 triggered")
        elif 910 > event.x > 810 and 435 < event.y < 535:
            print("event 6 triggered")
        return


if __name__ == "__main__":
    win = Tk()
    win.resizable(False, False)
    bg_img = ImageTk.PhotoImage(Image.open("bg.dat"))
    bg = Label(win, image=bg_img)
    bg.pack()

    PTG(win)
    win.mainloop()





