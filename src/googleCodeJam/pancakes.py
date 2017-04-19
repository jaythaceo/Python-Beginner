# oversized_pancake_flipper.py

"""
Sample input:
3
---+-++- 3
+++++ 4
-+-+- 4
Sample output
Case #1: 3
Case #2: 0
Case #3: IMPOSSIBLE
"""

import copy
from multiprocessing import Queue


# NOTE: The goddamn branching factor tho
class SequenceNode:

    def __init__(self, seq, flipper_width, num_flips = 0):

        self.seq = copy.deepcopy(seq)
        self.flipper_width = flipper_width
        self.num_flips = num_flips # equal to tree depth

        self.parent = None
        self.children = []

    def search(self):
        """
        Breadth-first search through tree: successful termination occurs when
        we find a node of all smiley faces (i.e. all chars of "+"), whereas
        unsuccessful termination occurs when we can no longer find a new
        configuration in the tree (via "flipping")
        """

        seq_set = set()
        node_queue = queue.Queue()

        node_queue.put(self)
        seq_set.add(self.seq)

        while not node_queue.empty():

            node = node_queue.get()

            # Check if solution node
            if "-" not in node.seq: return node.num_flips

            # Let's flip! Generates children; if we've already seen all
            # children, don't add to the queue for further exploration
            for flip_start_index in range(len(node.seq) - node.flipper_width + 1):

                flip_end_index = flip_start_index + node.flipper_width
                new_seq = SequenceNode.flip(node.seq, flip_start_index, flip_end_index)

                if new_seq in seq_set: continue

                new_node = SequenceNode(new_seq, node.flipper_width, node.num_flips + 1)
                seq_set.add(new_seq)
                node_queue.put(new_node)

        return None

    @staticmethod
    def flip(seq, a, b):
        """ Flip given sequence at the indices a and b, returning new string """

        flip_region = "".join(["+" if x == "-" else "-" for x in seq[a:b]])
        new_seq = seq[:a] + flip_region + seq[b:]
        return new_seq

def oversized_pancake_flipper(*args):
    """
    x in {+, -}^d, where 2 <= d <= 1000
    x = number of flips, or "IMPOSSIBLE"
    """

    # NOTE: Aim for strings of size 1000
    seq = args[0]
    flipper_width = int(args[1])

    # Search a tree for the answer
    seq_tree = SequenceNode(seq, flipper_width)
    answer = seq_tree.search()

    if answer is None: answer = "IMPOSSIBLE"
    return answer, ""