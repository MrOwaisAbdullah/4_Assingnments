import tkinter as tk

ERASE_SIZE = 40

def main():
    root = tk.Tk()
    root.title("Simple Eraser")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    canvas.create_rectangle(0, 0, 400, 400, fill="blue", outline="")

    def on_drag(event):
        x, y = event.x, event.y
        canvas.create_rectangle(x, y, x + ERASE_SIZE, y + ERASE_SIZE, fill="white", outline="")

    canvas.bind("<B1-Motion>", on_drag)

    root.mainloop()

if __name__ == '__main__':
    main()