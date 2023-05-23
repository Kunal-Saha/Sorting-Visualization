from tkinter import *    #for the GUI part
from tkinter import ttk   #for the comboBox in line 79
import random    #for generate the array for sorting
import time   # whenever a swap happens the is a time gap to understand the visualization

#################
#   Bubble Sort
##################
def bubble_sort(data, drawrectangle, delay):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawrectangle(data, ['blue' if x == j or x == j+1 else 'red' for x in range(len(data))] )
                time.sleep(delay)
    drawrectangle(data, ['green' for x in range(len(data))])

root = Tk()   #for the window of the GUI
root.title('DSA PROJECT Sorting Algorithm Visualiser')
root.geometry("1050x700")
root.config(bg='yellow')

select_algorithm = StringVar()
arr = []

#GENERATING THE ARRAY 
def Generate_array():
    global arr
    lowest = int(lowest_Entry.get())
    highest = int(highest_Entry.get())
    size = int(arrsize_Entry.get())

    arr = []
    for i in range(size):
        #by using random.range we are getting random numbers and we are appending it to our array
        arr.append(random.randrange(lowest, highest+1))  

    drawrectangle(arr, ['red' for x in range(len(arr))]) 
    
    

#DRAWING THE ARRAY ELEMENTS AS RECTANGLES
def drawrectangle(arr, colorArray):
    canvas.delete("all")  # Every time a swap happens the bars show be redrawn so as to visualize clearly
    canvas_height = 380
    canvas_width = 600
    bar_width = canvas_width / (len(arr) + 1)
    border_offset = 30    #gap at the edges of the border
    spacing = 10     #gap between each bar
    normalized_array = [ i / max(arr) for i in arr]
    #we had to normalize the array else one value will be very high and other will be very low
    for i, height in enumerate(normalized_array):
        #top left coordinates
        #border_offset means how much it should be gap from the border
        x0 = i * bar_width + border_offset + spacing 
        y0 = canvas_height - height * 340
        #bottom right coordinates
        x1 = (i + 1) * bar_width + border_offset
        y1 = canvas_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])  #for creating the bars
        canvas.create_text(x0+2,y0,anchor=SW,text=str(arr[i]))
    
    root.update_idletasks()   #to update inside the GUI


def sorting1():     #func for the Bubble Sort
    global arr
    bubble_sort(arr, drawrectangle, sortingspeed.get())


#GUI CODING PART

options_frame = Frame(root, width= 1000, height=400, bg='yellow') #for the outer frame
options_frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(root, width=900, height=450, bg='grey')  #for the inner grid
canvas.grid(row=3, column=0, padx=10, pady=5)    #here 'place' function can also be used

# as the label is inside the gui thus it is "options_frame"
Label(options_frame, text="CHOOSE THE ALGORITHM  --> ",bg='green').grid(row=0, column=0, padx=10, pady=10)
#Label(options_frame,text="-->",).grid(row=0,column=1,padx=3, pady=3)
algomenu = ttk.Combobox(options_frame, textvariable=select_algorithm, values=['Select','BUBBLE SORT'],width=15)
algomenu.grid(row=0, column=1, padx=5, pady=5)
algomenu.current(0)

sortingspeed = Scale(options_frame, from_=0.1, to=2.0, length=110, digits=2, resolution=0.1, orient=HORIZONTAL, label="SPEED OF SORTING ", bg='light blue')
sortingspeed.grid(row=0, column=3, padx=10, pady=10)

Button(options_frame, text="START SORTING", command=sorting1, bg='red',height=5).grid(row=1, column=5, padx=5, pady=5)

lowest_Entry = Scale(options_frame, from_=3, to=15, resolution=1, orient=HORIZONTAL, label="LOWER LIMIT", bg='pink')
lowest_Entry.grid(row=1, column=0, padx=5, pady=5)

highest_Entry = Scale(options_frame, from_=20, to=100, resolution=1, orient=HORIZONTAL, label="UPPER LIMIT",bg ='pink')
highest_Entry.grid(row=1, column=1, padx=5, pady=5)

arrsize_Entry = Scale(options_frame, from_=3, to=50, length=120, resolution=1, orient=HORIZONTAL, label="SIZE OF THE ARRAY",bg='light blue')
arrsize_Entry.grid(row=0, column=5, padx=5, pady=7)

#command --> what should happen after clicking the button
Button(options_frame, text="CURRENT ARRAY", command=Generate_array, bg='Red',height=5).grid(row=1, column=3, padx=10, pady=10)

root.mainloop()