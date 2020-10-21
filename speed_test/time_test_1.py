import time 

from tqdm import tqdm

start_time  = time.time()

# list for final results
simple_list = []

# three working arrays
period_list = [i for i in range(100)]
start_RA = -75
start_DEC = -75

for i in tqdm(period_list):
    for j in tqdm(range(100), leave=True):
        start_RA += 1
        for k in tqdm(range(100), leave=True):
            start_DEC += 1
            simple_list.append((i, start_RA, start_DEC))
    
print(time.time() - start_time)