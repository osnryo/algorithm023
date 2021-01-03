# 设计实现双端队列。
# 你的实现需要支持以下操作：
# MyCircularDeque(k)：构造函数,双端队列的大小为k。
# insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
# insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
# deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
# deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
# getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
# getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
# isEmpty()：检查双端队列是否为空。
# isFull()：检查双端队列是否满了。

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        
        self.capacity = k
        self.size = 0
        
        self.circular_deque = [ 0 ] * k
        
        self.rear = 0
        self.front = k-1
        
        
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size+1 <= self.capacity:
            
            self.circular_deque[ self.front ] = value
            self.front = (self.front-1)%self.capacity
            self.size += 1
        
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        
        if self.size+1 <= self.capacity:
            
            self.circular_deque[ self.rear ] = value
            self.rear = (self.rear+1)%self.capacity
            self.size += 1
        
            return True
        
        else:
            return False
        
        
        
        
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        
        if self.size != 0:
            
            self.front = (self.front+1)%self.capacity
            self.size -= 1
            return True
        
        else:
            return False
        
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """

        if self.size != 0:
            
            self.rear = (self.rear-1)%self.capacity
            self.size -= 1
            return True
        
        else:
            return False        
        
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        
        if self.size != 0:
            return self.circular_deque[ (self.front+1)%self.capacity ]
        else:
            return -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        
        if self.size != 0:
            return self.circular_deque[ (self.rear-1)%self.capacity ]
        else:
            return -1
        
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        
        return self.size == self.capacity