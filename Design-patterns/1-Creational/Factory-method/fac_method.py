from animals import Dog, Cat, Animal

class AnimalFactory:
    """Class used to instantiate the animal specification.
    """
    def create_an_animal(self, animal_type: str, animal_name: str) -> Animal:
        """Function used to instantiate an animal.

        Args:
            animal_type (str): Type of the animal that will be instantiated.
            animal_name (str): Name of the animal that will be instantiated.

        Raises:
            ValueError: When the type of the animal isn't valid.

        Returns:
            Animal: Returns the animal created.
        """
        animal_type = animal_type.strip().lower()
        
        if animal_type == "dog":
            print('An Dog was created.')
            return Dog(animal_name)

        elif animal_type == "cat":
            print('An Cat was created.')
            return Cat(animal_name)

        else:
            raise ValueError("Invalid animal type")