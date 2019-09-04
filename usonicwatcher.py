
import usensor_simul
import time
import datetime
import smtplib


class USonicWatcher:

    #I did not used SendMail class instead only a function 
    #When you initialize you put your email & password 
    #Status is just a string. 
    def __init__(self, username, password,status="OK"):
        # OK / Alarm
        
        self.status = status 
        self.username = username
        self.password = password
        

    def saveTargetDistance(self, infofile):
      
        self.dist = usensor_simul.distance(18, 24)
        self.F = open(infofile, "w")
        self.F.write(str(self.dist))
        self.F.close()

    def loadTargetDistance(self, infofile):
      
        self.LF = open(infofile, "r")
        self.info = self.LF.read()
        self.LF.close()
        return self.info


    #I added info file as a parameter :D I hope i Did not violate anything
    def ExecuteAlarmLoop(self, alarmFile, thresholdtime, targetemail, infofile):        

        self.iFile = open(infofile, "r")
        self.okDistance = self.iFile.read
        self.iFile.close()

        try:
            while True:
                self.currentD = usensor_simul.distance(18, 24)
                if self.sagnificantChange(self.okDistance, self.currentD):
                    self.status = 'ALARM'
                    self.startTime = time.time()
                else:
                    self.status = 'OK'
                    self.endTime = time.time()

                if self.status =='ALARM' and (self.endTime-self.startTime) > (thresholdtime*2):                                
                    self.aFile = open(alarmFile, "a")
                    self.aFile.write(datetime.datetime.now())
                    self.send_email("Warning about recent events!",self.username, self.password, "There is a potential unwanted activities on your door, check ASAP!",targetemail)
                    self.aFile.close()
                time.sleep(0.5)

               

        # Reset by pressing CTRL + C
        except KeyboardInterrupt:
            print("Stopped by User")

    def ExecuteMonitoringLoop(self, thresholdtime, monitoringFile):
    
        self.numberOfPersons = 0
        
        try:
            while True:
                currentD = usensor_simul.distance(18, 24)
                if self.sagnificantChange(self.okDistance, currentD):
                    self.status = 'ALARM'
                    self.startTime = time.time()
                else:
                    self.status = 'OK'
                    self.endTime = time.time()

                if (self.status =='ALARM' and (self.endTime-self.startTime) > thresholdtime*2):
                                
                    self.mFile = open(monitoringFile, "a")
                    self.mFile.write(datetime.datetime.now())
                    self.numberOfPersons = self.numberOfPersons+1
                    self.mFile.close()
                time.sleep(0.5)

        # Reset by pressing CTRL + C
        except KeyboardInterrupt:
            print("Stopped by User")
            print("Number of persons activating an alarm: " + self.numberOfPersons)

    


    def send_email(self,subject, username, password, msg,yourMail, targetemail):
        try:
	        self.server = smtplib.SMTP('smtp.gmail.com:587')
            self.server.ehlo()
	        self.server.starttls()
            self.server.login(username, password)
	        self.message = 'Subject: {}\n\n{}'.format(subject, msg)
	        self.server.sendmail(yourMail, targetemail, message)
            self.server.quit()
	        print("Successfully sent an email")
        except:
            print("Failed to send an email")
  

    def sagnificantChange(self, okDistance, currentDistance):
        #Significant change I used that if its bigger than 1.5 times of the ok
        if currentDistance > (okDistance * 1.5):
            return True
        else:
            return False


