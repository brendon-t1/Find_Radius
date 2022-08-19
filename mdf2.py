def volumeCircle(radius, height):
    volume = 3.14159 * (radius * radius) * height
    return volume

def radiusForWeight(weight=5, height=.75):
    # weight of mdf per cubic inch and the value of pi
    mdf = .028
    pi = 3.14159

    # volume of the .5" radius hole to be removed
    hole_volume = volumeCircle(.5, .75)

    # weight of hole and total weight needed to account for hole removal
    hole_weight = hole_volume * mdf
    total_weight = weight + hole_weight

    #calc cubic inches needed for weight
    cubic_inches = total_weight / mdf
    print(cubic_inches)
    
    #circle_radius = sqrt(cubic_inches / 3.14159 * .75)
    circle_radius = (cubic_inches / (pi * height)) **.5
    #circle_radius = squared_circle_radius**.5
    circle_radius_rounded = round(circle_radius, 2)
    
    return circle_radius_rounded

print(radiusForWeight())
