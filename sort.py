import os
import shutil
import sys
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(prog = 'Directory sorter')
    parser.add_argument('path',
                        nargs = 1,
                        type = str,
                        help = 'Path pointing to the directory that you want to be sorted')

    parser.add_argument('-n', '--name',
                        nargs = '+',
                        type =  str,
                        required = False,
                        help = 'The name of the files that will be sorted into a folder. Indended use is for files with same names but different extensions.')
    
    return parser.parse_args()


def main():

    args = parse_arguments()
    # In case of sorting a certain name, we get the name
    names = args.name
    # We specify the target destination
    target_path = args.path[0]

    # We define categories for files we want to sort
    categories = {
        "System Files" : ['.exe', '.dll', '.sys', '.drv', '.ini',
                          '.bat', '.cmd', '.msi', '.vxd', '.iso',
                          '.sh', '.bash', '.service', '.plist',
                          '.dmg', '.run', '.deb', '.rpm', '.so'],
        "Documents" : ['.txt', '.docx', '.doc', '.pdf', '.md', '.odt'],
        "Presentations" : ['.pptx'],
        "Tables" : ['.xlsx','.csv', '.tsv'],
        "Audios" : ['.mp3', '.wav', '.flac', '.ogg', '.m4a', '.aiff'],
        "Videos" : ['.mp4', '.avi', '.mov', '.mkv', '.webm'],
        "Images" : ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.heic', '.svg', '.tiff'],
        "Fonts" : ['.ttf', '.otf', '.fon', '.dfont'],
        "Programming files" : ['.c', '.cpp', '.h', '.py', '.java',
                               '.js', '.ts', '.sh', '.rb', '.php',
                               '.html', '.htm', '.css', '.json','.xml',
                               '.sql', '.rs', '.go', '.pl', '.yml',
                               '.yaml', '.swift']

    }

    # We will dynamically create folders to which we will put files in later
    created_folders = {}

    # Listing the contents of the target directory
    directory_contents = os.listdir(target_path)
    # Creating a data structure to store subfolders
    directories = []

    # Only if the directory has contents we check each one if it is a file or a subfolder
    if directory_contents:
        
        for element in directory_contents:
            path_to_element = os.path.join(target_path, element)

            if os.path.isdir(path_to_element):
                directories.append(element)

            elif os.path.isfile(path_to_element):
                file = os.path.splitext(element)
                file_name = file[0]
                file_extension = file[1]

            # If the name isn't set then it means we are executing a normal sort
            if not names:
            
                # We try to check if the selected file matches one of our categories
                for category in categories:
                    for extension in categories.get(category):
                        if file_extension == extension:
                                
                            # Here the dynamic dictionary creation takes place:
                            # The 'category' is going to be used a folder name
                            # Inside this folder the absolute path to the element in question is saved
                            if not category in created_folders:
                                created_folders[category] = []
                            created_folders[category].append(path_to_element)
                            break

            # If the name is set then we find all occurences of the name and sort them into a folder                    
            else:
                for name in names:
                    if file_name == name:
                        if not name in created_folders:
                            created_folders[name] = []
                        created_folders[name].append(path_to_element)
    else:
        print('The downloads are empty!')
        exit(1)

    moved_files = 0
    new_folders = 0

    # For each dynamically added folder we create an actual directory if it doesn't already exist
    for folder in created_folders:

        if not folder in directories:
            os.mkdir(os.path.join(target_path, folder))
            new_folders += 1

        destination_path = os.path.join(target_path, folder)
        for path in created_folders.get(folder):
            shutil.move(path, destination_path)
            moved_files += 1


    print(f'Moving is done! {moved_files} has been moved into {new_folders} new folders!')

if __name__ == "__main__":
    main()