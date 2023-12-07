from tkinter import *
from tkinter import ttk

import time

def current_milli_time():
    return round(time.time() * 1000)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480

BOTTOM_HEIGHT = 60
SIDEBAR_WIDTH = 160

CENTER_WIDTH = 360
CENTER_BOTTOM_HEIGHT = 320

QUIT_BUTTON_OFFSET = SCREEN_WIDTH - 95

# displays data returned by calling display_func, label updates every freq milliseconds
# displays it in middle of parent_frame
class DynamicLabel:
    def __init__(self, parent_frame, display_func, freq, font_config="Arial 16"):
        self.display_func = display_func
        self.freq = freq
        self.font_config = font_config
        self.parent_frame = parent_frame
        self.label = ttk.Label(parent_frame, font=font_config, text=self.display_func())
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.label.after(self.freq, self.update)
    def update(self):
        self.label.configure(text=self.display_func())
        self.label.after(self.freq, self.update)

# time elapsed display label
class TimeElapsedLabel(DynamicLabel):
    def __init__(self, parent_frame, freq, font_config="Arial 32"):
        self.start_time = current_milli_time()
        func = self.get_elapsed_time
        super().__init__(parent_frame, func, freq, font_config)
    def get_elapsed_time(self):
        cur_time = current_milli_time()
        dt = cur_time - self.start_time
        dt = int(dt/1000) # convert to seconds
        seconds = str(dt % 60).zfill(2)
        minutes = str(dt // 60).zfill(2)
        return(minutes + ":" + seconds)

def setup_gui():
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

    #time_label = DynamicLabel(center_frame, current_milli_time, 1)
    time_label_frame = ttk.Frame(center_frame, width=CENTER_WIDTH/2, height=SCREEN_HEIGHT - BOTTOM_HEIGHT - CENTER_BOTTOM_HEIGHT)
    time_label_frame.place(x=CENTER_WIDTH / 2, y=CENTER_BOTTOM_HEIGHT)
    time_label = TimeElapsedLabel(time_label_frame, 1)

    root.mainloop()

def main():
    setup_gui()

if __name__ == "__main__":
    main()
