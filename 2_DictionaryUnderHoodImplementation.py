'''
Implement your own dictionary but using classes

create a class called Dictionary and it should have methods for initialising an array, getter, setter functions

Apart from that bonus points for any additional methods or properties you have implemented

 

1) For the hashing part, you must use your own custom hashing function, and should not use ascii values
'''
# global_arr=[None, None, None, None, None, None, None, None]
#hash map-nased on hashing
class diction:
  def __init__(self):
    self.arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  def set_hashmap(self,key,value):
    total=0
    for i in key:
      total += ord(i)
    print(total) 
    #resizing
    total = total%10
    print(total)
    self.arr.insert(total,value)
    # print(self.arr)
  def get_hashmap(self,key):
    total=0
    for i in key:
      total += ord(i)
    # print(total)
    #resizing
    total = total%10
    # print(total)
    return self.arr[total]
  def display(self):
    print(self.arr)

if __name__ == "__main__":
  obj=diction()
  obj.set_hashmap("chandana",291)
  print(obj.get_hashmap("chandana"))
  obj.display()
  