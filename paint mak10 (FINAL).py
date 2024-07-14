import tkinter as tk
import random
from tkinter import colorchooser, simpledialog, messagebox
from enum import Enum

class Tool(Enum):
    PENCIL = 1
    ERASER = 2
    SHAPE=3
    RECT =4
    CIRC =5
    RECT1=6
    CIRC1=7
    ARC = 8
    ARC1 = 9
   
class Shape(Enum):
    LINE = 1
    RECTANGLE = 2
    OVAL = 3

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EXCALIBRUHHHHHHHHHHHHHHHH")

        self.current_tool = Tool.PENCIL
        self.current_color = "black"
        self.pencil_size = 2
        self.eraser_size = 10
        self.shape_type = Shape.LINE
        self.shape_fill_color = ""

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.setup_toolbar()
        self.setup_menu()

       
        self.start_x = None
        self.start_y = None
       
        
        self.shapes = []
        self.undo_stack = []
        self.redo_stack = []

        self.setup_keyboard_controls()
    
    
            
        
        
    def setup_toolbar(self):
        toolbar_frame = tk.Frame(self.root)
        toolbar_frame.pack(side=tk.TOP, fill=tk.X)

        self.pencil_button = tk.Button(toolbar_frame, text="PENCIL", command=self.use_pencil)
        self.pencil_button.pack(side=tk.LEFT)

        self.eraser_button = tk.Button(toolbar_frame, text="ERASER", command=self.use_eraser)
        self.eraser_button.pack(side=tk.LEFT)
        
        self.rect_button = tk.Button(toolbar_frame, text="WIERD RECTANGLES", command=self.use_rect)
        self.rect_button.pack(side=tk.LEFT)
        
        self.rect1_button = tk.Button(toolbar_frame, text="RECTANGULAR PENCIL", command=self.use_rect1)
        self.rect1_button.pack(side=tk.LEFT)
        
        
        
        self.circ_button = tk.Button(toolbar_frame, text="WIERD CIRCLES", command=self.use_circ)
        self.circ_button.pack(side=tk.LEFT)
        
        self.circ1_button = tk.Button(toolbar_frame, text="CIRCULAR PENCIL", command=self.use_circ1)
        self.circ1_button.pack(side=tk.LEFT)
        
        self.arc_button = tk.Button(toolbar_frame, text="WIERD ARCS", command=self.use_arc)
        self.arc_button.pack(side=tk.LEFT)
        
        self.arc1_button = tk.Button(toolbar_frame, text="ARC PENCIL", command=self.use_arc1)
        self.arc1_button.pack(side=tk.LEFT)

        self.pencil_color_button = tk.Button(toolbar_frame, text="COLOUR", command=self.choose_pencil_color)
        self.pencil_color_button.pack(side=tk.LEFT)

        self.pencil_size_scale = tk.Scale(toolbar_frame, from_=1, to=10, orient=tk.HORIZONTAL, label="PENCIL SIZE", command=self.set_pencil_size)
        self.pencil_size_scale.pack(side=tk.LEFT, padx=5)

        self.eraser_size_scale = tk.Scale(toolbar_frame, from_=5, to=20, orient=tk.HORIZONTAL, label="ERASER SIZE", command=self.set_eraser_size)
        self.eraser_size_scale.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(toolbar_frame, text="CLEAR", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        

        self.canvas_size_button = tk.Button(toolbar_frame, text="BOARD SIZE", command=self.change_canvas_size)
        self.canvas_size_button.pack(side=tk.LEFT, padx=5)

        self.canvas_color_button = tk.Button(toolbar_frame, text="BOARD COLOUR", command=self.change_canvas_color)
        self.canvas_color_button.pack(side=tk.LEFT, padx=5)

        self.undo_button = tk.Button(toolbar_frame, text="UNDO", command=self.undo)
        self.undo_button.pack(side=tk.LEFT, padx=5)

        self.redo_button = tk.Button(toolbar_frame, text="REDO", command=self.redo)
        self.redo_button.pack(side=tk.LEFT, padx=5)

    def setup_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_canvas)
        file_menu.add_command(label="Save", command=self.save_canvas)
        menubar.add_cascade(label="File", menu=file_menu)

        options_menu = tk.Menu(menubar, tearoff=0)
        options_menu.add_command(label="Canvas Size", command=self.change_canvas_size)
        options_menu.add_command(label="Canvas Color", command=self.change_canvas_color)
        menubar.add_cascade(label="Options", menu=options_menu)

    def setup_keyboard_controls(self):
        self.root.bind("<Up>", lambda event: self.move_pencil("up"))
        self.root.bind("<Down>", lambda event: self.move_pencil("down"))
        self.root.bind("<Left>", lambda event: self.move_pencil("left"))
        self.root.bind("<Right>", lambda event: self.move_pencil("right"))
        self.root.bind("<space>", lambda event: self.stop_pencil())
        self.root.bind("+", lambda event: self.change_item_size("increase"))
        self.root.bind("-", lambda event: self.change_item_size("decrease"))

    def move_pencil(self, direction):
        if self.current_tool == Tool.PENCIL:
            if direction == "up":
                self.canvas.move(tk.ALL, 0, -5)
            elif direction == "down":
                self.canvas.move(tk.ALL, 0, 5)
            elif direction == "left":
                self.canvas.move(tk.ALL, -5, 0)
            elif direction == "right":
                self.canvas.move(tk.ALL, 5, 0)

    def stop_pencil(self):
        # Implement functionality to stop the pencil movement if required.
        pass

    def use_pencil(self):
        self.current_tool = Tool.PENCIL
        self.canvas.config(cursor="pencil")

    def use_eraser(self):
        self.current_tool = Tool.ERASER
        self.canvas.config(cursor="circle")
        
    def use_rect(self):
        self.current_tool = Tool.RECT
        self.canvas.config(cursor="pencil")
        
    def use_rect1(self):
        self.current_tool = Tool.RECT1
        self.canvas.config(cursor="pencil")
        
   
        
    def use_circ(self):
        self.current_tool = Tool.CIRC
        self.canvas.config(cursor="pencil")
        
    def use_circ1(self):
        self.current_tool = Tool.CIRC1
        self.canvas.config(cursor="pencil")
        
    def use_arc(self):
        self.current_tool = Tool.ARC
        self.canvas.config(cursor="pencil")
        
    def use_arc1(self):
        self.current_tool = Tool.ARC1
        self.canvas.config(cursor="pencil")

    def choose_pencil_color(self):
        color = colorchooser.askcolor(parent=self.root, title="Choose Pencil Color")
        if color:
            self.current_color = color[1]

    def set_pencil_size(self, size):
        self.pencil_size = int(size)

    def set_eraser_size(self, size):
        self.eraser_size = int(size)

    def on_move_press(self, event):
        if self.current_tool == Tool.PENCIL:
            if self.start_x and self.start_y:
                self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, width=self.pencil_size, fill=self.current_color, capstyle=tk.ROUND, smooth=True)
                self.undo_stack.append(("line", self.start_x, self.start_y, event.x, event.y, self.pencil_size, self.current_color))
            self.start_x, self.start_y = event.x, event.y

        elif self.current_tool == Tool.ERASER:
            if self.start_x and self.start_y:
                self.canvas.create_rectangle(event.x - self.eraser_size, event.y - self.eraser_size, event.x + self.eraser_size, event.y + self.eraser_size, fill="white", outline="white")
                self.undo_stack.append(("erase", event.x, event.y, self.eraser_size))
            self.start_x, self.start_y = event.x, event.y
            
        elif self.current_tool == Tool.RECT:
            if self.start_x and self.start_y and event.x and event.y:
                self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y ,width=self.pencil_size, fill=self.current_color)
                self.undo_stack.append(("rectangle", self.start_x, self.start_y, event.x, event.y, self.pencil_size, self.current_color))
            self.start_x, self.start_y = event.y, event.x
            
        elif self.current_tool == Tool.CIRC:
             if self.start_x and self.start_y and event.x and event.y:
                 self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y ,width=self.pencil_size, fill=self.current_color)
                 self.undo_stack.append(("oval", self.start_x, self.start_y, event.x, event.y, self.pencil_size, self.current_color))
             self.start_x, self.start_y = event.y, event.x
             
        elif self.current_tool == Tool.RECT1:
            if self.start_x and self.start_y:
                self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, width=self.pencil_size, fill=self.current_color)
                self.undo_stack.append(("rectangle", self.start_x, self.start_y, event.x, event.y, self.pencil_size, self.current_color))
            self.start_x, self.start_y = event.x, event.y
            
        elif self.current_tool == Tool.CIRC1:
            if self.start_x and self.start_y:
                self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, width=self.pencil_size, fill=self.current_color)
                self.undo_stack.append(("oval", self.start_x, self.start_y, event.x, event.y, self.pencil_size, self.current_color))
            self.start_x, self.start_y = event.x, event.y
            
        elif self.current_tool == Tool.ARC:
             if self.start_x and self.start_y and event.x and event.y:
                 self.canvas.create_arc(self.start_x, self.start_y, event.x, event.y ,start=0,extent = random.randint(0,360),width=self.pencil_size, fill=self.current_color)
                 self.undo_stack.append(("arc", self.start_x, self.start_y, event.x, event.y, self.pencil_size, self.current_color))
             self.start_x, self.start_y = event.y, event.x
             
        elif self.current_tool == Tool.ARC1:
             if self.start_x and self.start_y and event.x and event.y:
                 self.canvas.create_arc(self.start_x, self.start_y, event.x, event.y ,start=0,extent = random.randint(0,360),width=self.pencil_size, fill=self.current_color)
                 self.undo_stack.append(("arc", self.start_x, self.start_y, event.x, event.y, self.pencil_size, self.current_color))
             self.start_x, self.start_y = event.x, event.y
        
       
            
    def on_button_release(self, event):
        self.start_x, self.start_y = None,None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.shapes = []
        self.undo_stack = []
        self.redo_stack = []

    def new_canvas(self):
        self.clear_canvas()

    def save_canvas(self):
        messagebox.showinfo("Save", "Canvas saved as image")

    def change_canvas_size(self):
        width = simpledialog.askinteger("Canvas Width", "Enter canvas width:", parent=self.root)
        height = simpledialog.askinteger("Canvas Height", "Enter canvas height:", parent=self.root)
        if width and height:
            self.canvas.config(width=width, height=height)

    def change_canvas_color(self):
        color = colorchooser.askcolor(parent=self.root, title="Choose Canvas Color")
        if color:
            self.canvas.config(bg=color[1])
  
    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.redo_stack.append(action)
            self.redraw_canvas()

    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            self.undo_stack.append(action)
            self.redraw_canvas()

    def redraw_canvas(self):
        self.canvas.delete("all")
        for action in self.undo_stack:
            if action[0] == "line":
                self.canvas.create_line(action[1], action[2], action[3], action[4], width=action[5], fill=action[6], capstyle=tk.ROUND, smooth=True)
            elif action[0] == "erase":
                self.canvas.create_rectangle(action[1] - action[3], action[2] - action[3], action[1] + action[3], action[2] + action[3], fill="white", outline="white")

    def change_item_size(self, action):
        if self.undo_stack:
            last_action = self.undo_stack[-1]
            if last_action[0] == "line":
                x1, y1, x2, y2, size, color = last_action[1:]
                if action == "increase":
                    size += 1
                elif action == "decrease":
                    size -= 1 if size > 1 else 0
                self.undo_stack[-1] = ("line", x1, y1, x2, y2, size, color)
            elif last_action[0] == "erase":
                x, y, size = last_action[1:]
                if action == "increase":
                    size += 1
                elif action == "decrease":
                    size -= 1 if size > 1 else 0
                self.undo_stack[-1] = ("erase", x, y, size)
            self.redraw_canvas()

if __name__ == "__main__":
    root = tk.Tk()
    paint_app = PaintApp(root)
    root.mainloop()
