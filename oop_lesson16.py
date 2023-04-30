from dataclasses import dataclass

@dataclass
class Rectangle():
    width: int
    height : int

    # methods:
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return (self.width+self.height)*2
    
figure = Rectangle(25,4)

print(figure.area())
print(figure.perimeter())


@dataclass
class User:
    name: str
    age: int
    language : list

    def welcome(self):
        if self.language == 'Chinese':
            print(f'NIHAO{self.name}')
        if self.language == 'Kazakh':
            print(f'SALEM{self.name}')

student = User('Dameli', 24,'Kazakh')

student.welcome()

