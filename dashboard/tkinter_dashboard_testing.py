from tkinter import *
from tkinter import ttk

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480

BOTTOM_HEIGHT = 60
SIDEBAR_WIDTH = 160

CENTER_WIDTH = 360

QUIT_BUTTON_OFFSET = SCREEN_WIDTH - 95

root = Tk()
root.geometry("{}x{}".format(SCREEN_WIDTH, SCREEN_HEIGHT))
s = ttk.Style()
s.configure("Debug_Cyan.TFrame", background='cyan')
s.configure("Debug_Magenta.TFrame", background='magenta')
s.configure("Debug_Yellow.TFrame", background='yellow')

btm_frame = ttk.Frame(root, width=SCREEN_WIDTH, height=BOTTOM_HEIGHT)
btm_frame.grid(column=0, row=1, columnspan=3, sticky="sw", padx=10, pady=5)

# left sidebar - ready indicator & regen
sidebar_l_frame = ttk.Frame(root, width=SIDEBAR_WIDTH, height=SCREEN_HEIGHT - BOTTOM_HEIGHT)
sidebar_l_frame.grid(column=0, row=0, sticky="nw", padx=10, pady=10)
sidebar_l_frame.configure(style="Debug_Cyan.TFrame")

# center frame - most important data
center_frame = ttk.Frame(root, width=CENTER_WIDTH, height=SCREEN_HEIGHT - BOTTOM_HEIGHT)
center_frame.grid(column=1, row=0, sticky="nw", padx=10, pady=10)
center_frame.configure(style="Debug_Magenta.TFrame")

# right sidebar - BMS data
sidebar_r_frame = ttk.Frame(root, width=SIDEBAR_WIDTH, height=SCREEN_HEIGHT - BOTTOM_HEIGHT)
sidebar_r_frame.grid(column=2, row=0, sticky="nw", padx=10, pady=10)
sidebar_r_frame.configure(style="Debug_Yellow.TFrame")

# bottom frame - error & quit
l1 = ttk.Label(btm_frame, text="Put error message here")
l1.place(x=0, y=0)
# button just here for easier testing, in actual operation should disable this
b1 = ttk.Button(btm_frame, text="Quit GUI", command=root.destroy)
b1.place(x=QUIT_BUTTON_OFFSET, y=0)

root.mainloop()
