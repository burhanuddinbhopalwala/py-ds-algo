
import pdb


class LinkedListNode(object):
    def __init__(self, ele: int):
        self.ele = ele
        self.next = None
        self.arbt = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, ele: int):
        if self.head:
            node = LinkedListNode(ele)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = LinkedListNode(ele)
            self.head.next = None

    def reverse_inplace(self):
        current = self.head
        previous, next_ = None, None
        while current:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_
        self.head = previous
        return self.head

    def find_middle_node(self):
        # * Hair Tortoize problem
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # * Floyd Cycle detection algorithm
            # fast == slow
        return slow.ele

    def find_kth_node(self, k: int):
        p = self.head
        q = self.head

        while k > 0:
            p = p.next
            k -= 1
        if not p:
            return -1
        while p:
            p = p.next
            q = q.next

        return q.ele

    def print(self):
        current = self.head
        while current:
            print(current.ele)
            current = current.next

    def print_by_arbt(self):
        current = self.head
        while current.next:
            print(current.arbt.ele)
            current = current.next

    def pop(self, ele):
        current = self.head
        temp = self.head
        while current:
            if current.next and current.ele == ele:
                if current.next:
                    current.ele = current.next.ele
                    current.next = current.next.next
                    return
                else:
                    temp.next = None
            temp = current
            current = current.next

    def alternate_split(self):
        head1 = self.head
        head2 = self.head.next
        if not any([head1, head2]):
            return [-1, -1]

        current = head1
        while current.next:
            temp = current.next
            current.next = temp.next if temp.next else temp
            current = temp
        return [head1, head2]

    def merge(self, head1: LinkedListNode, head2: LinkedListNode):
        if not head1:
            return head2
        if not head2:
            return head1

        head = None
        if head1.ele < head2.ele:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next

        while head1 and head2:
            if head1.ele < head2.ele:
                head.next = head1
                head = head.next
                head1 = head1.next
            else:
                head.next = head2
                head = head.next
                head2 = head2.next

        while head1:
            head.next = head1
            head1 = head1.next

        while head2:
            head.next = head2
            head2 = head2.next

        return head

    # def palindrome(self):

    #     # find middle + reverse half
    #     # OR iterate first and last pointer until middle pointer

    def sorted_0_1_2(self):
        count = [0] * 3
        current = self.head
        while current:
            count[current.ele] += 1
            current = current.next

        current = self.head
        for index, ele in enumerate(count):
            while ele > 0:
                ele -= 1
                current.ele = index
                current = current.next

    def add_1(self):
        carry = 1
        self.head = self.reverse_inplace()

        current = self.head
        while current:
            add = current.ele + carry
            carry = 1 if add // 10 else 0
            current.ele = 0 if add // 10 else add

            temp = current
            current = current.next

        if carry:
            temp.next = LinkedListNode(carry)
        self.head = self.reverse_inplace()

    def set_arbt_right_maxm(self):
        self.head = self.reverse_inplace()
        current = self.head
        current.arbt = None

        maxm = float('-inf')
        maxm_temp = current
        current = current.next

        while current:
            current.arbt = maxm_temp
            if maxm < current.ele:
                maxm_temp = current
                maxm = current.ele

            current = current.next

        self.reverse_inplace()


ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)
ll.push(50)
ll.print()
ll.reverse_inplace()
ll.print()


print(ll.find_middle_node())
print(ll.find_kth_node(2))
ll.pop(30)
ll.print()

print('#######################################################################')
heads = ll.alternate_split()
h1, h2 = heads[0], heads[1]
head1, head2 = h1, h2
while head1:
    print(head1.ele)
    head1 = head1.next
while head2:
    print(head2.ele)
    head2 = head2.next

print('#######################################################################')
# head = ll.merge(h1, h2)
# while head:
#     print(head.ele)
#     head = head.next

print('#######################################################################')
ll = LinkedList()
ll.push(2)
ll.push(2)
ll.push(1)
ll.push(1)
ll.push(0)
ll.sorted_0_1_2()
ll.print()

print('#######################################################################')
ll = LinkedList()
ll.push(2)
ll.push(9)
ll.push(9)
ll.add_1()
ll.print()

print('#######################################################################')
ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(2)
ll.push(1)
ll.set_arbt_right_maxm()
ll.print_by_arbt()
