from collections import Counter
import sys

def h_tree(data):
    tree = []
    sec_queue = []
    counts = Counter(data)
    freq = sorted([(i[0], i[1],) for i in zip(counts.keys(), counts.values())], key=lambda x: x[1])
    sec_queue.append([freq[0][1] + freq[1][1], [freq[0][1] + freq[1][1], freq[0], freq[1]]])
    tree.append([freq[0][1] + freq[1][1], freq[0], freq[1]])
    freq = freq[2:]
    while len(freq) > 1:
        if len(sec_queue) < 2:
            if freq[0][1] + freq[1][1] <= freq[0][1] + sec_queue[0][0]:
                tree.append([freq[0][1] + freq[1][1], freq[0], freq[1]])
                sec_queue.append([freq[0][1] + freq[1][1], [freq[0][1] + freq[1][1], freq[0], freq[1]]])
                freq = freq[2:]
            elif freq[0][1] + sec_queue[0][0] < freq[0][1] + freq[1][1]:
                for i in tree:
                    if i == sec_queue[0][1]:
                        hold = tree.index(i)
                        tree[tree.index(i)] = [sec_queue[0][0] + freq[0][1], sec_queue[0][1], freq[0]]
                        sec_queue.append([freq[0][1] + sec_queue[0][0], tree[hold]])
                        sec_queue = sec_queue[1:]
                        freq = freq[1:]
                        break
            if len(freq) < 2:
                break
        if len(sec_queue) > 1:
            if freq[0][1] + freq[1][1] <= freq[0][1] + sec_queue[0][0] and freq[0][1] + freq[1][1] <= sec_queue[0][0] + sec_queue[1][0]:
                tree.append([freq[0][1] + freq[1][1], freq[0], freq[1]])
                sec_queue.append([freq[0][1] + freq[1][1], [freq[0][1] + freq[1][1], freq[0], freq[1]]])
                freq = freq[2:]
            elif freq[0][1] + sec_queue[0][0] < freq[0][1] + freq[1][1] and freq[0][1] + sec_queue[0][0] <= sec_queue[0][0] + sec_queue[1][0]:
                for i in tree:
                    if i == sec_queue[0][1]:
                        hold = tree.index(i)
                        tree[tree.index(i)] = [sec_queue[0][0] + freq[0][1], sec_queue[0][1], freq[0]]
                        sec_queue.append([freq[0][1] + sec_queue[0][0], tree[hold]])
                        sec_queue = sec_queue[1:]
                        freq = freq[1:]
                        break
            elif sec_queue[0][0] + sec_queue[1][0] < freq[0][1] + freq[1][1] and \
                sec_queue[0][0] + sec_queue[1][0] < sec_queue[0][0] + freq[0][1]:
                for i in tree:
                    if i == sec_queue[0][1]:
                        hold = tree.index(i)
                        tree[tree.index(i)] = [sec_queue[0][0] + sec_queue[1][0], sec_queue[0][1], sec_queue[1][1]]
                        sec_queue.append([sec_queue[0][0] + sec_queue[1][0], tree[hold]])
                        for j in tree:
                            if j == sec_queue[1][1]:
                                tree.remove(j)
                                break
                        sec_queue = sec_queue[2:]
                        break
    while len(sec_queue) > 1:
        if freq:
            if freq[0][1] + sec_queue[0][0] < sec_queue[0][0] + sec_queue[1][0]:
                for i in tree:
                    if i == sec_queue[0][1]:
                        hold = tree.index(i)
                        tree[tree.index(i)] = [sec_queue[0][0] + freq[0][1], sec_queue[0][1], freq[0]]
                        sec_queue.append([freq[0][1] + sec_queue[0][0], tree[hold]])
                        sec_queue = sec_queue[1:]
                        freq = freq[1:]
                        break
            else:
                for i in tree:
                    if i == sec_queue[0][1]:
                        hold = tree.index(i)
                        tree[tree.index(i)] = [sec_queue[0][0] + sec_queue[1][0], sec_queue[0][1], sec_queue[1][1]]
                        sec_queue.append([sec_queue[0][0] + sec_queue[1][0], tree[hold]])
                        for j in tree:
                            if j == sec_queue[1][1]:
                                tree.remove(j)
                                break 
                        sec_queue = sec_queue[2:]
                        break
        else:
            for i in tree:
                if i == sec_queue[0][1]:
                    hold = tree.index(i)
                    tree[tree.index(i)] = [sec_queue[0][0] + sec_queue[1][0], sec_queue[0][1], sec_queue[1][1]]
                    sec_queue.append([sec_queue[0][0] + sec_queue[1][0], tree[hold]])
                    for j in tree:
                        if j == sec_queue[1][1]:
                            tree.remove(j)
                            break
                    sec_queue = sec_queue[2:]
                    break
    if freq:
        for i in tree:
            if i == sec_queue[0][1]:
                hold = tree.index(i)
                tree[tree.index(i)] = [sec_queue[0][0] + freq[0][1], sec_queue[0][1], freq[0]]
                sec_queue.append([freq[0][1] + sec_queue[0][0], tree[hold]])
                sec_queue = sec_queue[1:]
                freq = freq[1:]
                break
    return tree[0]

print h_tree(sys.argv[1])
