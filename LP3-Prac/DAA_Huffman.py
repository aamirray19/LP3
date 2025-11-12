# Huffman coding implementation (build tree, generate codes, encode, decode)
# Uses heapq (min-heap) to always pick two smallest-frequency nodes -> greedy step.

import heapq
from collections import Counter, namedtuple

# A tiny Node class for the Huffman tree
class Node:
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq          # frequency / weight
        self.symbol = symbol      # character / symbol; None for internal nodes
        self.left = left          # left child (represents bit '0' in our convention)
        self.right = right        # right child (represents bit '1')
    
    # heapq needs comparison; we'll only compare by frequency.
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequency_map):
    """
    Build Huffman tree from a dict-like {symbol: frequency}.
    Returns the root Node of the Huffman tree.
    """
    heap = []
    # Create a leaf node for each symbol and push onto heap
    for sym, freq in frequency_map.items():
        heapq.heappush(heap, Node(freq, symbol=sym))
    
    # Edge case: single symbol -> give it code '0'
    if len(heap) == 1:
        only = heapq.heappop(heap)
        root = Node(only.freq, left=only, right=None)
        return root

    # Greedy step: merge two lowest-frequency nodes until one node (root) remains
    while len(heap) > 1:
        left = heapq.heappop(heap)   # least frequent
        right = heapq.heappop(heap)  # second least frequent
        merged = Node(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)
    
    return heapq.heappop(heap)

def generate_codes(root):
    """
    Traverse the Huffman tree and produce a dict {symbol: code}.
    Uses pre-order traversal accumulating the bit string.
    """
    codes = {}
    def dfs(node, prefix):
        if node is None:
            return
        if node.symbol is not None:  # leaf
            # If tree had only one symbol, prefix could be empty string; assign '0'
            codes[node.symbol] = prefix if prefix != "" else "0"
            return
        dfs(node.left, prefix + "0")
        dfs(node.right, prefix + "1")
    dfs(root, "")
    return codes

def encode(text, codes):
    """Encode text (string or sequence of symbols) into a bitstring using codes map."""
    return ''.join(codes[s] for s in text)

def decode(bitstring, root):
    """
    Decode a bitstring using the Huffman tree root.
    Walk the tree for each bit until a leaf is reached, then append symbol.
    """
    if root is None:
        return ""
    result = []
    node = root
    for bit in bitstring:
        node = node.left if bit == "0" else node.right
        if node.symbol is not None:  # reached leaf
            result.append(node.symbol)
            node = root
    return ''.join(result)

# Example usage and demonstration
if __name__ == "__main__":
    text = input("Enter the text: ")
    # 1) frequency table
    freq = Counter(text)
    print("Frequencies:")
    for ch, f in freq.items():
        print(f"'{ch}': {f}")
    # 2) build tree
    root = build_huffman_tree(freq)
    # 3) generate codes
    codes = generate_codes(root)
    print("\nHuffman Codes:")
    for ch, code in sorted(codes.items(), key=lambda x: (len(x[1]), x[0])):
        printable = ch if ch != " " else "' '"
        print(f"{printable!s}: {code}")
    # 4) encode
    encoded = encode(text, codes)
    print(f"\nEncoded bitstring (length {len(encoded)}):\n{encoded[:120]}{'...' if len(encoded)>120 else ''}")
    # 5) decode
    decoded = decode(encoded, root)
    print("\nDecoded equals original?", decoded == text)
    if decoded != text:
        print("Decoded:", decoded)
        print("Original:", text)
