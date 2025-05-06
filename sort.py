import os
import shutil
import pathlib

target_path = "C:/Users/Owner/Downloads"
if not os.path.exists(target_path):
    print('Path does not exist!')
    exit(0)

categories = {
    "System Files" : ['.exe', '.dll', '.sys', '.drv', '.ini', '.bat', '.cmd', '.msi', '.vxd', '.iso'],
    "Documents" : ['.txt', '.docx', '.pdf'],
    "Presentations" : ['.pptx'],
    "Tables" : ['.xlsx','.csv'],
    "Audios" : ['.mp3', '.wav', '.flac'],
    "Videos" : ['.mp4', '.avi', '.mov'],
    "Images" : ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.heic', '.gif'],
    "Fonts" : ['.ttf', '.otf', '.fon'],
    "Programming files" : ['.html', '.htm', '.css', '.js', '.json', '.xml', '.php',
                           '.asp', '.aspx', '.cpp', '.h', '.java', '.py', '.cs', '.rb', '.html', '.htm', '.sql']

}

directory_contents = os.listdir(target_path)
directories = []
if directory_contents:
    for element in directory_contents:
        path_to_element = os.path.join(target_path, element)
        if os.path.isdir(path_to_element):
            directories.append(element)
        #elif os.path.isfile(path_to_element):


print(os.listdir(target_path))
