'''
5 Number Summary:
                    Min, max, median, Q1, Q3, IQR
'''

import numpy as np
import pandas as pd

lst_marks = [45, 32, 56, 75, 89, 90, 87, 67, 54, 45, 98, 99, 67, 74]
min, q1, median, q3, max = np.quantile(lst_marks, [0, 0.25, 0.50, 0.75, 1])
print((min, q1, median, q3, max))

IQR = q3 - q1
print(IQR)

lower_fence = q1 - 1.5 * (IQR)
higher_fence = q1 + 1.5 * (IQR)

import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(lst_marks)
plt.show()

####################################################################################################################

lst_marks_with_outliers = [2, 1, 3, 14, 45, 32, 56, 75, 89, 90, 87, 67, 54, 45, 98, 99, 67, 74, 150, 159, 170]
sns.boxplot(lst_marks_with_outliers)
plt.show()
