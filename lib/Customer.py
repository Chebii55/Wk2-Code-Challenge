class Customer:
    customers=[]
    
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.review=[]
        Customer.customers.append(self)

    @property
    def given_name(self):
        return self.first_name
    @given_name.setter
    def change_first_name(self,new_name):
        self.first_name=new_name

    @property
    def family_name(self):
        return self.last_name
    
    @family_name.setter
    def change_last_name(self,new_name):
        self.last_name=new_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def all(cls):
        return cls.customers
    
    def find_by_name(cls,name):
        for customer in cls.customers:
            if customer == name:
                return customer
        return None
    def find_all_by_given_name(cls, name):
        matching_customers = [customer for customer in cls.customers if customer == name]
        return matching_customers
        
    def restaurants(self):
        reviewed_restaurants = set()
        for review in self.review:
            reviewed_restaurants.add(review.get_restaurant().name)
        return list(reviewed_restaurants)
    
    def num_reviews(self):
        return len(self.review)


        
        