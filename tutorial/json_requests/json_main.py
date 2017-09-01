# coding=utf-8
import json

json_data = {
    "widget": {
        "debug": "on",
        "window": {
            "title": "Sample Konfabulator Widget",
            "name": "main_window",
            "width": 50.0,
            "height": 50.0
        },
        "image": {
            "src": "Images/Sun.png",
            "name": None,
            "hOffset": 250,
            "vOffset": 250,
            "alignment": "center"
        },
        "text": {
            "data": [1, 2, 3, 'hello', 'world'],
            "size": 36,
            "style": "bold",
            "name": "text1",
            "hOffset": 250,
            "vOffset": 100,
            "alignment": "center",
            "onMouseUp": False
        }
    }
}


class Company(object):
    def __init__(self, name):
        self.name = name

company = Company('博雅立方科技')
object_data = {
    'name': 'smite',
    'age': 18,
    'company': company
}

# dumps

json_data_string = json.dumps(json_data)
print json_data_string
print json.dumps(json_data, indent=4)

print json.dumps(json_data["widget"]["debug"])
print json.dumps(json_data["widget"]["image"]["name"])
print json.dumps(json_data["widget"]["window"]["width"])
print json.dumps(json_data["widget"]["text"]["data"])

try:
    print json.dumps(object_data)
except Exception as e:
    print e


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Company):
            return {'__custom_object__': True, 'class_name': 'Company', 'arg': obj.name}
        return super(self, CustomJsonEncoder).default(obj)

complex_string = json.dumps(object_data, cls=CustomJsonEncoder, indent=4)
print complex_string

# loads

print json.loads(json_data_string)
print cmp(json_data, json.loads(json_data_string)) == 0


def custom_json_decoder(dic):
    if '__custom_object__' in dic:
        return eval('{class_name}({arg})'.format(class_name=dic['class_name'], arg=repr(dic['arg'])))
    return dic


complex_data = json.loads(complex_string, object_hook=custom_json_decoder)
print complex_data["company"]
print complex_data["company"].name
