import os
import subprocess

# install_command = "pip install ipynb-py-convert" - to musisz wpisa w pole poniej na bialo (w tzw command line)
# subprocess.Popen(install_command, shell=True)

current_dicrectory = os.getcwd()
all_files = os.listdir(current_dicrectory)

ipynb_files = []
for filename in all_files:
    if filename.endswith("ipynb"):
        ipynb_files.append(filename)


for filename in ipynb_files:
    old_file = f"{current_dicrectory}/{filename}"
    new_file = f"{current_dicrectory}/{filename}".replace("ipynb", "py")

    command = f"ipynb-py-convert {old_file} {new_file}"

    subprocess.Popen(command, shell=True)


