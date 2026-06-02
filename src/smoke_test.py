from datetime import date
import pandas as pd
import numpy as np

print("Environment working!")
print("Today's date:", date.today())

data = pd.DataFrame({
    "Temperature": [24, 25, 26],
    "Humidity": [80, 75, 78]
})

print(data)