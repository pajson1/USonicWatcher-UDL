# Use this module to get fake distance measures
# when you are not working in the RsPi with an
# ultrasonic sensor
import time
import random



# In this function, that has the same name as the "real" function
# in the RSPi, only the two first arguments are mandatory
#
# So, in your program, to use this function you must first
# use import:
#   import usensor_simul
# and then use the function in the same way you would use the real
# function (but with the prefix with the name of this module):
#
#   dist = usensor_simul.distance( GPIO_TRIGGER, GPIO_ECHO )
#
#  To simulate a "significant" change in the distance, use
#  a high value for the deviation parameter (e.g. 15 cm of deviation)
def distance( GPIO_TRIGGER, GPIO_ECHO, allow_deviation = False, good_distance = 34.0, deviation=0.2 ):

    if (allow_deviation):
      dist = random.uniform( good_distance - deviation, good_distance + deviation )
    else:
      dist = good_distance

    return dist

# This is only a test program. The distance function should
# be used from the program your own python file
#
if __name__ == '__main__':
    try:
        while True:
            dist = distance( 18, 24, True, deviation = 10.3 )
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
