class Book:
    # Initialize a new Book object
    # Requires a title and page_count
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    # Getter for page_count
    @property
    def page_count(self):
        return self._page_count

    # Setter for page_count with validation
    # Ensures page_count is an integer
    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    # Method to simulate turning a page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")