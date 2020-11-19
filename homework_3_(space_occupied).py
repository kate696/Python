
import os
def space_occupied(directory):
    total_space = 0
    for item in os.listdir(directory):
        joined_path = os.path.join(directory, item)
        if os.path.isfile(joined_path):
            total_space += os.path.getsize(joined_path)
        elif os.path.isdir(joined_path):
            total_space += space_occupied(joined_path)
    return total_space

print ("Space occupied by the folder is ", space_occupied("C:\\Python39"))


