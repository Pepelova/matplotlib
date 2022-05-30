import matplotlib.pyplot as plt
import pandas as pd

courses = pd.read_csv("udemy_courses.csv")

c_p = courses.loc[courses["is_paid"] == 1]
c_n_p = courses.loc[courses["is_paid"] == 0]

plt.axis([0, 3, 0, 1000])

plt.title('Lectures and content_duration')

cpmin = c_p['num_lectures'].min()
cpmax = c_p['num_lectures'].max()
cpmed = c_p['num_lectures'].median()
values1 = [cpmin, cpmed, cpmax]

cpmin_n = c_n_p['num_lectures'].min()
cpmax_n = c_n_p['num_lectures'].max()
cpmed_n = c_n_p['num_lectures'].median()
values2 = [cpmin_n, cpmed_n, cpmax_n]


cpmind = c_p['content_duration'].min()
cpmaxd = c_p['content_duration'].max()
cpmedd = c_p['content_duration'].median()
values3 = [cpmind, cpmedd, cpmaxd]

cpmind_n = c_n_p['content_duration'].min()
cpmaxd_n = c_n_p['content_duration'].max()
cpmedd_n = c_n_p['content_duration'].median()
values4 = [cpmind_n, cpmedd_n, cpmaxd_n]

index = ['Min', 'Med', 'Max']
B = 0.5
f1 = plt.bar(index, values1, B, color='g')
f2 = plt.bar(index, values2, B, color='r')
f3 = plt.bar(index, values3, B, color='y')
f4 = plt.bar(index, values4, B, color='b')
L1 = 'lectures of paid courses'
L2 = 'lectures of not paid courses'
L3 = 'content duration of paid courses'
L4 = 'content duration of not paid courses'
plt.legend((f1, f2, f3, f4), [L1, L2, L3, L4])
plt.show()
