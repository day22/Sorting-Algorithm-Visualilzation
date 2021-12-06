from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from mergeSort import merge_sort
from insertionSort import insertion_sort
from bogoSort import bogo_sort
from cocktailSort import cocktail_sort

# create GUI window
root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(1800, 1200)
root.config(bg='black')

# Global Variables
selected_alg = StringVar()
data = []

# input: array for numbers and an array of color values for each number
# summary: draws data as rectangles onto the canvas with corresponding colors from colorArray


def drawData(data, colorArray):
    # clear canvas
    canvas.delete("all")

    # canvas dimensions
    c_height = 760
    c_width = 1200
    x_width = c_width / (len(data) + 1)

    # bar spacing
    offset = 30
    spacing = 5

    # normalize data
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        # calculate rectangle coordinates
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 760
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        # draw rectangle
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
    # update canvas
    root.update_idletasks()

# creates new random set of data specific to user selected parameters


def Generate():
    global data

    # read user selected values
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    # clear existing data
    data = []
    for _ in range(size):
        # add random number to data
        data.append(random.randrange(minVal, maxVal+1))

    # draw new data to canvas
    drawData(data, ['red' for x in range(len(data))])

# runs selected algorithm


def StartAlgorithm():
    global data
    if not data:
        return

    # run selected algorithm
    if algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())
    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())
    elif algMenu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, speedScale.get())
    elif algMenu.get() == 'Bogo Sort':
        bogo_sort(data, drawData, speedScale.get())
    elif algMenu.get() == 'Cocktail Sort':
        cocktail_sort(data, drawData, speedScale.get())

    # draw now sorted data all green
    drawData(data, ['green' for x in range(len(data))])


# frame to hold sliders and combobox for user to interface
UI_frame = Frame(root, width=200, height=600, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=10)

# canvas to display sorting
canvas = Canvas(root, width=1200, height=760, bg='white')
canvas.grid(row=0, column=1, padx=10, pady=10)

# user interface


# algorithm label and combobox
Label(UI_frame, text="Algorithm: ", bg='grey').grid(
    row=0, column=0, padx=5, pady=5, sticky=W)

algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=[
                       'Bubble Sort', 'Merge Sort', 'Insertion Sort', 'Bogo Sort', 'Cocktail Sort'])
algMenu.grid(row=2, column=0, padx=5, pady=5)
algMenu.current(0)

# scale for selecting what speed animation runs at
speedScale = Scale(UI_frame, from_=0.01, to=2.0, length=100, digits=2,
                   resolution=0.01, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=3, column=0, padx=5, pady=5)

# Sliders for random data parameters
sizeEntry = Scale(UI_frame, from_=3, to=30, resolution=1,
                  orient=HORIZONTAL, label="Select Size")
sizeEntry.grid(row=4, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1,
                 orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=5, column=0, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1,
                 orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=6, column=0, padx=5, pady=5)

# Generate data and Start algorithm buttons
Button(UI_frame, text="Start", command=StartAlgorithm,
       bg='red').grid(row=7, column=1, padx=5, pady=5)
Button(UI_frame, text="Generate", command=Generate,
       bg='white').grid(row=7, column=0, padx=5, pady=5)


root.mainloop()
