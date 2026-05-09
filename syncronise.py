# def zomato(name):
#      print(name)
#      time.sleep(2)
#      print(name,"completed")
# import time 
# start=time.time()
# zomato('User')  
# zomato('Order')  
# zomato('Payment') 
# print("total time taken",time.time()-start) 


# def resturant(order,t):
#      print(order)
#      time.sleep(t)
#      print("deliverd done")
# import time
# start=time.time()
# resturant("Table1 butterchicken",5)
# resturant("Table2 butternans",2)
# resturant("Table3 biryani",1)
# resturant("Table4 apricot",3)
# print(time.time()-start)



import asyncio 
async def resturant(order,t):
    print(order)
    await asyncio.sleep(t)
    print("deliverd done")
import time
start=time.time()
async def all_calls_at_a_time():
    await asyncio.gather(
resturant("Table1 butterchicken",5),
resturant("Table2 butternans",2),
resturant("Table3 biryani",1),
resturant("Table4 apricot",3)
)   
asyncio.run(all_calls_at_a_time())   
print(time.time()-start)
from threading import Thread
def resturant(order,t):
    print(order)
    time.sleep(t)
    print("deliverd done")
start=time.time()
w1=Thread(target=resturant,args=("Table1 Butterchicken",5))
w2=Thread(target=resturant,args=("Table2 Nanns",2))
w3=Thread(target=resturant,args=("Table1 biryani",1))
w4=Thread(target=resturant,args=("Table1 apricot",3))
s=time.time()
w1.start()
w2.start()
w3.start()
w4.start()
w1.join()
w2.join()
w3.join()
w4.join()
print(time.time()-s)