class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}

    def _insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.key_to_node:
            if self.head.next != self.tail and self.head.next.count == 1:
                node = self.head.next
            else:
                node = Node(1)
                self._insert_after(self.head, node)

            node.keys.add(key)
            self.key_to_node[key] = node
            return

        current = self.key_to_node[key]
        new_count = current.count + 1
        next_node = current.next

        if next_node != self.tail and next_node.count == new_count:
            target = next_node
        else:
            target = Node(new_count)
            self._insert_after(current, target)

        current.keys.remove(key)
        target.keys.add(key)
        self.key_to_node[key] = target

        if not current.keys:
            self._remove_node(current)

    def dec(self, key: str) -> None:
        current = self.key_to_node[key]

        if current.count == 1:
            current.keys.remove(key)
            del self.key_to_node[key]

            if not current.keys:
                self._remove_node(current)
            return

        new_count = current.count - 1
        prev_node = current.prev

        if prev_node != self.head and prev_node.count == new_count:
            target = prev_node
        else:
            target = Node(new_count)
            self._insert_after(prev_node, target)

        current.keys.remove(key)
        target.keys.add(key)
        self.key_to_node[key] = target

        if not current.keys:
            self._remove_node(current)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))