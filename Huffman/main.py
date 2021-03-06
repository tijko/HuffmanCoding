#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ast
import argparse

from Huffman import *

# read data in/out from outside of system?

def options():
    parser = argparse.ArgumentParser(description='''Huffman Coding -- compress 
                                                    or decompress data.''')
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('-W', '--write', help='Write to file', action='store_true')
    group.add_argument('-e', '--encode', help='Encode data', action='store_true')
    group.add_argument('-d', '--decode', help='Decode data', action='store_true')
    parse = parser.parse_args()
    return parse


def main(options):
    choice = 'answer?'
    if options.encode:
        while choice[0].lower() != 'y' and choice[0].lower() != 'n':
            choice = raw_input('Do you want to use data read from a file y/n?: ')
        if choice[0].lower() == 'y':
            datafile = raw_input('Which file(use absolute path)?: ')
            if not os.path.isfile(datafile):
                print 'Error: file does not exist --'
                print 'Make sure your path is correct(/home/username/filename)'
                return
            else:
                with open(datafile) as f:
                    data = f.read()            
            msg = '\n' + 'Huffman Tree...\n%s\n' % str(h_tree(data))
            compress = huff_bin(h_tree(data), '')
            stream = []
            encoding = ''
            for i in data:
                if compress.has_key(i):
                    stream.append(compress[i])
                    encoding += compress[i]
            msg = msg + '\nKey-Map... \n%s\n' % str(compress)
            msg = msg + '\nEncoded data stream... \n%s\n' % str(stream)
            msg = msg + '\nEncoded string...\n%s\n' % encoding
            print msg
        if choice[0].lower() == 'n':
            data = raw_input('Data to compress: ')
            if not data:
                return
            msg = '\n' + 'Huffman Tree...\n%s\n' % str(h_tree(data))
            compress = huff_bin(h_tree(data), '')
            stream = []
            encoding = ''
            for i in data:
                if compress.has_key(i):
                    stream.append(compress[i])
                    encoding += compress[i]
            msg = msg + '\nKey-Map... \n%s\n' % str(compress)
            msg = msg + '\nEncoded data stream... \n%s\n' % str(stream)
            msg = msg + '\nEncoded string...\n%s\n' % encoding
            print msg
        if options.write:
            with open(os.environ['HOME'] + '/encode.txt', 'w') as f:
                f.write(msg)
            print 'Saved to... %s\n' % (os.environ['HOME'] + '/encode.txt')
    if options.decode:
        try:
            datamap = ast.literal_eval(raw_input('\nProvide a key-map to read: '))
        except (SyntaxError, ValueError) as e:
            print 'A dictionary is needed'
            return
        if not isinstance(datamap, dict):
            print 'A dictionary is needed'
            return
        try:
            stream = ast.literal_eval(raw_input('\nData stream to decompress: '))
        except (SyntaxError, ValueError) as e:
            print 'Error: check the data stream --'
            return
        datamap = {v:k for k,v in datamap.items()}
        print '\nDecoded data...\n%s'% (''.join([datamap[i] for i in stream if i in datamap]) + '\n')
        if options.write:
            with open(os.environ['HOME'] + '/decode.txt', 'w') as f:
                f.write(decode)            
        

if __name__ == '__main__':
    opts = options()    
    main(opts)

