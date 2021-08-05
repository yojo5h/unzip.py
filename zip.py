import os, zipfile

dir_name =r"<directorypath>"
extension = ".zip"

#change directory from working dir to dir with files
os.chdir(dir_name)

#loop through items in dir
for item in os.listdir(dir_name):

#check for ".zip" extension
     if item.endswith(extension):
          
          file_name = os.path.abspath(item)
          
          zip_ref = zipfile.ZipFile(file_name)
          
          #extract file to dir
          zip_ref.extractall(dir_name)
          
          zip_ref.close()
         
print("Files have been unzipped successfully!")
