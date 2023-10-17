import random


class Node:
    def __init__(self, parent, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent


class BinaryTree:
    def __init__(self, key) -> None:
        self.root = Node(None, key)
    
    def __insert(self, parent, node, key):
        if node is None:
            return Node(parent, key)
        if key < node.key:
            node.left = self.__insert(node, node.left, key)
        else:
            node.right = self.__insert(node, node.right, key)
        return node

    def __minValueNode(self, node):
        current = node
        while(current.left is not None):
            current = current.left
        return current

    def insertNode(self, key):
        self.__insert(None, self.root, key)
    
    def __delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.__delete(root.left, key)
        elif key > root.key:
            root.right = self.__delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.__minValueNode(root.right)

            root.key = temp.key
            root.right = self.__delete(root.right, temp.key)

        return root
    
    def deleteNode(self, key):
        self.root = self.__delete(self.root, key)
        print(self.root)

    def __height(self, root):
            return 1 + max(self.__height(root.left), self.__height(root.right)) if root else -1 

    def __printTree(self, root): 
        nlevels = self.__height(root)
        width =  pow(2,nlevels+1)

        q=[(root,0,width,'c')]
        levels=[]

        while(q):
            node,level,x,align= q.pop(0)
            if node:            
                if len(levels)<=level:
                    levels.append([])
            
                levels[level].append([node,level,x,align])
                seg= width//(pow(2,level+1))
                q.append((node.left,level+1,x-seg,'l'))
                q.append((node.right,level+1,x+seg,'r'))

        for i,l in enumerate(levels):
            pre=0
            preline=0
            linestr=''
            pstr=''
            seg= width//(pow(2,i+1))
            for n in l:
                valstr= str(n[0].key)
                if n[3]=='r':
                    linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                    preline = n[2] 
                if n[3]=='l':
                    linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
                    preline = n[2] + seg + seg//2
                pstr+=' '*(n[2]-pre-len(valstr))+valstr 
                pre = n[2]
            print(linestr)
            print(pstr)  

    def display(self):
        self.__printTree(self.root)

    def __searchNode(self, root, node):
        if root == None: 
            print(f'Element {node} doenst found or tree is empty')
            return
        if node > root.key:
            self.__searchNode(root.right, node)
        elif node < root.key:
             self.__searchNode(root.left, node)
        else:
            print(f'Element {node} found')

    def searchNode(self, node):
        self.__searchNode(self.root, node)


rootTree = int(input('Input root tree: '))
tree = BinaryTree(rootTree)

while(True):
    data_raw = input("Please enter value (add, remove, search, print): ")

    if data_raw == "add":
        value = input("Please enter value for insert into tree: ")
        value = int(value)
        tree.insertNode(value)


    elif data_raw == "remove":
        value = input("Please enter value for delete from tree: ")
        value = int(value)
        tree.deleteNode(value)


    elif data_raw == "search":
        value = input("Please enter value for search from tree: ")
        value = int(value)
        tree.searchNode(value)


    elif data_raw == "print":
        tree.display()

    elif data_raw == 'exit':
        break