l = []

if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        x = input().split()
        cmd = x[0]
        if cmd == 'append':
            l.append(x[1])
        elif cmd == 'print':
            print(l)
        elif cmd == 'insert':
            l.insert(int(x[1]), int(x[2]))
        elif cmd == 'reverse':
            l = l[::-1]
        elif cmd == 'pop':
            l.pop()
        elif cmd == 'sort':
            l = sorted(l)
        elif cmd == 'remove':
            l.remove(int(x[1]))
        print(l)