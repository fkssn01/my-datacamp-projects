
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

crimes = pd.read_csv("crimes.csv", dtype={"TIME OCC": str})
crimes.head()



crimes["HOUR OCC"] = crimes["TIME OCC"].str[:2].astype(int)


crimes.head()

sns.countplot(data=crimes, x="HOUR OCC")
plt.show()


peak_crime_hour = 12



night_time = crimes[crimes["HOUR OCC"].isin([22,23,0,1,2,3])]

peak_night_crime_location = night_time.groupby("AREA NAME", 
                                               as_index=False)["HOUR OCC"].count().sort_values("HOUR OCC",
                                                                                               ascending=False).iloc[0]["AREA NAME"]

print(f"The area with the largest volume of night crime is {peak_night_crime_location}")

age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]


crimes["Age Bracket"] = pd.cut(crimes["Vict Age"],
                               bins=age_bins,
                               labels=age_labels)


victim_ages = crimes["Age Bracket"].value_counts()
print(victim_ages)