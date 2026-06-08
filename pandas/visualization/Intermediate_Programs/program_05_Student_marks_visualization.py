#program_05_Student_marks_visualization.py

import pandas as pd

df = pd.DataFrame({
    "Student":["A","B","C"],
    "Marks":[80,70,90]
})

df.plot(
    x="Student",
    y="Marks",
    kind="bar"
)

plt.show()