import time 
import itertools

from tqdm import tqdm

start_time  = time.time()

# three working arrays

period_list = [i for i in range(100)]
start_RA = [i for i in range(-75, 76)]
start_DEC = [i for i in range(-75, 76)]

# list for final results

final_list = []
simple_list = list(itertools.product(period_list, start_RA, start_DEC))
for i in tqdm(simple_list):
    final_list.append(i) 
    
print(time.time() - start_time)