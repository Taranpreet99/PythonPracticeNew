class MyTime:
    def __init__(self,hrs=0,mins=0, secs=0):
        
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return "{0}:{1}:{2}".format(self.hours,self.minutes,self.seconds)

    def __add__(self,other):
        return MyTime(0,0,self.to_seconds() + other.to_seconds())  

    def increment(self,seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
    
    #Return number of seconds represented by this instance
    def to_seconds(self):
        return self.hours*3600 + self.minutes*60 + self.seconds

    #After function to compare two times 
    def after(self,time2):
        return self.to_seconds() > time2.to_seconds()

def add_time(t1,t2):
        secs = t1.to_seconds() + t2.to_seconds()
        return MyTime(0,0,secs)

#Instantiate new object
tim1 = MyTime(11,59,30)

current_time = MyTime(9,14,30)
bread_time = MyTime(3,35,0)

current_time.increment(500)

