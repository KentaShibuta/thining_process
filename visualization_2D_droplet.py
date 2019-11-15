import pandas as pd
import matplotlib.pyplot as plt
# write file name
df = pd.read_csv('20191116004307.csv',header=None)
pd.DataFrame(df)
df.columns = ['t','x', 'y','z', 'non']
plt.xlabel('x')
plt.ylabel('y')
plt.title('visualization mesh')
plt.scatter(df['x'],df['y'])#ここを入れると節点が強調して表示される．
plt.show()
