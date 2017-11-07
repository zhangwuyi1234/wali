
import urllib.request as request  
import datetime  
import time 

def getFrstday(today):
    if today==None:
        today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday  
    return yesterday  

def getNextday(today):
    if today==None:
        today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today+oneday  
    return yesterday  

def get_day_type(query_date):  
    url = 'http://tool.bitefu.net/jiari/?d=' + query_date  
    resp = request.urlopen(url)  
    content = resp.read()  
    if content:  
        try:  
            day_type = int(content)  
        except ValueError:  
            return -1  
        else:  
            return day_type  
    else:  
        return -1  
  
  
def is_tradeday(query_date):  
    weekday = datetime.datetime.strptime(query_date, '%Y%m%d').isoweekday()  
    if weekday <= 5 and get_day_type(query_date) == 0:  
        return 1  
    else:  
        return 0  
  
  
def today_is_tradeday():  
    query_date = datetime.datetime.strftime(datetime.datetime.today(), '%Y%m%d')  
    return is_tradeday(query_date)  

def dealDayFrst(endTime):
    times=getFrstday(endTime)
    end=times.strftime('%Y%m%d')
    istra=is_tradeday(end)
    if istra==1:
        return times
    return dealDayFrst(times)

def dealDay(endTime):
    times=getNextday(endTime)
    end=times.strftime('%Y%m%d')
    istra=is_tradeday(end)
    if istra==1:
        return times
    return dealDay(times)
  
def getTimeForFrst(ins,endTime):
    stime = datetime.datetime.strptime(endTime,'%Y%m%d')
    for i in range(ins):        
        stime=dealDayFrst(stime)
        end=stime.strftime('%Y%m%d')
    return end


def getTimeForEnd(ins,endTime):
    stime = datetime.datetime.strptime(endTime,'%Y%m%d')
    for i in range(ins):        
        stime=dealDay(stime)
        end=stime.strftime('%Y%m%d')
    return end


if __name__ == "__main__":
    times=getTimeForEnd(4,"20170423")
    print(times)
    times=getTimeForFrst(4,"20170423")
    print(times)
