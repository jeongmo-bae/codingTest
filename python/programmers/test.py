from collections import Counter
import numpy as np

t_dict = Counter([1,1,1,2,3,4,5,1,2,3,541,5,0,123,123,4,13,23,1,None,np.nan])
print(f"KEYS : {t_dict.keys()}")
print(f"VALUES : {t_dict.values()}")
print(f"ITEMS : {t_dict.items()}")

t_dict_count_more_2_key = [key for key, count in t_dict.items() if count >= 2]
print(t_dict_count_more_2_key)
for i in range(len(t_dict_count_more_2_key)) :
    print(t_dict_count_more_2_key.pop(0))

from collections import deque
queue = deque([1,2,3])
print(queue.popleft())
print(queue)
