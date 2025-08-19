import random
import string
from time import sleep
import time

def generate_string():
    
    length = random.randint(8, 64) # length is a random number between 8 and 63 characters.
    return ''.join(random.choices(string.ascii_letters + string.digits, k = length)) #the computer returns a joint string of ascii letters, digits; paired with the length of the password

pass 

for _ in range(1): # for some number in range, (generate 1 password)
    exc = generate_string() #execute, call function

    with open("generated_passwords.txt", "a") as f: # open a text file and write output to it  #note, must create a text file, or just erase this section completely
        print(exc, file=f)
    
    print(exc) #print the result from generatestring()
#sleep(0.1)


#ime counter (funsies)

start_time = time.perf_counter()
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")