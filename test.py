import files_utils as fu
import os

Path=os.getcwd()
Repo="test"
File_name="test.csv"
Lx=[0,1,2,3,4]
Ly=[10,11,12,13,14]

fu.save_tuple_csv(Lx,Ly,Path,Repo,File_name)