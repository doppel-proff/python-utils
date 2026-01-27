import files_utils as fu
import os

Path=os.getcwd()
Repo="test"
File_name="test.csv"
Lx=[0,1,2,3,4]
My=[[10,11,12,13,14],[20,21,22,13,24]]

fu.save_mult_csv(Lx,My,Path,Repo,File_name)