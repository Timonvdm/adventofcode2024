import pandas as pd
import numpy as np

df = pd.read_csv('input.txt', sep='\s+')
df = pd.DataFrame(np.sort(df.values, axis=0), index=df.index, columns=df.columns)

#Calculate distance (part one)
sum = 0
for index, row in df.iterrows():
    sum += abs(row['a'] - row['b'])

print(f"Total distance part 1: {sum}")

#Calculate similarity (part two)
similarity = 0
for index, row in df.iterrows():
    occurences = df['b'].value_counts().get(row['a'], 0)
    if occurences > 0:
        similarity += row['a'] * occurences

print(f"Similarity part 2: {sum}")
