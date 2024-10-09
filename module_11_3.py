from pprint import pprint
import numpy as np
import inspect
def introspection_info(obj):
    type_obj = type(obj)
    attributes = []
    methods = []
    for attr_name in dir(obj):
        if '__'  not in attr_name:
            attributes.append(attr_name)
        else:
            methods.append(attr_name)
    module = __name__
    module_origin = inspect.getmodule(obj)
    is_float = isinstance(determinant, float)

    return {f'type: {type_obj}, attributes: {attributes}, methods: {methods}, module: {module}, '
            f'float: {is_float}, from module: {module_origin}'}

matrix = np.array([[5, 3, -2], [3, 2, -3], [4, 2, -1]])
determinant = np.linalg.det(matrix)

determinant_info = introspection_info(determinant)
pprint(determinant_info)