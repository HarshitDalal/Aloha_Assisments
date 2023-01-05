import json

'''
Python object =	JSON object
dict =	object
list, tuple	 = array
str	= string
int, long, float = numbers
True = true
False = false
None = null
'''


if __name__ == '__main__':
    data = {
        'name': 'Harshit',
        'age': 23,
        'edu': [
            {
                'Graduation': 'BCA'
            },
            {
                'Post Graduation': 'MCA'
            }
        ],
        'work': 'Aloha Technology',
        'married': False,
        'disability': None
    }

    json_data = json.dumps(data, indent=4)
    print(json_data)
    print(type(json_data))

    json_to_normal = json.loads(json_data)
    print(json_to_normal)
    print(type(json_to_normal))
