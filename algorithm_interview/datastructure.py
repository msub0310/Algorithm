import collections

class ListNode():
    def __init__(self, x: any):
        self.val = x
        self.next = None

    def copy(self):
        copied_head = ListNode(self.val)
        now = copied_head
        while now.next is not None:
            now.next = ListNode(self.next.val)
            now = now.next
        return copied_head

    "ver2, more memory, more computation"
    #def copy(self):
    #    return listToListNode(listNodeToList(self))

    def print(self):
        output_list = []
        head = self
        while head:
            output_list.append(str(head.val))
            head = head.next
        print("->".join(output_list))

    def toList(self):
        output_list = []
        head = self
        while head:
            output_list.append(head.val)
            head = head.next

        return output_list

def listToListNode(input_list: list) -> ListNode:
    head = ListNode(input_list[0])
    now = head
    for i in range(1, len(input_list)):
        now.next = ListNode(input_list[i])
        now = now.next

    return head

def listNodeToList(head: ListNode) -> list:
    output_list = []
    while head:
        output_list.append(head.val)
        head = head.next

    return output_list

def printListNode(head: ListNode) -> None:
    output_list = []
    while head:
        output_list.append(str(head.val))
        head = head.next

    print("->".join(output_list))

def reverseListNode(head: ListNode) -> ListNode:
    copied_head = head.copy()
    node, prev = copied_head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

class Stack():
    def __init__(self):
        self.last = None
        self.__len = 0

    def push(self, x):
        self.last, self.last.next = ListNode(x), self.last
        self.__len += 1

    def pop(self):
        x = self.last.val
        self.last = self.last.next
        self.__len -= 1
        return x

    def len(self):
        return self.__len


class CircularDeque():
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node
        
    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True
    
    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createBTree(treeList: [int], index: int) -> TreeNode:
    pNode = None
    if index < len(treeList):
        if treeList[index] == None:
            return
        pNode = TreeNode(treeList[index])
        pNode.left = createBTree(treeList, 2 * index + 1)
        pNode.right = createBTree(treeList, 2 * index + 2)
    return pNode

def BTreeToList(root: TreeNode) -> list:
    result = []
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

        if all((x is None for x in queue)) and len(queue) % 2 == 0:
            break
    
    return result

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.word

    def startWith(self, prefix: str) -> bool:
        node = self.node
        for char in prefix:
            if char not in node.children[char]:
                return False
            node = node.children[char]
        
        return True