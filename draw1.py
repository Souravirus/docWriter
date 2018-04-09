#from imageRead import imageClick
import imageSegmenter2 as ImageSegment

#external imports
from tkinter import *
from tkinter.colorchooser import askcolor
from pyautogui import screenshot

class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()
        w = 600
        h = 400
        x=100
        y=100
        #self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.buttonFrame = Frame(self.root)
        self.buttonFrame.pack()
        self.pen_button = Button(self.buttonFrame, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.buttonFrame, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.buttonFrame, text='color', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.buttonFrame, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.buttonFrame, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=1, column=1)
        
        self.ran_button = Button(self.buttonFrame,text = 'clear',command=self.clear_screen)
        self.ran_button.grid(row=0,column=4)

        #self.canvasFrame = Frame(self.root,bg='#a2a133')
        #self.canvasFrame.pack(expand=YES,fill=BOTH)

        self.c = Canvas(self.root, bg='white',width=595,height=195)
        self.c.pack(expand=YES,fill=BOTH)
        #self.c = Canvas(self.canvasFrame, bg='white', width=600, height=200)
        #self.c.grid(row=0, columnspan=4)
        #self.recogniseFrame = Frame(self.root)
        #self.recogniseFrame.pack(side=BOTTOM)
        self.recognise_button = Button(self.buttonFrame, text='recognise',command=lambda x=self.c: self.capture(x))
        self.recognise_button.grid(row = 0,column=5)
        #wc = tkinter.Canvas(window,width='30',height='20',relief=tkinter.SUNKEN)
        #wc.pack(expand = tkinter.YES, fill = tkinter.BOTH,padx=10,pady=10)
        #105, 170, 700, 365
        Label(self.root,text='Output:').pack(side=LEFT)
        self.outputHolder = StringVar()
        self.outputHolder.set('No output')
        self.output = Message(self.root,textvariable=self.outputHolder,  bg='white',fg='black',anchor='w',justify=LEFT,aspect=100000)
        self.output.pack(fill=X,padx=5,pady=5,side=BOTTOM)
        
        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)
    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)
    def clear_screen(self):
        self.c.delete('all')
    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y
    def capture(self,widget):
        x=self.root.winfo_rootx()+widget.winfo_x()
        y=self.root.winfo_rooty()+widget.winfo_y()
        x1=widget.winfo_width()
        y1=widget.winfo_height()
        print(x,y,x1,y1)
        screenshot(region=(x+1,y+1,x1-2,y1-2)).save('Hello1.png')
        outputText = ImageSegment.getText()
        self.outputHolder.set(outputText) 
    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()
