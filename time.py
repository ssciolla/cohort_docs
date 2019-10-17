from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
print("The current time is {}:{}".format(hour, minute))