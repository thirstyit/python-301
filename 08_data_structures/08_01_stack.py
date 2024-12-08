# Build a custom `Stack` similar to the `Queue` you built
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            old_head = self.head
            self.head = new_node
            self.head.next = old_head
            
            self.length += 1                   
        

    def pop(self):
        if self.head == None:
            return None
        else:
            popped_value = self.head.value
            self.head = self.head.next
            self.length -= 1
            return popped_value
            

    def is_empty(self):
        return self.head is None
    


    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head.value
        
    def print_length(self):
        return print(self.length)

# Create a new `Queue` object
morning_tasks = Stack()

# Add items to the queue during the previous night
morning_tasks.push("get dressed")
morning_tasks.push("eat breakfast")

print(morning_tasks.peek())


morning_tasks.push("go to work")

morning_tasks.print_length()

# Check what'll be your first task during a midnight wake-up without doing it
print(morning_tasks.peek())  # get dressed

# Fetch an element from the queue in the morning right after waking up
task = morning_tasks.pop()

print(f"Todo: {task}")


morning_tasks.print_length()

task = morning_tasks.pop()  # get dressed

print(f"Todo: {task}")  # Todo: get dressed

morning_tasks.push("Work hard")

print(morning_tasks.peek())