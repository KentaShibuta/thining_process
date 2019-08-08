import pandas as pd
import matplotlib.pyplot as plt

num_lines = 0
num_lines =len(open('20190808113210.csv').readlines())
print(num_lines)

df = pd.read_csv('20190808113210.csv', header=None)
df_1 = pd.DataFrame(df)
df_1.columns = ['t', 'a', 'b', 'c', 'interface_right_displacement']
print(df_1)
df_1.plot.line(x='t', y='interface_right_displacement')
#plt.plot([df['t'],df['4']])
plt.show()
