import journal

# TODO Add Docstrings to functions.

def main():
    print_header()
    run_event_loop()


def print_header():
    print('---------------------')
    print('    Journal App')
    print('---------------------')
    print()


def run_event_loop():
    print('What did you want to do with your Journal?')
    cmd = 'empty'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd entries, E[x]it: ')
        cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, I'm not sure what you mean by '{}'".format(cmd))

    print('Exiting...')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}]: {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <Enter> to exit: ')
    journal.add_entry(text, data)


if __name__ == '__main__':
    main()
