N = int(input())
if N==0:
    print(0)
if N != 0:
    act = {}
    for i in range(N):
        inp = input().split()
        T, C, F = ' '.join(inp[:-2]), inp[-2], inp[-1]

        C = int(''.join(C.split(':')))
        F = int(''.join(F.split(':')))

        act[T] = {
            'start': C,
            'end': F
        }
        order = sorted(act, key=lambda x: act[x]['end'])

    S = [order[0]]

    for activity in order[1:]:
        if act[activity]['start']>=act[S[-1]]['end']:
            S.append(activity)
    print(len(S))
    for activity in S:
        print(activity)

