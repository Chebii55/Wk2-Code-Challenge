from Restaurant import Restaurant

class Review(Restaurant):
    reviews=[]
    customers=[]
    restaurants=[]
    def __init__(self,review):
        super().__init__()
        self.review=review
        Review.reviews.append(review)
        

    def rating(self):
        return self.review

    def all(cls):
        return cls.review
    
    @property
    def customer(self,first_name,last_name):
        self.name=f"{first_name} {last_name}"
        Review.customers.append(self)
        return self.name
    
    @property
    def restaurant(self,restaurant):
        self.restaurant=restaurant
        Review.restaurants.append(self)
        return self.restaurants
    
    def get_restaurant(self):
        return self.restaurant 

        