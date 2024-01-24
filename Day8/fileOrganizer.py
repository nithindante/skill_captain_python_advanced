import os 
import shutil  
pdf= mp4 = mp3= gif= pptx= []
input_files= str(input("Enter the directory to be organised "))
output_files=str(input("Enter the directory where the organized files should go "))
try:
    dir_list = os.listdir(input_files) 
except FileNotFoundError:
    print("Please enter a correct file path ")
else:
    for dir in dir_list:
        if ".pdf" in dir:
            pdf.append(dir)
        elif ".mp3" in dir:
            mp3.append(dir)
        elif ".gif" in dir:
            gif.append(dir)
        elif ".pptx" in dir:
            pptx.append(dir)
        elif ".mp4" in (dir):
            mp4.append(dir)

def copy_files(doc,output_files,fileFormat):
        directory = doc
        parent_dir = output_files
        path = os.path.join(parent_dir, directory)
        newdir = os.makedirs(path)
        for document in fileFormat:
            source = input_files+f"\\{document}"
            destination = path
            dest = shutil.copy(source, path) 

copy_files("pdf",output_files,pdf)
copy_files("mp4",output_files,mp4)
copy_files("mp3",output_files,mp3)
copy_files("gif",output_files,gif)
copy_files("pptx",output_files,pptx)


#C:\Users\NithinRajkumar\Desktop\SortedFiles
#C:\Users\NithinRajkumar\Desktop\files