#!/usr/bin/env python

from heapq import heappop, heappush, heapify
from collections import Counter
import sys


class HuffmanCoding(object):

    def __init__(self):
        self.tree = [] 

    def huff_bin(self, tree, encode, data=None):
        if data == None:
            data = {}
        for i in tree:
            if isinstance(i, list) or isinstance(i, tuple):
                if tree.index(i) == 1:
                    old_encode = encode
                    encode += '0'
                    self.huff_bin(i, encode, data)
                if tree.index(i) == 2:
                    encode = old_encode
                    encode += '1'
                    self.huff_bin(i, encode, data)
            if isinstance(i, str):
                data[i] = encode
        return data

    def construct_tree(self, data):
        char_freq = Counter(data)
        queue = [(char_freq[i],i,) for i in char_freq]
        heapify(queue)
        while len(queue) > 1:
            q1 = heappop(queue)
            q2 = heappop(queue)
            branch = (q1[0] + q2[0], q1, q2)
            heappush(queue, branch)
            if len(q1[1]) < 2:
                self.tree.append([q1[0] + q2[0],q1, q2])
            elif len(q1[1]) > 1 and len(q2[1]) > 1:
                self.tree.append([q1[0] + q2[0], q1, q2])
                self.tree.pop(0)
                self.tree.pop(0)
            else:
                self.tree.append([q1[0] + q2[0], q1, q2])
                self.tree.pop(0)
        print 'Huffman Tree...'
        print '%s\n' % str(self.tree[0])
        return self.tree[0]


if __name__ == '__main__':
    hc = HuffmanCoding()
    if len(sys.argv) >= 2:
        data = sys.argv[1]
        print '\nData to encode... %s\n' % data
        t = hc.construct_tree(data)
        compress = hc.huff_bin(t, '')
        encoding = ''
        stream = []
        for i in  data:
            if compress.has_key(i):
                stream.append(compress[i])
                encoding += compress[i]
        print '\nEncoded data... \n%s\n' % encoding
    else:
        print 'You need to provide some data to encode!'
