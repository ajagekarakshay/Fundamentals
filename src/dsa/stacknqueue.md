---
title: Stack & Queue
---

# Stack

A stack is a linear data structure that follows a particular order in which the operations are performed. The order is LIFO(Last In First Out). The principal operations of a stack are:

- Push
- Pop
- Peek
- isEmpty

=== "Python"
    Stacks in python can be implemented using lists (dynamic arrays).
    ```py
    stack = []
    
    # Stack operations
    stack.append(10)  # Push
    stack.append(20)
    stack.append(30)
    print(stack)  # [10, 20, 30]
    
    item = stack.pop()  # Pop
    print(item)  # 30
    print(stack)  # [10, 20]
    
    peek_item = stack[-1]  # Peek
    print(peek_item)  # 20
    
    is_empty = not stack  # isEmpty
    print(is_empty)  # False
    
    ```

=== "C++"
    Stacks in C++ uses vector or deque (default) as the underlying container.
    ```cpp
    #include <stack>
    #include <iostream>
    
    int main() {
        std::stack<int> stack;

        // Push
        stack.push(10); 
        stack.push(20);

        // peek
        std::cout << stack.top() << std::endl;  // 20

        // pop 
        int item = stack.pop(); 
        std::cout << item << std::endl;  // 20

        std::cout << stack.size() << std::endl;  // 1

        // isEmpty
        std::cout << stack.empty() << std::endl;  // false
        
        return 0;
    }
    ```

# Queue

A queue is another linear data structure that follows a particular order in which the operations are performed. The order is FIFO(First In First Out). The principal operations of a queue are:

- Enqueue
- Dequeue
- Peek
- isEmpty

=== "Python"
    Queues in python can be implemented using lists (dynamic arrays).
    ```py
    queue = []
    # Enqueue
    queue.append(10)  
    queue.append(20)

    # Dequeue
    item = queue.pop(0) 
    
    # Peek
    peek_item = queue[0] 
    print(peek_item)  # 20
    
    # isEmpty
    is_empty = not queue  
    print(is_empty)  # False
    
    ```
    Queues can also be implemented with Deque (double ended queue) in Python.
    ```py
    from collections import deque
    queue = deque()
    # Enqueue
    queue.append(10)  
    queue.append(20)
    
    # Dequeue
    item = queue.popleft() 
    
    # Peek
    peek_item = queue[0] 
    print(peek_item)  # 10
    
    # isEmpty
    is_empty = not queue  
    print(is_empty)  # False
    ```

=== "C++"
    Queues in C++ uses deque (default) as the underlying container.
    ```cpp
    #include <queue>
    #include <iostream>
    
    int main() {
        std::queue<int> qq;

        // Enqueue
        qq.push(10); 
        qq.push(20);

        // Dequeue
        int item = qq.pop(); 
        std::cout << item << std::endl;  // 10

        // Peek
        std::cout << qq.front() << std::endl;  // 20

        // isEmpty
        std::cout << qq.empty() << std::endl;  // false
        
        return 0;
    }
    ```