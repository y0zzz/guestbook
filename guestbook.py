import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='Command to run')
    parser.add_argument('note', nargs='?', help='Note content')
    parser.add_argument('index', nargs='?', type=int, help='Note index')
    args = parser.parse_args()

    guestbook = load_guestbook()

    if args.command == 'new':
        guestbook.append(args.note)
        save_guestbook(guestbook)
        print('Note added')
    elif args.command == 'list':
        for i, note in enumerate(guestbook):
            print(f'{i+1}. {note}')
    elif args.command == 'edit':
        guestbook[-args.index] = args.note
        save_guestbook(guestbook)
        print('Note edited')
    elif args.command == 'delete':
        del guestbook[-args.index]
        save_guestbook(guestbook)
        print('Note deleted')
    else:
        print('Invalid command')

def load_guestbook():
    try:
        with open('guestbook.txt', 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def save_guestbook(guestbook):
    with open('guestbook.txt', 'w') as f:
        f.write('\n'.join(guestbook))

if __name__ == '__main__':
    main()
