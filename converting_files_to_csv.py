# from pdf2image import convert_from_path
import os 

walk_dir = './results'
print("Converting from ", walk_dir)

all_files = []
file_names = []
for root, dirs, files in os.walk(walk_dir):
    for f in files:
        all_files.append(os.path.join(root, f))
        file_names.append(f.split('.')[0])
    break

# print(all_files)
# print(file_names)

import pandas as pd

df1 = pd.DataFrame()

# print(df1, "initialised.")

for i,j  in zip(all_files, file_names):
    try:
        with open(i, 'r') as read_file:
            # print(j)
            content = read_file.readlines()
            # print(content)
            new_df1 = pd.DataFrame({'name':j, 'content':"\n".join(content)}, index=[0])
            # print('\n', new_df1)
            df1 = df1.append(new_df1)
            # print(df1)
    except Exception as e:
        print(e)

print(df1)

df1.to_csv(walk_dir+".csv")


