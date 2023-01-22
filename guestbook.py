import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='Command to run')
    parser.add_argument('note', nargs='?', help='Note content')
    parser.add_argument('index', nargs='?', type=int, help='Note index')
    args = parser.parse_args()

    guestbook = []

    if args.command == 'new':
        guestbook.append(args.note)
        print('Note added')
    elif args.command == 'list':
        for i, note in enumerate(guestbook):
            print(f'{i+1}. {note}')
    elif args.command == 'edit':
        guestbook[args.index-1] = args.note
        print('Note edited')
    elif args.command == 'delete':
        del guestbook[args.index-1]
        print('Note deleted')
    else:
        print('Invalid command')

if __name__ == '__main__':
    main()
