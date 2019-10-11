""" A control solution to verify the logic of the Team Apparatus Calculator, and the Other Apparatus Calculator"""

import math
import numpy

num = numpy


def tension_calc():
    # Calculates the weight of the object
    mass = 1600*9.8

    # Measurements defined between the various points during group meeting (cm)
    m1 = 110
    m2 = 40

    # Defined height from top of apparatus to top of mass
    m3 = 96

    # Calculates the Angles between the strings based on the provided measurements
    angleA = math.atan(m3/m1)
    angleB = math.atan(m3/m2)

    # Sets up the matrices for multiplication to find the tension in each cable
    matrix1 = num.linalg.inv([[math.cos(angleB), -math.cos(angleA)], [math.sin(angleB), math.sin(angleA)]])
    matrix2 = [0, mass]

    # Matrix multiplication to find the tension
    AnswerMatrix = num.dot(matrix1, matrix2)

    # Prints out answers from final matrix
    print("Tension of Cable A: " + "%.2f" % AnswerMatrix[0] + " N")
    print("Tension of Cable B: " + "%.2f" % AnswerMatrix[1] + " N")

    pause = input("\nHit Enter to Close Program")


# If program is executed, the code above runs
if __name__ == "__main__":
    tension_calc()
