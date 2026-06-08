#program_03_Log_file_analyzer.py

import pandas as pd

logs = pd.read_csv("server_logs.csv")

error_logs = logs[
    logs["Status"] == "ERROR"
]

print(error_logs)