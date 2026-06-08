#program_04_Real-time_monitoring_chart.py

import pandas as pd
import matplotlib.pyplot as plt
import time

for i in range(5):

    plt.clf()

    plt.plot(
        np.random.randint(
            1,
            100,
            10
        )
    )

    plt.pause(1)

plt.show()