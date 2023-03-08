from Module_classe_fonctions import*
import unittest

#---Test des fonctions de la classe ArrayQueue--------------
class fonctions_Testcase(unittest.TestCase):
    def testlenArrQu(self):
        arrQu=ArrayQueue()
        arrQu.enqueue(4)
        self.assertEqual(arrQu.__len__(),1)



#-----Test des fonctions de la classe ArrayStack-------


    def testlenArrStack(self):
        arrStack=ArrayStack()
        arrStack.push(8)
        arrStack.push(4)
        arrStack.push(2)
        arrStack.pop()
        
        self.assertEqual(arrStack.top(),4)
        self.assertEqual(arrStack.__len__(),2)

    
#-----Test des fonctions de la classe LinkedQueue----------

    def testFonctLQueue(self):
        LQueue=LinkedQueue()
        LQueue.enqueue(7)
        LQueue.enqueue("exercice")
        LQueue.enqueue("labeur")
        self.assertEqual(LQueue.__len__(),3)

#------Test des fonctions de la class LinkedStack--------

    def testFoncLStack(self):
        LStack=LinkedStack()
        LStack.push(10)
        LStack.push("succes")
        LStack.push("etudes")
        LStack.push("Sciences et programmation")
        LStack.pop()
        LStack.top()
        LStack.top()
        self.assertEqual(LStack.__len__(),3)

if __name__=='__main__':
    unittest.main()
