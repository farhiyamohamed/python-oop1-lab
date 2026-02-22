class Coffee:
    # Initialize a new Coffee object
    # Requires size and price
    def __init__(self, size, price):
        self.size = size
        self.price = price

    # Getter for size
    @property
    def size(self):
        return self._size

    # Setter for size with validation
    # Ensures size is Small, Medium, or Large
    @size.setter
    def size(self, value):
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    # Method to tip for the coffee
    # Prints message and increases price by 1
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1