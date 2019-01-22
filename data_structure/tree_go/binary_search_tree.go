package tree_go

type BinarySearchTree struct {
	Root *Node
}

func (tree *BinarySearchTree) Insert(key int) {
	if tree.Root == nil {
		tree.Root = &Node{
			Key: key,
		}
		return
	}
	move := tree.Root
	for move != nil {
		if key > move.Key {
			if move.Right == nil {
				move.Right = &Node{Key: key}
				return
			}
			move = move.Right
		} else if key < move.Key {
			if move.Left == nil {
				move.Left = &Node{Key: key}
				return
			}
		} else {
			return
		}
	}
}

func (tree *BinarySearchTree) Find(key int) *Node {
	move := tree.Root
	for move != nil {
		if move.Key == key {
			return move
		}
		if key > move.Key {
			move = move.Right
		} else {
			move = move.Left
		}
	}
	return nil
}

func (tree *BinarySearchTree) Delete(key int) {
	node := tree.Root
	var nodeParent *Node
	for node != nil && node.Key != key {
		nodeParent = node
		if key > node.Key {
			node = node.Right
		} else {
			node = node.Left
		}
	}
	if node == nil {
		return // 没找到
	}

	// 如果删除的节点左右节点都不为空，那么找到右子树中最小节点
	// 将他的数据替换到要删除的节点，然后删除这个柚子属于中最小的节点
	if node.Left != nil && node.Right != nil {
		rightTreeMinNode := node.Right
		rightTreeMinNodeParent := node
		for rightTreeMinNode.Left != nil {
			rightTreeMinNodeParent = rightTreeMinNode
			rightTreeMinNode = rightTreeMinNode.Left
		}
		node.Key = rightTreeMinNode.Key // 替换数据
		node = rightTreeMinNode
		nodeParent = rightTreeMinNodeParent
	}

	// 如果要删除的节点只有左节点，右节点或者是叶子节点
	var child *Node
	if node.Left != nil {
		child = node.Left
	} else if node.Right != nil {
		child = node.Right
	} else {
		child = nil
	}

	// 从树中删除节点
	if nodeParent == nil {
		tree.Root = child
	} else if nodeParent.Left == node {
		nodeParent.Left = child
	} else {
		nodeParent.Right = child
	}
}

func inOrder(node *Node, result []*Node) {
	if node != nil {
		inOrder(node.Left, result)
		result = append(result, node)
		inOrder(node.Right, result)
	}
}

func (tree *BinarySearchTree) InOrder() []*Node {
	keys := make([]*Node, 0)
	inOrder(tree.Root, keys)
	return keys
}
