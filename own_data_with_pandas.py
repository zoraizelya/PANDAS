#import librarires first
from matplotlib import style
import pandas as pd
# chilla = pd.read_csv("data_chilla.csv")
# print(chilla)
chilla2 = pd.read_csv("data_sheet.csv")
print(chilla2)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes=True)
# p=sns.countplot(x="Employee Markme", hue="Leave",data=chilla)
p=sns.countplot(x="Subscribers", hue="username",data=chilla2)
plt.show()
