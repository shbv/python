"""
JSON is cross-language compatible. 
Text based (not binary like pickle), but stored in unicode encoding
"""
import json

# dictionary
d = {}
d['id'] = 100
d['name'] = 'test'
d['tags'] = ('a', 'b', 'c')     # converts to list 
d['enabled'] = True             # converts to true
d['comments'] = None            # converts to null
d['map'] = {'a': 1, 'b': 2}

# write json
print(f"=== writing {d} into json ===")
with open('temp.json', mode='w', encoding='utf-8') as fp:
    json.dump(d, fp)  # serialize python dict d & writes it to stream object fp
print()

# write json with indent
print(f"=== writing {d} into json with indent ===")
with open('temp2.json', mode='w', encoding='utf-8') as fp:
    json.dump(d, fp, indent=2)  # number of spaces for each level
print()

# write json with custom serializer for types it doesnt support
d['bytes'] = b'\xAB\xD5\xf8'
def to_json(python_object):                                             
    if isinstance(python_object, bytes):                                
        return {'__class__': 'bytes',
                '__value__': list(python_object)}                       
    raise TypeError(repr(python_object) + ' is not JSON serializable')  
print(f"=== writing {d} with bytes into json with indent ===")
with open('temp3.json', mode='w', encoding='utf-8') as fp:
    json.dump(d, fp, indent=2, default=to_json)  # without default, json.dump will raise TypeError bytes not JSON serializable
print()

# read json  
del d
print(f"=== reading from json with indent ===")
with open('temp2.json', mode='r', encoding='utf-8') as fp:
    d = json.load(fp)   
print(d)
print()

# read json with custom serializer to convert back types it doesnt support 
del d
def from_json(json_object):                                             
    if '__class__' in json_object and json_object['__class__'] == 'bytes':                                
        return bytes(json_object['__value__'])                       
    return json_object
print(f"=== reading from json with bytes & indent ===")
with open('temp3.json', mode='r', encoding='utf-8') as fp:
    d = json.load(fp, object_hook=from_json)  # without object_hook, json.load will not convert bytes to python bytes object
print(d)
print()


