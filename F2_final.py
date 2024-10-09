#F2:Done By->Saksham Gupta-001314203

import random

class Customer:
    def __init__(self, identifier):
        self.identifier = identifier   #Giving each customer a numbering
        self.items_in_the_basket = random.randint(1, 30)   #Initialize the customer with a random no.of items in the basket ranging from 1 to 30
        self.has_lottery_ticket = False   #Initialize the customer with no lottery ticket in the beginning

    def get_the_items_count(self):
        return self.items_in_the_basket   #Counting the no.of items in the customer's basket

    def award_lottery_ticket(self):
        self.has_lottery_ticket = self.items_in_the_basket >=10 and random.choice([False, True])   #Awarding lottery ticket to customers having atleast 10 items in their baskets

    def calculate_checkout_time(self, fixed_time):
        return fixed_time * self.items_in_the_basket   #Calculating the checkout time of each customer

class CheckoutProcess:
    def __init__(self, customers):   #Initialize checkout process of the customers
        self.customers = customers

    def customer_details(self):   #Displaying the details of customers
        self.customers.award_lottery_ticket()
        lottery_message = "Lucky customer, wins a lottery ticket!" if self.customers.has_lottery_ticket else "Hard luck, no lottery ticket this time!"
        cashier_till_time = self.customers.calculate_checkout_time(4)
        self_service_till_time = self.customers.calculate_checkout_time(6)
        print(f"### Customer details ###\nC{self.customers.identifier} -> Items_in_basket: {self.customers.items_in_the_basket}, {lottery_message}")
        print(f"Time to process basket at cashier till: {cashier_till_time} Seconds")
        print(f"Time to process basket at self-service till: {self_service_till_time} Seconds")

object_customers = [Customer(identifier=i) for i in range(1,11)]
for customer in object_customers:
    object_checkout = CheckoutProcess(customer)
    object_checkout.customer_details()

### CODE ENDED ###


#Reference: Lecture slides, Youtube videos and ChapGPT used for getting ideas


