import pandas as pd
import matplotlib.pyplot as plt
print("input filename >>>")
file_name = input().strip()

print("input filename_2 >>>")
file_name_2 = input().strip()

num_lines = 0
num_lines =len(open(file_name).readlines())
print(num_lines)

df_1 = pd.read_csv(file_name, header=None)
df_1 = pd.DataFrame(df_1)
df_1.columns = ['time', 'x', 'y']
print(df_1)

df_2 = pd.read_csv(file_name_2, header=None)
df_2 = pd.DataFrame(df_2)
df_2.columns = ['time', 'x', 'y']
print(df_2)

plt.xlabel('x')
plt.ylabel('y')

plt.plot(df_1['time'], df_1['y'], label="Y coordinate 100:100:100")
plt.plot(df_2['time'], df_2['y'], label="Y coordinate 6:10:10")
plt.legend()
plt.show()
