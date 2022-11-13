#we import libraries
from PIL import ImageTk, Image

def read_image(path, size):
        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))

def center_window(window, app_width, app_height):
    window_width=window.winfo_screenwidth()
    window_height=window.winfo_screenheight()
    x = int((window_width/2) - (app_width/2))
    y = int((window_height/2 - (app_height/2)))
    return window.geometry(f"{app_width}x{app_height}+{x}+{y}")



