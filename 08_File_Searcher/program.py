import os
import collections

SearchResults = collections.namedtuple('search result', 'file, line, text')


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

    matches = search_folders(folder, text)
    for m in matches:
        print('------ MATCH---------')
        print('File: ' + m.file)
        print('Line {}'.format(m.line))
        print('Text' + m.text.strip())
        print()


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
    return text.lower()


def search_folders(folder, text):
    items = os.listdir(folder)
    # all_matches = []

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, text)
            # all_matches.extend(matches)
            # for m in matches:
            #     yield m
        else:
            yield from search_file(full_item, text)
            # all_matches.extend(matches)
            # for m in matches:
            #     yield m

    # return all_matches


def search_file(filename, search_text):
    # matches = []

    with open(filename, 'r', encoding='utf-8') as fin:

        line_number = 0
        for line in fin:
            line_number += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResults(text=line, file=filename, line=line_number)
                yield m

        # return matches


if __name__ == '__main__':
    main()
