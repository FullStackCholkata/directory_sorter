import os
import shutil
import sys
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(prog = 'Directory sorter')
    parser.add_argument('path',
                        nargs = 1,
                        default = os.path.expanduser('~/Downloads'),
                        # required = False,
                        help = 'Path pointing to the directory that you want to be sorted')

    args = parser.parse_args()
    return args.path


def main():

    # We specify the target destination and check if it exists
    target_path = parse_arguments()[0]
    # if not os.path.exists(target_path):
    #     print('Path does not exist!')
    #     exit(0)

    # We define categories for files we want to sort
    categories = {
        "System Files" : ['.exe', '.dll', '.sys', '.drv', '.ini', '.bat', '.cmd', '.msi', '.vxd', '.iso', '.sh', '.bash', '.service', '.plist', ],
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
                file_extension = os.path.splitext(element)[1]

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
    else:
        print('The downloads are empty!')
        exit(0)

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