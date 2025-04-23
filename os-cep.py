class Tree:
    def __init__(self, fruits):
        self.fruits = fruits

    def __str__(self):
        return str(self.fruits) 

class Picker:  
    
    def __init__(self):
        self.crate = []
    
    def pick(self,tree, callLoader):

        for fruit in tree.fruits[:]:
            
            if len(self.crate) == 12:
                self.crate = callLoader(self.crate)
                
            tree.fruits.remove(fruit) 
            self.crate.append(fruit)
        
        self.crate = callLoader(self.crate)

            
class Loader:
    
    def __init__(self):
        
        self.truck = []
    
    def load(self,crate):
        
        self.truck.append(crate)        
        return []   # or crate = []



            


mytree = Tree([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10])
mypicker = Picker()
myloader = Loader()
mypicker.pick(mytree, myloader.load)

print(mypicker.crate)
print(myloader.truck)
print(mytree)