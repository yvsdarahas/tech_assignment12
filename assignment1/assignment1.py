import pickle as pk
import pandas as pd

# Converted TestResults.pickle to .csv format
with open("./TestResults.pickle", "rb") as f:
    object = pk.load(f)

df = pd.DataFrame(object)
df.to_csv('TestResults.csv', index=False)

# Merged info and the results for clear view
info = pd.read_csv('./TestInfo.csv')
results = pd.read_csv('./TestResults.csv')

merged = pd.merge(info, results, on='TestId', how='inner')

# Sorted based in Speed (Time)
print('Based on Time \n\n')
merged = merged.sort_values(by=['Time (ms)'], ascending=True)
print(merged)

# For better performance
# 1. High CPU frequency
# 2. More threads (Common)
# 3. Less Execution time
# 4. Less Peak memory
