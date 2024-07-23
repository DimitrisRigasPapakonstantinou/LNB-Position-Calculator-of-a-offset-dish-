#https://www.satsig.net/pointing/finding-dish-offset-angle.htm
#https://ftapinamar.blogspot.com/2012/05/el-foco-en-antenas-offset.html?showComment=1429781145918


import math
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import os

def round_number(number, n):
    return round(number * 10**n) / 10**n

def computeform(sideways, vertical, depth):
    width = sideways
    height = vertical

    offsetangle = math.acos(sideways / vertical) * 180 / math.pi
    focallength = sideways ** 3 / (16 * depth * vertical)
    DistF = focallength
    a = 2 * DistF * math.sqrt((height / 2 / (width / 2))**2 - 1)
    topdistanced1 = (a + width / 2)**2 / (4 * DistF) + DistF
    bottomdistanced2 = (a - width / 2)**2 / (4 * DistF) + DistF
    fdratio = focallength / sideways

    return {
        'focallength': round_number(focallength, 4),
        'topdistanced1': round_number(topdistanced1, 4),
        'bottomdistanced2': round_number(bottomdistanced2, 4),
        'offsetangle': round_number(offsetangle, 4),
        'fdratio': round_number(fdratio, 4)
    }

def on_compute():
    sideways = float(sideways_entry.get())
    vertical = float(vertical_entry.get())
    depth = float(depth_entry.get())
    #method = float(method_entry.get())

    results = computeform(sideways, vertical, depth)
    
    focallength_var.set(results['focallength'])
    topdistanced1_var.set(results['topdistanced1'])
    bottomdistanced2_var.set(results['bottomdistanced2'])
    offsetangle_var.set(results['offsetangle'])
    fdratio_var.set(results['fdratio'])

root = tk.Tk()
root.title("Compute LNB Point on an Offset Parabolic Mirror")


# Input fields
tk.Label(root, text="Horizontal:").grid(row=0, column=0, padx=5, pady=5)
sideways_entry = tk.Entry(root)
sideways_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Vertical:").grid(row=1, column=0, padx=5, pady=5)
vertical_entry = tk.Entry(root)
vertical_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Depth:").grid(row=2, column=0, padx=5, pady=5)
depth_entry = tk.Entry(root)
depth_entry.grid(row=2, column=1, padx=5, pady=5)

# tk.Label(root, text="Method:").grid(row=3, column=0, padx=5, pady=5)
# method_entry = tk.Entry(root)
# method_entry.grid(row=3, column=1, padx=5, pady=5)

# Output fields
focallength_var = tk.StringVar()
topdistanced1_var = tk.StringVar()
bottomdistanced2_var = tk.StringVar()
offsetangle_var = tk.StringVar()
fdratio_var = tk.StringVar()

tk.Label(root, text="Focal Length:").grid(row=4, column=0, padx=5, pady=5)
tk.Label(root, textvariable=focallength_var).grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Top Distance D1:").grid(row=5, column=0, padx=5, pady=5)
tk.Label(root, textvariable=topdistanced1_var).grid(row=5, column=1, padx=5, pady=5)

tk.Label(root, text="Bottom Distance D2:").grid(row=6, column=0, padx=5, pady=5)
tk.Label(root, textvariable=bottomdistanced2_var).grid(row=6, column=1, padx=5, pady=5)

tk.Label(root, text="Offset Angle:").grid(row=7, column=0, padx=5, pady=5)
tk.Label(root, textvariable=offsetangle_var).grid(row=7, column=1, padx=5, pady=5)

tk.Label(root, text="FD Ratio:").grid(row=8, column=0, padx=5, pady=5)
tk.Label(root, textvariable=fdratio_var).grid(row=8, column=1, padx=5, pady=5)


tk.Label(root, text="Equations and photo from: www.satsig.net , ftapinamar.blogspot.com ").grid(row=9, column=0, padx=5, pady=5)


# Compute button
compute_button = tk.Button(root, text="Compute", command=on_compute)
compute_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

image_path = os.path.join(os.path.dirname(__file__), "explanation.png")
image = PhotoImage(file= image_path)
image_label = tk.Label(root, image=image)
image_label.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()