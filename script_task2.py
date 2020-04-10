# Import argparse for command line automation processes

import time

# starting time
start = time.time()


import argparse





# Now, you should create a parser instance using ArgumentParser()
parser = argparse.ArgumentParser()

parser.add_argument("directory_path",
                    help="enter directory_path")
# Now, we will add a optional argument ( remember linux style )

# action :: --> behavior of script when using this option
# for example :: we are using here a "store_true" action, this tell the script that we well store a default
# true of false value and this default value is passed in the default argument
# dest :: the name of the attribute that will be used in the rest of our code
parser.add_argument("-u",action="store_true", dest="unixformat", default=False,help="maintain unix time format")

args = parser.parse_args()

import json
import re
import pandas as pd 
records = [json.loads(line) for line in open(args.directory_path)]
# Print the data frame
df = pd.DataFrame(records) 

df= df[['a', 'r','u','cy','ll','tz','t','hc']]
df = df.dropna()
df = df.reset_index(drop=True)


def get_browser(s):
    x=re.search("\w*/\d\.\d",str(s))
    if x:
        return x.group()
    else : 
        return None 

df['web_browser'] = df['a'].apply(get_browser)     



df['operating_sys']= df.a.str.extract(r'\(([^)]+)\)', expand=True)
df['operating_sys']= df.operating_sys.str.extract(r'^([\w\-]+)', expand=True)



#def get_os(s):
#    if s is not None:
#        e=str(s).split()
#        if len(e) > 1:
#            return e[1][1:].replace(";", "")
#        else:
#            return None

#df['operating_sys'] = df['a'].apply(get_os)


df['from_url']= df.r.str.extract(r'([\w_-]+(?:(?:\.[\w_-]+)+))', expand=True)

df['to_url']= df.u.str.extract(r'([\w_-]+(?:(?:\.[\w_-]+)+))', expand=True)

df['city'] = df['cy']




def get_longitude(s):
        e=str(s).replace('[','').split(', ')[0]
        return e

df['longitude'] = df['ll'].apply(get_longitude)


def get_latitude(s):
        e=str(s).replace(']','').split(', ')[1]
        return e

df['latitude'] = df['ll'].apply(get_latitude)







df['time_zone']=df['tz']


    
df['time_in']=df['t']


time_in = []
for i, row in df.iterrows():
    stamp = pd.to_datetime(row['time_in'], unit = 's').tz_localize(row['time_zone']).tz_convert('UTC')
    time_in.append(stamp)
    
df['time_in'] =time_in


df['time_out']=df['hc']   


time_out = []
for i, row in df.iterrows():
    stamp2 = pd.to_datetime(row['time_out'], unit = 's').tz_localize(row['time_zone']).tz_convert('UTC')
    time_out.append(stamp2)
    
df['time_out'] =time_out

    
    


#    print(x)  

#for x in df['time_zone']:
#        print(x)
            


    

if args.unixformat:
    df['time_in']=df['t']
    df['time_out']=df['hc']
    

#df.head(50)




df_final=df[['web_browser','operating_sys','from_url','to_url','city','longitude','latitude','time_zone','time_in','time_out']]
 
df_final = df_final.dropna()
df_final = df_final.reset_index(drop=True)




if args.directory_path=="/home/nourhan/Downloads/ITI_Python/task2/Task2/usa.gov_click_data_1.json" :
	target_file="/home/nourhan/Downloads/ITI_Python/task2/Task2/target/newfile1.csv"
elif args.directory_path=="/home/nourhan/Downloads/ITI_Python/task2/Task2/usa.gov_click_data_2.json" :
	target_file="/home/nourhan/Downloads/ITI_Python/task2/Task2/target/newfile2.csv"
else :
	target_file="/home/nourhan/Downloads/ITI_Python/task2/Task2/target/newfile3.csv"


   
df_final.to_csv (target_file, index = True, header=True)

#df_final.head(20)


print('done inshallaaaaa')

print('number of rows transformed',df_final.shape[0])
print('target file is',target_file)









checksums = {}
duplicates = []

# Import subprocess
from subprocess import PIPE, Popen
# Import os 
from os import listdir
# Get all files in the current directory
from os.path import isfile, join
files = [item for item in listdir('.') if isfile(join('.', item ))]

# Iterate over the list of files filenames
for filename in files:
    # Use Popen to call the md5sum utility
    with Popen(["md5sum", filename], stdout=PIPE) as proc:
        checksum, _ = proc.stdout.read().split()
        
        # Append duplicate to a list if the checksum is found
        if checksum in checksums:
            duplicates.append(filename)
        checksums[checksum] = filename

print(f"Found Duplicates: {duplicates}")















# program body ends







# end time
end = time.time()

# total time taken
print(f"Runtime of the program is {end - start}")









