import files_utils as fu
import os

Path=os.getcwd()
Repo="test"
File_name="test.parquet"
Lx=[0,1,2,3,4]
My=[[10,11,12,13,14],[20,21,22,13,24]]

fu.save_mult_pqt(Lx,My,Path,Repo,File_name)
fu.pqt_to_csv(Path, Repo, File_name)