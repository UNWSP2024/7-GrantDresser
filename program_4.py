# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 

# Program 4: Distance between two 3D points stored as tuples

##
# Program 4: Coordinates
# Grant Dresser 
# 10/17/2025
##

import math
from typing import Tuple

Point3D = Tuple[float, float, float]

def distance3d(p1: Point3D, p2: Point3D) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def parse_point(prompt: str) -> Point3D:
    """Accepts input like: 1, 2.5, -3  (commas optional, spaces ok)."""
    while True:
        try:
            text = input(prompt).replace(",", " ")
            parts = [p for p in text.split() if p]
            if len(parts) != 3:
                raise ValueError("Please provide exactly three numbers.")
            x, y, z = map(float, parts)
            return (x, y, z)
        except ValueError as e:
            print(f"Invalid point: {e}")

def main():
    try:
        p1 = parse_point("Enter point 1 (x,y,z): ")
        p2 = parse_point("Enter point 2 (x,y,z): ")
        d = distance3d(p1, p2)
        print(f"Distance between {p1} and {p2} is {d:.6f}")
    except Exception as e:
       
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
