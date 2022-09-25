class Shop:
    def __init__(self, type, category, condition, rent):
        self.type = type
        self.condition = condition
        self.rent = rent
        self.category = category

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    
    @property
    def category(self, value):
        return self.__category

    @category.setter    
    def category(self, value):
        self.__category = value
        
    @property
    def condition(self):
        return self.condition
    
    @condition.setter
    def condition(self, value):
        self.condition = value

    @property
    def rent(self):
        return self.__rent

    @rent.setter
    def rent(self, value):
        if value < 0:
            raise ValueError("This rent is impossible")
        self.__rent = value