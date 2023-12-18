from Customer import Customer

class Restaurant:
    restaurants = []
    reviews = []
    customer_s = []

    def __init__(self, name):
        super().__init__()
        self.restaurant_name = name if isinstance(name, str) else print("Restaurant name should be a string")

    @property
    def name(self):
        return self.restaurant_name

    def add_review(self, review):
        self.review_content = review
        Restaurant.reviews.append(review)
        Restaurant.customer_s.append(self.customers)

    @classmethod
    def get_reviews(cls):
        return cls.reviews

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, name):
        self._customer = Customer(name)

    @classmethod
    def customers(cls):
        return list(cls.customer_s)
    
    def average_star_rating(cls):
        if not cls.reviews:
            return 0  # or handle as appropriate for your application
        return sum(cls.reviews) / len(cls.reviews)
