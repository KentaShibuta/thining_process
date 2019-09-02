import pandas as pd
import matplotlib.pyplot as plt
print("input filename >>>")
file_name = input().strip()
num_lines = 0
num_lines =len(open(file_name).readlines())
print(num_lines)

df = pd.read_csv(file_name, header=None)
df_1 = pd.DataFrame(df)
df_1.columns = ['time', 'a', 'Y coordinate of the bottom edge of the droplet']
print(df_1)
df_1.plot.line(x='time', y='Y coordinate of the bottom edge of the droplet')
plt.show()
