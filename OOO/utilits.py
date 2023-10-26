from datetime import datetime, timedelta
from pytz import timezone

current_datetime = datetime.now()

print(current_datetime.strftime("%d-%m-%Y %H:%M:%S %p"))

time_after_7_days = current_datetime + timedelta(days=5.5)
print(time_after_7_days)

# default_timezone = timezone("America/New_York")
default_timezone = timezone("utc")
print(datetime.now(default_timezone))
