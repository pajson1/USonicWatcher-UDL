import sys
import usonicwatcher

if __name__ == '__main__':

# Test Program
# Once you have your USonicWatcher class implemented, use it in a
# test program, named test-usonicwatcher.py with five arguments:
# 1. alarmFile: The name of the alarm file to use in alarm mode.
# 2. thresholdtime: The value for the thresholdtime parameter.
# 3. targetemail: The name of the target email to use for alarm messages.
# 4. monitoringFile: The name of the monitoring file to use in monitoring mode.
# 5. watchmode: An integer that may be either "1" (to enter alarm
# mode) or "2" (to enter monitoring mode).

    usonicwatcher.alarmFile = sys.argv[0]
    usonicwatcher.thresholdtime = sys.argv[1]
    usonicwatcher.targetemail = sys.argv[2]
    usonicwatcher.monitoringFile = sys.argv[3]
    watchmode = sys.argv[4]

#     Then, create an object of the USonicWatcher class, and execute either
# the alarm mode or the monitoring mode, depending on the value of
# the watchmode parameter


    USObject = usonicwatcher.USonicWatcher("","","")

    

    USObject.saveTargetDistance("")

    
    
    if (watchmode == 1):
        USObject.ExecuteAlarmLoop(sys.argv[0],sys.argv[1],sys.argv[2],"")
    elif (watchmode == 2):
        USObject.ExecuteMonitoringLoop(sys.argv[1],sys.argv[3])
