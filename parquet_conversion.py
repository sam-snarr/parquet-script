
import os
import pandas as pd 

# gets directory that the script is in
dirpath = os.path.dirname(os.path.realpath(__file__))

# gets full path of all files in same directory except the python script
onlyfiles = [os.path.join(dirpath, f) for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f)) and f != os.path.basename(__file__)]

list_df = []

c=0
num_files = len(onlyfiles)

# loops through all the files and appends them in dataframe form to list
for i in onlyfiles:
	list_df.append(pd.read_parquet(i, engine='pyarrow')) # note you will need to pip install pyarrow, other engines will also work

	print(c, num_files)
	c+=1

# concatenates all the dataframes together
total_df = pd.concat(list_df)

# writes to final csv for upload into kepler.gl
total_df.to_csv('total_data.csv')

input('enter to exit...')
