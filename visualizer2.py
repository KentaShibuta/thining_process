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
df_1.columns = ['time', 'a', 'b', 'c', 'interface_right_displacement']
print(df_1)

df_2 = pd.read_csv(file_name_2, header=None)
df_2 = pd.DataFrame(df_2)
df_2.columns = ['time', 'a', 'b', 'c', 'interface_right_displacement_2']
print(df_2)

plt.plot(df_1['time'], df_1['interface_right_displacement'])
plt.plot(df_2['time'], df_2['interface_right_displacement_2'])
plt.show()
