# import random
# import csv
#
# with open("input.csv", "w", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Компанія 1", "Компанія 2", "Компанія 3"])
#     for i in range(100):
#         writer.writerow([random.randint(200, 10000) for j in range(3)])

import pandas as pd

dataframe = pd.read_csv("input.csv", sep=",", encoding="utf-8")
s1 = dataframe.sum(0)

print(s1)

