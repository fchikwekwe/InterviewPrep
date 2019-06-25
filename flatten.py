def flatten(diction, new_dict=None, new_key=None):
    print('current output\n', new_dict)
    if new_dict is None:
        new_dict = {}

    for key, value in diction.items():
        if new_key is None:
            new_key = str(key)
        else:

            new_key = new_key + '_' + str(key)
            print(new_key)

        try:
            for item in value:
                flatten(value, new_dict, new_key)
        except:
            # base case; value is no longer iterable
            new_dict[new_key] = value

    return new_dict


example = {'Geeks': {'for': {'for': 1, 'geeks': 4}}, 'for': {
    'geeks': {'Geeks': 3}}, 'geeks': {'Geeks': {'for': 7}}}

print(flatten(example))
