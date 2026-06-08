#program_04_Histogram.py

import pandas as pd
import matplotlib.pyplot as plt

marks = [50,60,70,80,90,95]

plt.hist(marks, bins=5)

plt.show()