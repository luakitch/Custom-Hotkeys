import tkinter as tk
from tkinter import simpledialog
import pyautogui
from screeninfo import get_monitors

class PixelMeasurementTool:
    def __init__(self, root, monitor):
        self.root = root
        self.monitor = monitor
        self.start_x = None
        self.start_y = None
        
        # Set up the window on the selected screen
        self.root.attributes("-alpha", 0.3)
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.geometry(f"{monitor.width}x{monitor.height}+{monitor.x}+{monitor.y}")

        # Bind mouse events and the Esc key
        self.root.bind("<ButtonPress-1>", self.start_measurement)
        self.root.bind("<B1-Motion>", self.update_measurement)
        self.root.bind("<ButtonRelease-1>", self.end_measurement)
        self.root.bind("<Escape>", self.close_app)
        
        # Create a canvas for drawing the rectangles
        self.canvas = tk.Canvas(root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.rect = None
        self.label = tk.Label(root, bg="white", font=("Arial", 12))
        self.label.place(x=10, y=10)
        self.rectangles = []

    def start_measurement(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="red", width=2)

    def update_measurement(self, event):
        if self.rect:
            self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)
            width = abs(event.x - self.start_x)
            height = abs(event.y - self.start_y)
            self.label.config(text=f"{width}px x {height}px")
            self.label.place(x=event.x + 10, y=event.y + 10)

    def end_measurement(self, event):
        if self.rect:
            end_x, end_y = pyautogui.position()
            width = abs(end_x - (self.monitor.x + self.start_x))
            height = abs(end_y - (self.monitor.y + self.start_y))
            self.label.config(text=f"Final Size: {width}px x {height}px")
            print(f"Measured Width: {width}px, Measured Height: {height}px")
            # Store the final rectangle
            self.rectangles.append(self.rect)
            self.rect = None  # Allow drawing a new rectangle

    def close_app(self, event):
        print("Closing application...")
        self.root.quit()

def select_monitor():
    monitors = get_monitors()
    root = tk.Tk()
    root.withdraw()

    selected_monitor = simpledialog.askinteger(
        "Select Monitor",
        "Enter the monitor number:\n" + "\n".join([f"{i+1}: {m.width}x{m.height}" for i, m in enumerate(monitors)])
    )

    if selected_monitor is not None and 1 <= selected_monitor <= len(monitors):
        return monitors[selected_monitor - 1]
    else:
        print("Invalid monitor selection.")
        root.quit()
        return None

if __name__ == "__main__":
    selected_monitor = select_monitor()
    if selected_monitor:
        root = tk.Tk()
        app = PixelMeasurementTool(root, selected_monitor)
        root.mainloop()
