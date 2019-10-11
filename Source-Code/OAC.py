"""Other Apparatus Calculator - calculates the tension in two cables of a custom apparatus"""

import math
import numpy

num = numpy


def tension_calc():
    # Asks for mass of object from the user
    mass = ((float(input("Object Mass (g): ")))/1000)*9.8

    # Measurements defined between the various points during group meeting
    m1 = int(input("Left-to-Middle Measurement (cm): "))
    m2 = int(input("Middle-to-Right Measurement (cm): "))

    # Defined height from top of apparatus to top of mass
    m3 = int(input("Height between top of apparatus and object (cm): "))

    # Calculates the Angles between the strings based on the provided measurements
    angleA = math.atan(m3 / m1)
    angleB = math.atan(m3 / m2)

    # Sets up the matrices for multiplication to find the tension in each cable
    matrix1 = num.linalg.inv([[math.cos(angleB), -math.cos(angleA)], [math.sin(angleB), math.sin(angleA)]])
    matrix2 = [0, mass]

    # Matrix multiplication to find the tension
    AnswerMatrix = num.dot(matrix1, matrix2)

    # Prints out answers from final matrix
    print("\nTension of Cable A: " + "%.2f" % AnswerMatrix[0] + " N")
    print("\nTension of Cable B: " + "%.2f" % (AnswerMatrix[1]) + " N")

    close = input("\nPress Enter to Exit Program")

# If program is executed, the code above runs
if __name__ == "__main__":
    tension_calc()
