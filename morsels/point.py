

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    def __neq__(self, other):
        if isinstance(other, Point):
            return self.x != other.x and \
                self.y != other.y and \
                self.z != other.z
        return False
 
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and \
                self.y == other.y and \
                self.z == other.z
        return False
    
    def __add__(self, other):
        if not isinstance(other, Point):
            raise Exception('Does not support joining instance')
        return Point(
                x = self.x + other.x,
                y = self.y + other.y,
                z = self.z + other.z
            )
    
    def __sub__(self, other):
        if not isinstance(other, Point):
            raise Exception('Does not support joining instance')
        return Point(
                x = self.x - other.x,
                y = self.y - other.y,
                z = self.z - other.z
            )
    
    def __rmul__(self, scalar):
        return Point(self.x * scalar, 
                    self.y * scalar, 
                    self.z * scalar)
    
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z