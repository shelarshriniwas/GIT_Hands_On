# Subtract 10 days from date.

from datetime import datetime, timedelta

today = datetime.now()

past_date = today - timedelta(days=10)

print("Past Date :", past_date)