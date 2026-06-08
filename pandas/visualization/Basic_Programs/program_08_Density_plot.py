#program_08_Density_plot.py

import pandas as pd

df = pd.DataFrame({
    "Marks":[50,60,70,80,90]
})

df["Marks"].plot(
    kind="density"
)