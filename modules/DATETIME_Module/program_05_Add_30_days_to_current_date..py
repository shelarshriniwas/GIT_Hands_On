# Add 30 days to current date.

from datetime import datetime, timedelta

today = datetime.now()

future_date = today + timedelta(days=30)

print("Future Date :", future_date)