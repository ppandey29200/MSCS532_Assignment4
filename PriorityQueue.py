class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        # Initialize a task with its ID, priority, arrival time, and deadline
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        # Return a string representation of the task
        return f"Task(ID: {self.task_id}, Priority: {self.priority}, Arrival Time: {self.arrival_time}, Deadline: {self.deadline})"

class PriorityQueue:
    def __init__(self):
        # Initialize an empty heap
        self.heap = []

    def _heapify_up(self, index):
        # Move the element at index up to its correct position
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent].priority < self.heap[index].priority:
                # Swap if the current element has higher priority than its parent
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        # Move the element at index down to its correct position
        size = len(self.heap)
        while index * 2 + 1 < size:
            left_child = index * 2 + 1
            right_child = index * 2 + 2
            largest = index

            # Find the largest among the current element and its children
            if left_child < size and self.heap[left_child].priority > self.heap[largest].priority:
                largest = left_child
            if right_child < size and self.heap[right_child].priority > self.heap[largest].priority:
                largest = right_child

            if largest != index:
                # Swap if the largest is not the current element
                self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
                index = largest
            else:
                break

    def insert(self, task):
        # Insert a new task into the heap
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        # Remove and return the task with the highest priority
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def increase_key(self, task_id, new_priority):
        # Increase the priority of a task with the given task_id
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                task.priority = new_priority
                self._heapify_up(i)
                break

    def is_empty(self):
        # Check if the priority queue is empty
        return len(self.heap) == 0

# Testing the PriorityQueue
pq = PriorityQueue()

# Adding tasks
pq.insert(Task(1, 10, 5, 10))
pq.insert(Task(2, 20, 2, 8))
pq.insert(Task(3, 15, 1, 12))
pq.insert(Task(4, 25, 0, 7))

# Display tasks in the priority queue
print("Priority Queue tasks:")
print(pq.heap)

# Extracting tasks with highest priority
print("\nExtracting tasks with highest priority:")
print(pq.extract_max())  # Should return the task with priority 25
print(pq.extract_max())  # Should return the task with priority 20
print(pq.extract_max())  # Should return the task with priority 15

# Check if priority queue is empty
print("\nIs priority queue empty?", pq.is_empty())