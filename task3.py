

import sqlalchemy as db
# create connection with the database
con = db.create_engine('postgresql://iti:iti@localhost/data_management')
# Find out the tables in this DB
con.table_names()



import pandas as pd
# Create a SQL query to load the entire diabetes table
#query = """
#SELECT *
#FROM diabetes_unscored
#"""

query = """
select pregnancies,
  glucose ,
  bloodpressure ,
  skinthickness ,
  insulin ,
 bmi ,
  diabetespedigreefunction,
  age from diabetes_unscored 
Except
select pregnancies,
  glucose ,
  bloodpressure ,
  skinthickness ,
  insulin ,
 bmi ,
  diabetespedigreefunction,
  age from diabetes_scored ;

"""

# Load the table 
diabetes_df = pd.read_sql(query, con)
# View the head
#diabetes_df.head(60)
diabetes_df.shape






import numpy as np
import h5py
filename = "/home/nourhan/Downloads/ITI_Python/Task3/model.h5"

with h5py.File(filename, 'r') as f:
    ls=list(f.keys())
    print('list of datasets',ls)
   # data=f.get('den')
   # den=np.array(data)
   # print('shape of dense ', den.shape )


import numpy as np
import json
import keras
from keras.models import model_from_json
json_file = open('/home/nourhan/Downloads/ITI_Python/Task3/model.json', 'r')
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
loaded_model.load_weights("/home/nourhan/Downloads/ITI_Python/Task3/model.h5")

numpy_array = diabetes_df.to_numpy()
#print(numpy_array)

prediction = loaded_model.predict(numpy_array)
#print(prediction)


new_list=[]
for x in prediction :
        for y in x:
            if y >= 0.5 :
                y=1
            else :
                y=0
            new_list.append(y)


diabetes_df['outcome']= new_list

diabetes_df.to_sql(name = 'diabetes_scored',                           # New table name
                con=con,                                            # Connection object to the database
                schema = 'public',index = False ,                                  # Name of schema to store the data in
                if_exists='append')                                 # Action to be done if a table with the same name e



print('scheduled')




