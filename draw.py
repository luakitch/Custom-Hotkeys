import tkinter as tk
from screeninfo import get_monitors
import keyboard


class DrawingApp:
    def __init__(self, root, screen_width, screen_height, offset_x=0, offset_y=0):
        self.root = root
        self.root.geometry(f"{screen_width}x{screen_height}+{offset_x}+{offset_y}")
        self.root.attributes("-topmost", True)
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.2)
        self.root.configure(bg="black")
        self.canvas = tk.Canvas(root, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.drawing = False
        self.last_x, self.last_y = None, None

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)
        self.root.bind("<Escape>", self.close_all_windows)

    def start_drawing(self, event):
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.drawing:
            self.canvas.create_line(
                (self.last_x, self.last_y, event.x, event.y), width=6, fill="black"
            )
            self.last_x, self.last_y = event.x, event.y

    def stop_drawing(self, event):
        self.drawing = False

    def close_all_windows(self, event=None):
        global windows
        for window in windows:
            window.destroy()
        windows = []  # Reset the windows list


def launch_drawing_app():
    global windows
    windows = []

    monitors = get_monitors()
    for monitor in monitors:
        root = tk.Tk()
        app = DrawingApp(root, monitor.width, monitor.height, monitor.x, monitor.y)
        windows.append(root)

    for window in windows:
        window.mainloop()


# Listen for the hotkey "Ctrl+Z+X" to launch the drawing app
keyboard.add_hotkey("ctrl+z+x", launch_drawing_app)

# Keep the script running to listen for hotkeys
keyboard.wait()
