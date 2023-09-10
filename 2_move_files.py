import glob
import os
import shutil

""" this scripts moves data files in their respective subfolders. This is mainly due to
the fact that IPEDS publishes revised files along with older files so they need to be 
separated.
"""

xlsx = glob.glob(r"./unzipped/*.xlsx")
xls = glob.glob(r"./unzipped/*.xls")

# let's move data files and data dictionaries
os.makedirs(r"./unzipped/production/")

# the files in this folder were revised, not to be used.
os.makedirs(r"./unzipped/old/")

for file in xlsx:
    csv_original = file.replace(".xlsx", ".csv")
    csv_revised = file.replace(".xlsx", "_rv.csv")

    shutil.move(file, r"./unzipped/production/")

    if os.path.isfile(csv_revised):
        shutil.move(csv_revised, r"./unzipped/production/")
    else:
        shutil.move(csv_original, r"./unzipped/production/")

    if os.path.isfile(csv_original):
        shutil.move(csv_original, r"./unzipped/old/")


for file in xls:
    csv_original = file.replace(".xls", ".csv")
    csv_revised = file.replace(".xls", "_rv.csv")

    shutil.move(file, r"./unzipped/production/")

    if os.path.isfile(csv_revised):
        shutil.move(csv_revised, r"./unzipped/production/")
    else:
        shutil.move(csv_original, r"./unzipped/production/")

    if os.path.isfile(csv_original):
        shutil.move(csv_original, r"./unzipped/old/")