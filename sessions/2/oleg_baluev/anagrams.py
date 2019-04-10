# The algorithm uses a prefix tree data structure. Each node of the tree is array of two values:
# [final_letter, children], where final_letter is a flag telling that there is a word which ends with this node,
# children is a dictionary if child nodes identified by the next character in the word.

# Check if a specified word is present in the tree
def check_presence(source, start_index, sample_len, tree_root):
    next_node = tree_root[1].get(source[start_index])
    if (next_node == None):
        return False

    if (sample_len == 1):
        # Whether the node is final letter
        return next_node[0]
    else:
        # Go to next character recursively
        next_start_index = (start_index + 1) % len(source)
        return check_presence(source, next_start_index, sample_len - 1, next_node)

# Add a new word into the tree
def insert_word(source, start_index, word_len, tree_root):
    next_node = tree_root[1].get(source[start_index])
    if (next_node) == None:
        # Creating a node for the character
        next_node = [False, {}]
        tree_root[1][source[start_index]] = next_node

    if (word_len == 1):
        # Marking the node as a final letter
        next_node[0] = True
    else:
        # Adding the rest word part
        next_start_index = (start_index + 1) % len(source)
        insert_word(source, next_start_index, word_len - 1, next_node)

# Returns a source word shifted using the specified start index
def shift(source, start_index):
    return source[start_index:len(source)] + source[0:start_index]

words = ["abc", "def", "cab", "bac", "Макар", "карма", "армак", "ракам", "кабан", "банка", "банк", "камыш", "мышка"]
print(words)

# Main program
root = [False, {}]
for word in words:
    if (type(word) != str or len(word) == 0):
        continue
    word = word.lower()

    # The word has already been handled before, skipping
    if (check_presence(word, 0, len(word), root)):
        continue;

    # Shifting the word consequently and seeing if there are such words in the tree
    for i in range(1, len(word)):
        if (check_presence(word, i, len(word), root)):
            print(word + " <--> " + shift(word, i))
    insert_word(word, 0, len(word), root)
print('end')