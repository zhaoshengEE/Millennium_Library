"""
Q3. Write a traverse function (def traverse)
Q4. Write an autocorrect function
"""

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        currentNode = self.root
        for char in word:
            # If the current node has child key with current character,
            # proceed to the next character.
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                return None
        # For autocomplete feature, return currentNode instead of TRUE
        return currentNode
    
    def insert(self, word):
        currentNode = self.root
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            # If the current character is not found in the current node's children,
            # add the character as a new child node
            else:
                newNode = TrieNode()
                currentNode.children[char] = newNode
                currentNode = newNode
        currentNode.children["*"] = None
    
    # Traverse each node of a trie and print each key, including all "*" keys
    def traverse(self, node = None):
        currentNode = node or self.root
        for key, childNode in currentNode.children.items():
            print(key)
            if key != "*":
                self.traverse(childNode)

    # Collect a list of all the trie's words starting from a particular node
    def collectAllWords(self, node = None, word = "", words = []):
        currentNode = node or self.root

        for key, childNode in currentNode.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(childNode, word + key, words)
        return words
    
    def autoComplete(self, prefix):
        currentNode = self.search(prefix)
        if currentNode is None:
            return None
        return self.collectAllWords(currentNode)
    
    def autoCorrect(self, prefix, prefixModified = False):
        currentNode = self.search(prefix)
        if currentNode is None:
            return self.autoCorrect(prefix[:-1], True)
        else:
            if prefixModified is False:
                return prefix
            else:
                return prefix + self.collectAllWords(currentNode)[0]
    
    # Below is the solution offered by the book
    def autoCorrect2(self, word):
        currentNode = self.root
        wordFoundSoFar = ""
        for char in word:
            if currentNode.children.get(char):
                wordFoundSoFar += char
                currentNode = currentNode.children.get(char)
            else:
                return wordFoundSoFar + self.collectAllWords(currentNode)[0]
        return word

if __name__ == "__main__":
    t = Trie()
    t.insert("cat")
    t.insert("catnap")
    t.insert("catnip")
    t.traverse()
    print(t.autoCorrect("catnar"))