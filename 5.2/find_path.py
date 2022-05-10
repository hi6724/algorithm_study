import sys

sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, value, key):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class NodeManage:
    def __init__(self, head):
        self.head = head

    def insert(self, value, key):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value, key)
                    break

            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value, key)
                    break

    def preorder(self):
        res = []

        def order(node):
            res.append(node.key)
            if node.left != None: order(node.left)
            if node.right != None: order(node.right)

        order(self.head)
        return res

    def postorder(self):
        res = []

        def order(node):
            if node.left != None: order(node.left)
            if node.right != None: order(node.right)
            res.append(node.key)

        order(self.head)
        return res


def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    nodeinfo = sorted(nodeinfo, key=lambda x: -x[1])
    print(nodeinfo)
    answer = []
    tree = NodeManage(Node(nodeinfo[0][0], nodeinfo[0][-1]))
    for i in nodeinfo[1:len(nodeinfo)]:
        tree.insert(i[0], i[-1])
    answer.append(tree.preorder())
    answer.append(tree.postorder())
    return answer


test_case = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2],
             [2, 2]]
print(sorted(test_case, key=lambda x: -x[1]))

print(solution(test_case))
