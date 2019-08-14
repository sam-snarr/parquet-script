import os
import pandas as pd 


dirpath = os.path.dirname(os.path.realpath(__file__))
print(os.listdir(dirpath))

# gets full path of all files in same directory as script if it contains keywords 'apptopia' or 'mighty'
onlyfiles = [os.path.join(dirpath, f) for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f)) and f != os.path.basename(__file__)]

list_df = []

c=0
for i in onlyfiles:
	print(c, len(onlyfiles))
	c+=1

	list_df.append(pd.read_parquet(i, engine='pyarrow')) # note you will need to pip install pyarrow, other engines will work also

total_df = pd.concat(list_df)
total_df.to_csv('total_data.csv')
input('enter to exit...')
