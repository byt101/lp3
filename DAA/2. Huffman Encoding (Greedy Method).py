# 2. Huffman Encoding

import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = self.right = None
    def __lt__(self, other): return self.freq < other.freq

def huffman_encoding(chars, freqs):
    heap = [Node(c, f) for c, f in zip(chars, freqs)]
    heapq.heapify(heap)
    while len(heap) > 1:
        left, right = heapq.heappop(heap), heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left, merged.right = left, right
        heapq.heappush(heap, merged)
    return heap[0]

def print_codes(node, code=""):
    if node is None: return
    if node.char: print(f"{node.char}: {code}")
    print_codes(node.left, code + "0")
    print_codes(node.right, code + "1")

if __name__ == "__main__":
    chars = ['a','b','c','d','e','f']
    freqs = [5,9,12,13,16,45]
    root = huffman_encoding(chars, freqs)
    print("characters:", chars)
    print("frequencies:", freqs)
    print("Huffman Codes:")
    print_codes(root)
