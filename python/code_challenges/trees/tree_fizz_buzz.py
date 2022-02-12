#### Code Challenge 18 ####


class Node:
    def __init__(self, val = None):
        self.val = val
        self.children = []


def fizz_buzz_tree(head):
    #### Checks to see if tree is empty ####
    if not head:
         raise Exception('Tree is Empty')

    #### Clones useing head as a reference
    clone= {head: Node(fizz_buzz(head.val))}
    queue = [head]
    while queue:
        cur = queue.pop(0)
        for child in cur.children:
            queue.append(child)
            clone[child] = Node(fizz_buzz(child.val))
            clone[cur].children.append(clone[child])

    #### Returns a clone ####
    return clone[head]

    #### Checks if the numbers are divisible by 3, 5, or both
def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)

    #### Creates the modified tree and returns it using original as a reference ####
def check_the_tree(head):
    if not head:
        return head

    queue, res = [head], []
    while queue:
        cur = queue.pop(0)
        res.append(cur.val)
        for child in cur.children:
            queue.append(child)
    return res
