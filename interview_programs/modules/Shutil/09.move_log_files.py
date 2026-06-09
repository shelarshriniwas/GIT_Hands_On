

import os
import shutil

for file in os.listdir("Logs"):

    if file.endswith(".log"):
        shutil.move(
            os.path.join("Logs", file),
            "Archive"
        )

print("All log files moved successfully")