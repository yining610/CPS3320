class Person:
    '''Inclass Tutorial'''

    # Constructor
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def input_person_data(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    
    def get_person_data(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Weight: {self.weight}')
        print(f'Height: {self.height}')

def main():
    # initiate the variables
    person_1 = Person('Yining', '22', '70', '180')
    person_2 = Person('Zirui', '21', '60', '180')
    person_1.get_person_data()
    person_2.get_person_data()

    # Update the variable
    person_1.input_person_data('King','23','71','181')
    person_2.input_person_data('Rudy', '22', '61','181')
    person_1.get_person_data()
    person_2.get_person_data()

if __name__=="__main__":
    main()