from tkinter import *

root = Tk()
root.title("Weight Training Equipment Developer")

def volumeCircle(radius, height):
    volume = 3.14159 * (radius * radius) * height
    return volume

def radiusForWeight(weight=5.0, height=.75, material=.028):
    # weight of mdf per cubic inch and the value of pi
    #mdf = .028
    pi = 3.14159

    # volume of the .5" radius hole to be removed
    hole_volume = volumeCircle(.5, height)

    # weight of hole and total weight needed to account for hole removal
    hole_weight = hole_volume * material
    total_weight = weight + hole_weight

    #calc cubic inches needed for weight
    cubic_inches = total_weight / material
    
    # calc radius
    circle_radius = (cubic_inches / (pi * height)) **.5
    circle_radius_rounded = round(circle_radius, 2)
    
    return circle_radius_rounded

# this function will take the input from the entry boxes and
# compute the answer
def run():
    answer_box.delete(0, END)
    weight = weight_entry.get()
    thickness = thickness_entry.get()
    density = material_density_entry.get()
    answer = radiusForWeight(float(weight), float(thickness), float(density))
    answer_box.insert(0, answer)


#answer box
answer_box = Entry(root, width=33, borderwidth=2)
answer_box.grid(row=0, column=0, columnspan=3)

#entry box for weight default is 5
weight_entry = Entry(root, width=10, borderwidth=2)
weight_entry.grid(row=1, column=0)
#entry box for thickness default is .75
thickness_entry = Entry(root, width=10, borderwidth=2)
thickness_entry.grid(row=1, column=1)
#entry box for material default is mdf
material_density_entry = Entry(root, width=10, borderwidth=2)
material_density_entry.grid(row=1, column=2)

#button to push to run the program
button_run = Button(root, text="Run", command=run)
button_run.grid(row=2, column=1)

root.mainloop()