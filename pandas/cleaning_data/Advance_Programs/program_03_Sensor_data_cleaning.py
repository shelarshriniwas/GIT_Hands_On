#program_03_Sensor_data_cleaning.py

import pandas as pd
import numpy as np

sensor = pd.DataFrame({
    "Temperature":[
        25,
        np.nan,
        28
    ]
})

sensor["Temperature"] = (
    sensor["Temperature"]
    .interpolate()
)

print(sensor)