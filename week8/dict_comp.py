dct = {"pen": 10, "pencil": 5, "eraser": 6,"sharpner":7,"scale":11}
dct.update({k: v + 3 for k, v in dct.items()})
print("Dictionary after updating:", dct)