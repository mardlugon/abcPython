import os
from pprint import pprint

current_dicrectory = os.getcwd()
print(current_dicrectory)

all_files = os.listdir(current_dicrectory + "/4.Thursday")
# print(all_files)

extentions = ["py", "ipynb"]
filtered_filed = []
for filename in all_files:
    if filename.endswith(extentions[0]) or  filename.endswith(extentions[1]):
        filtered_filed.append(filename)

filtered_fild = sorted(filtered_filed)
print(filtered_filed)

files_to_rename = []
for filename in filtered_filed:
    if filename[1] =="." and filename[0].isnumeric():
        files_to_rename.append(filename)
print(files_to_rename)

for filename in files_to_rename:
    os.rename(f"C:\\Users\\training\\Desktop\\Python Marcin\\4.Thursday\\{filename}", f"C:\\Users\\training\\Desktop\\Python Marcin\\4.Thursday\\0{filename}")

# os.rename("C:\\Users\\training\\Desktop\\Python Marcin\\4.Thursday\\10.curency 01.py", "C:\\Users\\training\\Desktop\\Python Marcin\\4.Thursday\\10.curency 01 renamed.py")