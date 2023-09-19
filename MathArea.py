import math
    
class MathShape():
    def __init__(self) -> None:
        pass
    
    def check_traingle(self, side1, side2, side3):
        if (side1**2 == side2**2 + side3**2) or (side2**2 == side1**2 + side3**2) or (side3**2 == side1**2 + side2**2): print('Это прямоугольный треугольник')
   
    def calculate_triangle_area(self, side_1, side_2, side_3):
        self.check_traingle(side_1, side_2, side_3)
        p = (side_1+side_2+side_3)/2
        return math.sqrt(p*(p-side_1)*(p-side_2)*(p-side_3))

    def calculate_circle_area(self, radius):
        return math.pi * radius * radius

    def calculate_shape_area(self, shape, **kwargs):

        if shape == "Круг":
            if "radius" in kwargs:
                return self.calculate_circle_area(kwargs["radius"])
            else:
                raise KeyError(f"Не указан радиус для фигуры {shape}")
            
        elif shape == "Треугольник":
            if "side1" in kwargs and "side2" in kwargs and "side3" in kwargs:
                return self.calculate_triangle_area(kwargs["side1"], kwargs["side2"], kwargs["side3"])
            else:
                raise KeyError(f"Не указаны стороны для фигуры {shape}")
        
        else:
            raise ValueError(f"Фигура {shape} не поддерживается")
        

'''

Чтобы добавить другую фигуру, достаточно добавить соответствующий блок elif shape == "Фигура": в метод calculate_shape_area, где "Фигура" - новый тип фигуры, и определить логику расчета площади для этого типа фигуры.

Например, чтобы добавить расчет площади прямоугольника, мы можем изменить код следующим образом:

elif shape == "Прямоугольник":
    if "width" in kwargs and "height" in kwargs:
        return kwargs["width"] * kwargs["height"]
    else:
        raise KeyError(f"Не указаны ширина и/или высота для фигуры {shape}")

        
'''