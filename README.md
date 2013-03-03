HuffmanCoding
=============

Huffman Coding is an algorithm technique for compression/decompression.

This is my take on it in python.  In the Huffman.py file I do the encoding with out
python's heapq module and in the HuffHeapq.py file I get the encoding done with, yup you
guessed it, pythons heapq module.

While they both work great you can see how much cleaner the code is with the heapq module.

###Example:

    python Huffman.py 'this is an example of a huffman tree'

    Huffman Tree...
    [36, [16, [8, ('a', 4), ('e', 4)], [8, [4, ('i', 2), ('h', 2)], [4, ('m', 2), ('n', 2)]]], [20, [8, [4, ('s', 2), ('t', 2)], [4, [2, ('l', 1), ('o', 1)], [2, ('p', 1), ('r', 1)]]], [12, [5, [2, ('u', 1), ('x', 1)], ('f', 3)], (' ', 7)]]]

    Encoded string without compression...
    11101110111010011110011111010011110011111000011101111110010111111100001110110111111011110010111101111110011111000011110111101011100111100111101101110000111011111110111100111001011100101

    Encoded data stream... ['1001', '0101', '0100', '1000', '111', '0100', '1000', '111', '000', '0111', '111', '001', '11001', '000', '0110', '10110', '10100', '001', '111', '10101', '1101', '111', '000', '111', '0101', '11000', '1101', '1101', '0110', '000', '0111', '111', '1001', '10111', '001', '001']

    Encoded string...
    100101010100100011101001000111000011111100111001000011010110101000011111010111011110001110101110001101110101100000111111100110111001001

    Decoded string... this is an example of a huffman tree
