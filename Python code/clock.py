#Gabriel Harrison
#9/21/2018
#Time sorter

#import time and calendar
import time
import calendar

#define the midnight time of January 1, 1970
def gmtnow():
    #1 calculate total for milli, second, minute, hour
    seconds=calendar.timegm(time.gmtime())
    current_second=seconds % 60
    minutes=seconds//60
    current_minute=minutes % 60
    hours=minutes//60
    current_hour= hours % 24
    return current_hour, current_minute, current_second
x=True
while x==True:
    h,m,s=gmtnow()
    print(h,":",m,":",s)
    
    
    
    

