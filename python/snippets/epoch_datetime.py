
# Convert string to epoch time
from datetime import datetime
import time
d = '20191001232054'
d=d[2:]
print(d)
d = d[:2]+'/'+d[2:4] +'/'+d[4:6]+' '+d[6:8]+':'+d[8:10]+':'+d[10:] 
print(d)

datetime_object = datetime.strptime(d, '%y/%m/%d %H:%M:%S')
currentTime=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.00Z")

print(type(datetime.now()))
print(type(datetime_object))
print(int(datetime_object.timestamp()))


#Python 2.7
datetime_object=time.mktime(datetime_object.timetuple())