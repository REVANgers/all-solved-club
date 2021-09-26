import sys;
import collections;
import json;

# sys.stdin = open("input1.txt");
# sys.stdin = open("input2.txt");
# sys.stdin = open("input3.txt");

T = int(input());

for testCase in range(T):
    P = input();
    N = int(input());
    dq = collections.deque(map(str, json.loads(input())));
    (isReversed, isError) = (False, False);

    # print(P);
    # print(N);

    """
    for cmd in P:
        if (cmd == 'R'):
            dq.reverse();
        elif (cmd == 'D'):
            if (dq):
                dq.popleft();
            else:
                break;
    """

    for cmd in P:
        if (cmd == 'R'):
            isReversed = not isReversed;
        elif (cmd == 'D'):
            if (dq):
                (dq.pop()) if (isReversed) else (dq.popleft());
            else:
                isError = True;
                break;


    # print(dq);

    if (isReversed):
        dq.reverse();

    print(("error") if (isError) else ("[" + ",".join(dq) + "]"));
