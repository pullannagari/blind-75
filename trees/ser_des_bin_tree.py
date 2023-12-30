# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def __init__(self):
        self.index = 0

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        def dfs(root):
            if not root:
                result.append("null")
                return
            result.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        return ",".join(result)

        # queue = deque()
        # queue.append(root)
        # ser_str = ""
        # while queue:
        #     for i in range(len(queue)):
        #         curr = queue.popleft()
        #         if curr:
        #             queue.append(curr.left)
        #             queue.append(curr.right)
        #             ser_str += f"{curr.val},"
        #         else:
        #             ser_str += "null,"
        # return ser_str[:len(ser_str)-1]

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        data = data.split(",")
        if not data:
            return
        def dfs():
            if self.index > len(data):
                return
            if data[self.index] == "null":
                self.index += 1
                return
            curr_node = TreeNode(data[self.index])
            self.index += 1
            curr_node.left = dfs()
            curr_node.right = dfs()
            return curr_node
        return dfs()
        # if data == "null":
        #     return None
        # nodes = data.split(",")
        # def dfs(index, nodes):
        #     if index >= len(nodes):
        #         return None
        #     if nodes[index] == "null":
        #         return None
        #     curr_node = TreeNode(nodes[index])
        #     curr_node.left = dfs(2*index+1, nodes)
        #     curr_node.right = dfs(2*index+2, nodes)
        #     return curr_node
        # return dfs(0, nodes)
        return None
        



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))