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
# merged = merged.sort_values(
#     by=['Time (ms)'], ascending=True, ignore_index=True)

# merged = merged.sort_values(
#     by=['PeakMemory (MB)'], ascending=True, ignore_index=True)

merged = merged.sort_values(
    by=['Build', 'Threads', 'MLNetwork'], ascending=True, ignore_index=True)
print(merged.tail(20))
