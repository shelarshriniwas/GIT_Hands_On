#program_06_Real-time_file_monitoring.py

import pandas as pd
import time

while True:
    df = pd.read_csv(
        "live_data.csv"
    )

    print(df.tail())

    time.sleep(5)