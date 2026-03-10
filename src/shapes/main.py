import numpy as np
from dataclasses import dataclass, field

@dataclass
class OrderedPair:
    x: float = 0.0
    y: float = 0.0

    # i get init and repr for free!
@dataclass
class Body:
    name: str = ""
    mass: float = 0.0

    # if we want to declare a default value that is a mutable object in Python (so something chaneagble and 
    # complex like a list or a custom class we defined), we need to use the "field" "default_factory"
    position: OrderedPair = field(default_factory=OrderedPair) #OrderedPair(0.0, 0.0)
    velocity: OrderedPair = field(default_factory=OrderedPair) #OrderedPair(0.0, 0.0)
    acceleration: OrderedPair = field(default_factory=OrderedPair) #OrderedPair(0.0, 0.0)
    radius: float = 0.0

class Rectangle:
    """
    Represents a 2D rectangle in a caretesian coordinate system.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        x1 (float): The x-coordinate of the top-left corner of the rectangle.
        y1 (float): The y-coordinate of the top-left corner of the rectangle.
        rotation (float): The rotation angle of the rectangle in radians.
    """

    def __init__(self, width: float = 0.0, height: float = 0.0, x1: float = 0.0, y1: float = 0.0, rotation: float = 0.0) -> None:
        
        # let's check the attributes are valid
        if isinstance(width, float) and width < 0:
            raise ValueError(f"Width must be non-negative float, got {width}")
        if isinstance(height, float) and height < 0:
            raise ValueError(f"Height must be non-negative float, got {height}.")
        if isinstance(rotation, float) and rotation < 0:
            raise ValueError(f"Rotation must be non-negative float got {rotation}")
        
        self.width = width
        self.height = height
        self.top_left: OrderedPair = OrderedPair(x1 + width/2, y1 + height/2)
        self.x1 = x1
        self.y1 = y1
        self.rotation = rotation

    def __repr__(self) -> str:
        return (f"Rectangle(width={self.width}, height={self.height}, x1={self.x1}, y1={self.y1}, rotation={self.rotation}, top_left={self.top_left})")
    
    def area(self) -> float:
        """
        Compute the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height
    
    def translate(self, dx: float, dy: float) -> None:
        """
        Translate the rectangle by a specified amount.

        Args:
            dx (float): The amount to translate in the x direction.
            dy (float): The amount to translate in the y direction.
        """
        self.x1 += dx
        self.y1 += dy
        self.center = OrderedPair(self.x1 + self.width/2, self.y1 + self.height/2)

class Circle:
    """
    Represents a 2D circle in a cartesian coordinate system.

    Attributes:
        radius (float): The radius of the circle.
        x1 (float): The x-coordinate of the center of the circle.
        y1 (float): The y-coordinate of the center of the circle.
    """

    def __init__(self, radius: float = 0.0, x1: float = 0.0, y1: float = 0.0, description: str = "Circles are round") -> None:

        # let's check the attributes are valid
        if radius < 0:
            raise ValueError("Radius must be non-negative.")

        self.x1 = x1
        self.y1 = y1
        self.radius = radius
        self.description = description
        # we DONT want to store something easy to compute from the definition. perhaps a method 
        # that uses the radius to compute the area
        # self.area = np.pi * self.radius**2

    def area(self) -> float:
        """
        Compute the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return np.pi * self.radius**2
    
    def translate(self, dx, dy) -> None:
        """
        Translate the circle by a specified amount.

        Args:
            dx (float): The amount to translate in the x direction.
            dy (float): The amount to translate in the y direction.
        """
        self.x1 += dx
        self.y1 += dy

    def __repr__(self) -> str:
        return (f"Circle(radius={self.radius}, x1={self.x1}, y1={self.y1}, description={self.description})")
    
def main():
    print("Object oriented programming, shapes!")

    # # their attributes are initialized with the default values, but let's change them:
    # my_circle = Circle()
    # my_circle.x1 = 1.0
    # my_circle.y1 = 3.0
    # my_circle.radius = 2.0

    # r = Rectangle()
    # r.x1 = 1.0
    # r.y1 = 3.0
    # r.width = 2.0
    # r.height = 3.0

    # let's actually use the constructors instead of editing the attributes directly
    my_circle = Circle(1.0, 3.0, 2.0)
    r = Rectangle(2.0, 3.0)
    r2 = Rectangle(2.0, 3.0)

    # let's print the objects. the __str__ or __repr__method is automatically called
    # https://www.codecademy.com/resources/docs/python/dunder-methods/str
    # since we DID not implement the __repr__ method for our class, print accesses this method.
    # if we hadn't the default would be a  human readable output of the object, 
    # in this case the objects' memory addresses
    
    print(f"str(r) = {str(r)}")
    print(f"repr(r) = {repr(r)}")
    print(f"r = {r}")
    print(f"my_circle = {my_circle}")

    # let's translate the objects


    print("------------")
    print("USING SHAPE METHODS")
    r.translate(1.0, 2.0)
    my_circle.translate(1.0, 2.0)
    print(f"r = {r}")
    print(f"my_circle = {my_circle}")
    print(f"r2 = {r2}")

    print("""\n
Uh-oh! We translated r but not r2, but r2's top_left changed as well. See the discussion in the
class "Body" defined above. Long story short, if we assign a mutable object to a class attribute,
then it will be shared between all the instances of that class... so, we need to use a decorator
to make the attribute not shared (i.e. immutable?)\n   
    """
    )

    
    b1 = Body()
    print(f"b1 = {b1}")
    b2 = Body("Snowperson", 100.0, OrderedPair(1.0, 2.0), OrderedPair(3.0, 4.0), OrderedPair(5.0, 6.0), 5.0)
    print(f"b2 = {b2}")
    b3 = Body("Snowperson", 100.0, OrderedPair(1.0, 2.0), OrderedPair(3.0, 4.0), OrderedPair(5.0, 6.0), 5.0)
    print(f"b3 = {b3}")
    b2.acceleration = OrderedPair(7.0e6, 8.0e6)

    b = Body(
        mass=1.989e30, 
        radius=6.96e8, 
        position=OrderedPair(0.0, 0.0), 
        velocity=OrderedPair(0.0, 0.0), 
        acceleration=OrderedPair(0.0, 0.0)
    )
    print(f"b = {b}")

    print("\nAFTER CHANGING b2, we have:")
    print(f"b1 = {b1}")
    print(f"b2 = {b2}")
    print(f"b3 = {b3}")

    

if __name__ == "__main__":
    main()
    print()