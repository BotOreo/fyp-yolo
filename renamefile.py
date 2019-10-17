import os

imdir='cube_train' #create the folder of the directory of the images to be trained is stored
if not os.path.isdir(imdir):
    os.mkdir(imdir)

small_folder = [folder for folder in os.listdir('.') if 'cube_data' in folder]

print(small_folder)

n = 2937
for folder in small_folder: #this loop is to rename everything in one folder
    for imfile in os.scandir(folder):
        os.rename(imfile.path, os.path.join(imdir,'{:06}.png'.format(n)))
        n+=1

#print(face_folder) # this is to check all folder with 'Faces' tagname