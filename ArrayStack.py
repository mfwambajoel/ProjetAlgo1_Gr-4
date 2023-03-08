class ArrayStack:
    """LIFO stack implementation using a python list as underlying storage"""
    
    def __init__(self):
        """create an empty"""
        self._data=[]
    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)
    
    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data)==0
    
    def push(self,e):
        """Return but not remove the element at the top of the stack"""
        self._data.append(e)
        
    def top(self):
        """Return (but not remove) the element at the top of the stack.
        Raise Empty Exception if the stack is empty"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def reverse_file(self,filename):
        S=ArrayStack()
        original=open(filename)
        for line in original:
            S.push(line.rstrip('\n'))
        original.close()
    
    def pop(self):
        """Remove and return the element from the top of the LIFO"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

        #now we overwrite with content in LIFO order
        output=open(filename,'w')
        while not S.is_empty():
            output.write(S.pop() + '\n')
        output.close()
        return
    def somme(self,a,b):
        print(a+b)
    
if __name__=='__main__':

    print('Test')
    arr=ArrayStack()
    arr.push(2)
    arr.push(5)
    arr.pop()
    print(arr)
    arr.somme(4,10)
  
    print("Taille",arr.__len__(),arr.top())
          
                 
