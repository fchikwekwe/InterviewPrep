

from pprint import pprint


def flatten(dictionary, new_dict=None, old_key=None):
    """
    Algorithmic complexity analysis
    n = total number of items in dictionary 
    k = total number of original keys in dictionary
    v = total number of values in dictionary 
    s = average length of original keys 
    m = max depth of recursive stack
    
    Time complexity: O(v + k * (s + m))
    """
    if new_dict is None:
        new_dict = {}  # O(v) time, space in the end

    for key, value in dictionary.items():  # O(k) time
        if old_key is None:
            # maybe add validation for keys?
            new_key = str(key)  # O(s) time, space
        else:
            new_key = old_key + '_' + str(key)  # O(s), time, space

        try:
            # RECURSIVE CASE; could also use conditional
            for item in value:
                flatten(value, new_dict, new_key)  # O(m) space
        except:
            # BASE CASE
            new_dict[new_key] = value  # O(1) time, space

    return new_dict


example = {'Geeks': {'for': {'for': 1, 'geeks': 4}}, 'for': {
    'geeks': {'Geeks': 3}}, 'geeks': {'Geeks': {'for': 7}}}

# pprint(example)
pprint(flatten(example))

'''
Pseudocode: 

- have a new_dict to store the output

- iterate over the key, value pairs in original dict
- check if the old_key was None
    - if None, then new_key = key 
    - else, new_key = old_key + _ + key

- try to iterate over value: 
    - RECURSIVE CASE: if you can, the recursively call flatten while passing in value, new dict and new key
    - BASE CASE: if not, then set new key as key and current value as value in new_dict 
    
- returns new dict 


Thoughts: 
- recursive approach 
- old_key from previous call, new_key to next call 
- params: original dict, new dict, old_key (this changes every time)
- changing the string each time as we recurse 
- BASE CASE: when value is not dict/ not iterable 
    - try/catch block? 
'''
