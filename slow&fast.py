'''#linked list cycle 
class Solution(object):
    def hasCycle(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False #op:True


#inked list cycle 2 
class Solution(object):
    def detectCycle(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else:
            return None
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow #op:2
#middle of the linked list
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# Helper: convert a Python list into a linked list
def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


# Helper: convert a linked list back into a Python list (for printing)
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# ---- Run it ----
head = build_linked_list([1, 2, 3, 4, 5, 6])

s1 = Solution()
middle = s1.middleNode(head)

print(linked_list_to_list(middle))   # Output: [4, 5, 6]
            
                
class Solution(object):
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total = 0
            while number > 0:
                digit = number % 10
                total += digit**2
                print(f"   digit={digit}, total so far={total}, number now={number//10}")
                number //= 10
            return total

        slow = n
        fast = get_next(n)
        print(f"start: slow={slow}, fast={fast}")

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            print(f"after step: slow={slow}, fast={fast}")

        print(f"final: fast={fast}")
        return fast == 1


# ---- Run it ----
s = Solution()
result = s.isHappy(19)
print("Is 19 happy?", result)
op:digit=9, total so far=81, number now=1
   digit=1, total so far=82, number now=0
start: slow=19, fast=82
   digit=9, total so far=81, number now=1
   digit=1, total so far=82, number now=0
   digit=2, total so far=4, number now=8
   digit=8, total so far=68, number now=0
   digit=8, total so far=64, number now=6
   digit=6, total so far=100, number now=0
after step: slow=82, fast=100
   digit=2, total so far=4, number now=8
   digit=8, total so far=68, number now=0
   digit=0, total so far=0, number now=10
   digit=0, total so far=0, number now=1
   digit=1, total so far=1, number now=0
   digit=1, total so far=1, number now=0
after step: slow=68, fast=1
final: fast=1
Is 19 happy? True


#is palindrome
class Solution(object):
    def isPalindrome(self, head):
        left=0
        right=len(head)-1
        while left<right:
            if head[left]!=head[right]:
                return False
            left+=1
            right-=1
        return True
s1=Solution()
print(s1.isPalindrome([1,2,2,1]))
#palindrome method 2
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # Step 1: Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Compare both halves
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


# -------- Create Linked List [1,2,2,1] --------
node4 = ListNode(1)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

head = node1

# -------- Test --------
s1 = Solution()
print(s1.isPalindrome(head))#op:True


#Remove nth node from list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        print(f"Start: fast={fast.val}, slow={slow.val}")

        for i in range(n + 1):
            fast = fast.next
            print(f"  Moving fast ahead, step {i+1}: fast={fast.val}")

        print(f"After gap setup: fast={fast.val}, slow={slow.val}")

        while fast:
            fast = fast.next
            slow = slow.next
            fast_val = fast.val if fast else "None"
            print(f"  Moving together: fast={fast_val}, slow={slow.val}")

        print(f"Loop ended. slow is now at value={slow.val}, about to remove value={slow.next.val}")

        slow.next = slow.next.next

        print("Node removed!")

        return dummy.next


# Helper: build a linked list from a Python list
def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


# Helper: convert linked list back to Python list for printing
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# ---- Run it ----
head = build_linked_list([1, 2, 3, 4, 5])
n = 2

s = Solution()
new_head = s.removeNthFromEnd(head, n)

print("Final list:", linked_list_to_list(new_head))
#op:
#Final list: [1, 2, 3, 5]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))

class Solution:
    def reorderList(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev

        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


# Test it
head = build_list([1, 2, 3, 4, 5])
print("Before:", end=" ")
print_list(head)

Solution().reorderList(head)

print("After: ", end=" ")
print_list(head)
op:Before: 1 -> 2 -> 3 -> 4 -> 5
After:  1 -> 5 -> 2 -> 4 -> 3




#duplicate number in array value=2
class Solution:
    def findDuplicate(self, nums):
        # Phase 1: find intersection point in the cycle
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(f"Phase 1 -> slow={slow}, fast={fast}")
            if slow == fast:
                break

        # Phase 2: find entrance to the cycle (the duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            print(f"Phase 2 -> slow={slow}, fast={fast}")

        return slow


# Test it
nums = [1, 3, 4, 2, 2]
print("Input:", nums)
result = Solution().findDuplicate(nums)
print("Duplicate:", result) #op:Duplicate: 2'''


hakdksdn