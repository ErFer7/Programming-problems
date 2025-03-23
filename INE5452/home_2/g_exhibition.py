"""
Exhibition.
"""

test_count = int(input())

for test in range(test_count):
    friend_count = int(input())
    friends = {friend: [[], 0] for friend in range(friend_count)}  # Stamps, stamps únicos
    all_stamps = {}

    for friend in range(friend_count):
        stamps = set(list(map(int, input().split()))[1:])
        friends[friend][0].extend(stamps)

        for stamp in stamps:
            if stamp in all_stamps:
                all_stamps[stamp] += 1
            else:
                all_stamps[stamp] = 1

    unique_stamp_count = len([count for count in all_stamps.values() if count == 1])
    result = ''

    for friend in range(friend_count):
        if unique_stamp_count > 0:
            for stamp in friends[friend][0]:
                if all_stamps[stamp] == 1:
                    friends[friend][1] += 1

            result += ' {:.6f}%'.format((friends[friend][1] / unique_stamp_count) * 100)
        else:
            result += ' 0.000000%'

    print('Case {}:{}'.format(test + 1, result))
