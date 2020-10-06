

#CODE-BEGINS
print('''
==========================================================
THIS PROGRAM CALCULATES THE A/C's REQUIRED RATE OF DESCENT
==========================================================
''')

import math
def rate_of_descent(ias, ang):
    calc = (ias * 1 / 60) * 6080 * ang
    return calc

angle = input("Enter the APPROACH ANGLE in degrees: ")
speed = input("Enter the AIRCRAFT SPEED in IAS: ")
conv_tan = math.radians(float(angle))
fin_calc = rate_of_descent(float(speed), float(conv_tan))
add = " FPM is your required ROD"
add2 = int(fin_calc)
print("---------------------------------------")
print(str(add2) + str(add))
print("---------------------------------------")

input('''
Press ENTER to EXIT the program
''')
#CODE-ENDS