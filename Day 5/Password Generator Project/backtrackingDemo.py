import secrets
#import time

#start_time = time.time()
import random
# l= [4,5,2]


l= [[1,2,3],[4,5,6],[7,8,9]]
#l = [[i + j for j in range(100)] for i in range(0, 5000, 10)] --> tested the time reduction when deleting the empty sublists,
# reduced from 284secs to 267secs

def mixed_list(parentlist: list[list[str]]):

    mixed_list=[]

    total_elements=sum(len(sublist) for sublist in parentlist)
    print(total_elements)
    non_empty_lists=[sublist for sublist in parentlist if len(sublist)>0]
    print("non empty lists: " + str(non_empty_lists))
    while total_elements > 0:
        sublist=secrets.choice(non_empty_lists)
        if len(sublist) > 0:
            selected_element=secrets.choice(sublist)
            sublist.remove(selected_element)
            print(non_empty_lists)
            mixed_list.append(selected_element)
            total_elements -= 1
        else:
            non_empty_lists.remove(sublist)
            print("non-empty_sublist after the removal of empty sublist: " + str(non_empty_lists))

    print(mixed_list)



#end_time = time.time()
#print(f"Execution time: {end_time - start_time:.4f} seconds")
