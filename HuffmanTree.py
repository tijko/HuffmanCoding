from collections import Counter
import sys

def two_freq(tree, sec_queue, freq):
    tree.append([freq[0][1] + freq[1][1], freq[0], freq[1]])
    sec_queue.append([freq[0][1] + freq[1][1], [freq[0][1] + freq[1][1], freq[0], freq[1]]])    
    freq = freq[2:]
    return tree, sec_queue, freq

def one_to_one(tree, sec_queue, freq):
    for i in tree:
        if i == sec_queue[0][1]:
            hold = tree.index(i)
            tree[tree.index(i)] = [sec_queue[0][0] + freq[0][1], sec_queue[0][1], freq[0]]
            sec_queue.append([freq[0][1] + sec_queue[0][0], tree[hold]])
            sec_queue = sec_queue[1:]
            freq = freq[1:]
            break
    return tree, sec_queue, freq

def two_sec(tree, sec_queue):
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
    return tree, sec_queue

def h_tree(data):
    tree = []
    sec_queue = []
    counts = Counter(data)
    freq = sorted([(i[0], i[1],) for i in zip(counts.keys(), counts.values())], key=lambda x: x[1])
    tree, sec_queue, freq = two_freq(tree, sec_queue, freq)
    while len(freq) > 1:
        if len(sec_queue) < 2:
            if freq[0][1] + freq[1][1] <= freq[0][1] + sec_queue[0][0]:
                tree, sec_queue, freq = two_freq(tree, sec_queue, freq)
            elif freq[0][1] + sec_queue[0][0] < freq[0][1] + freq[1][1]:
                tree, sec_queue, freq = one_to_one(tree, sec_queue, freq)
            if len(freq) < 2:
                break
        if len(sec_queue) > 1:
            if freq[0][1] + freq[1][1] <= freq[0][1] + sec_queue[0][0] and freq[0][1] + freq[1][1] <= sec_queue[0][0] + sec_queue[1][0]:
                tree, sec_queue, freq = two_freq(tree, sec_queue, freq)
            elif freq[0][1] + sec_queue[0][0] < freq[0][1] + freq[1][1] and freq[0][1] + sec_queue[0][0] <= sec_queue[0][0] + sec_queue[1][0]:
                tree, sec_queue, freq = one_to_one(tree, sec_queue, freq)
            elif sec_queue[0][0] + sec_queue[1][0] < freq[0][1] + freq[1][1] and \
                sec_queue[0][0] + sec_queue[1][0] < sec_queue[0][0] + freq[0][1]:
                tree, sec_queue = two_sec(tree, sec_queue)
    while len(sec_queue) > 1:
        if freq:
            if freq[0][1] + sec_queue[0][0] < sec_queue[0][0] + sec_queue[1][0]:
                tree, sec_queue, freq = one_to_one(tree, sec_queue, freq)
            else:
                tree, sec_queue = two_sec(tree, sec_queue)
        else:
            tree, sec_queue = two_sec(tree, sec_queue)
    if freq:
        tree, sec_queue, freq = one_to_one(tree, sec_queue, freq)
    return tree[0]

print h_tree(sys.argv[1])


