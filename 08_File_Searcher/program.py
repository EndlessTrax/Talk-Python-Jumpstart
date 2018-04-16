import os


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry we can't search that location...")
        return

    text = get_search_text_from_user()
    if not text:
        print("Sorry, we can't search nothing...")
        return

    search_folders(folder, text)


def print_header():
    print('-----------------------------')
    print('     FOLDER SEARCH APP')
    print('-----------------------------')


def get_folder_from_user():
    folder = input('What folder would you like to search?')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you searching for [single phrase only]?')
    return text


def search_folders(folder, text):
    print("Would print out results for Dir: {} with the search for {}...".format(folder, text))


if __name__ == '__main__':
    main()
