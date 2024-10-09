#F3: Done together by integrating the codes of F1 and F2 and also asigning a new class 'SimulationSystem'

import random
from datetime import datetime, timedelta
import time

class Lane:
    def __init__(self, lane_type, lane_number, number_of_checkout_tills, lane_capacity):   #Initialize a lane with some parameters
        self.lane_type = lane_type
        self.lane_number = lane_number
        self.number_of_checkout_tills = number_of_checkout_tills
        self.lane_capacity = lane_capacity
        self.lane_status = 'closed'
        self.customers_list = []

    def close(self):   #Changing the lane status to close
        self.lane_status = 'closed'

    def open(self):   #Changing the lane status to open
        self.lane_status = 'open'

    def add_customer(self, customer):   #Adding customers to lanes if it is not full
        if len(self.customers_list) < self.lane_capacity:
            self.customers_list.append(customer)
        else:
            print(f"Lane {self.lane_number} is full. Customer C{customer.customer_number} not assigned.")   #Displaying a message if the lane is full

    def remove_customer(self):   #Removing the first of the lane after billing
        if self.customers_list:
            removed_customer = self.customers_list.pop(0)
            print(f"Customer C{removed_customer.customer_number} removed from {self.lane_type} lane {self.lane_number} after checkout.")
            return removed_customer

    def get_total_number_of_customers(self):   #Get the total no.of customers
        return len(self.customers_list)

    def display_lane_status(self):   #Display lane status
        customer_symbols = " * " * len(self.customers_list)
        lane_info = f"{self.lane_type.capitalize()} Lane {self.lane_number} ({self.lane_status})"
        print(f"{lane_info.ljust(15)} -> {customer_symbols}")

class RegularLane(Lane):
    def __init__(self, lane_number):   #Initialize a RegularLane, inherited from Lane
        super().__init__("regular", lane_number, number_of_checkout_tills=1, lane_capacity=5)

class SelfServiceLane(Lane):
    def __init__(self, lane_number):   #Initialize a SelfServiceLane, inherited from Lane
        super().__init__("self_service", lane_number, number_of_checkout_tills=8, lane_capacity=15)

class Customer:
    customer_count = 0

    def __init__(self):   #Initialize a customer with a unique ID or number
        Customer.customer_count += 1
        self.customer_number = Customer.customer_count
        self.items_in_the_basket = random.randint(1, 30)

    def get_the_items_count(self):   #Counting the no.of items in the customer's basket
        return self.items_in_the_basket

    def award_lottery_ticket(self):   #Awarding lottery ticket to customers having atleast 10 items in their baskets
        self.has_lottery_ticket = self.items_in_the_basket >= 10 and random.choice([False, True])

    def calculate_checkout_time(self, fixed_time):   #Calculating the checkout time of each customer
        return fixed_time * self.items_in_the_basket

class LaneManager:
    def __init__(self):   #Initialize a LanaManager with regular and self-service lanes
        self.regular_lanes = [RegularLane(i + 1) for i in range(5)]
        self.self_service_lane = SelfServiceLane(6)
        self.lanes = self.regular_lanes + [self.self_service_lane]
        self.customers_list = []

    def set_up_lanes(self):
        self.lanes[0].open()  # Open the first regular lane
        self.lanes[-1].open()  # Open the self-service lane

    def display_lane_status(self):   #Displaying the status of all lanes
        print("\n### Lane Status ###")
        for lane in self.lanes:
            lane.display_lane_status()

    def initiate_simulation(self):   #Start the simulation by generating random no.of customers
        timestamp = datetime.now()
        number_of_customers = random.randint(1, 10)

        for _ in range(number_of_customers):
            customer = Customer()
            self.customers_list.append(customer)
            lane_type = "self_service" if random.choice([True, False]) else "regular"
            self.assign_customers_to_lanes(customer, lane_type)

    def assign_customers_to_lanes(self, customer, lane_type):   #Assigning the generated customers to lanes of specified type
        open_lanes = [lane for lane in self.lanes if lane.lane_status == 'open' and lane.lane_type == lane_type]

        if open_lanes:
            selected_lane = random.choice(open_lanes)
            selected_lane.add_customer(customer)
            print(f"Customer C{customer.customer_number} assigned to {lane_type} lane {selected_lane.lane_number}.")
        else:
            print(f"No open {lane_type} lanes available. Customer C{customer.customer_number} not assigned.")

    def close_or_open_lanes(self):   #Open or close lanes based upon the no.of customers
        for lane in self.lanes:
            if lane.lane_status == 'open':
                if len(lane.customers_list) == 0:
                    print(f"{lane.lane_type.capitalize()} Lane {lane.lane_number} closed due to low demand.")
                    lane.close()
                elif len(lane.customers_list) == lane.lane_capacity:   #Open another lane if the existing open lane is full
                    new_lane_type = "regular" if lane.lane_type == "regular" else "self_service"
                    new_lane_number = len(self.lanes) + 1
                    new_lane = RegularLane(new_lane_number) if new_lane_type == "regular" else SelfServiceLane(new_lane_number)
                    self.lanes.append(new_lane)
                    print(f"{new_lane_type.capitalize()} Lane {new_lane_number} opened due to high demand.")

    def display_total_customers(self, timestamp):   #Displaying the total no.of customers waiting to checkout
        total_customers = sum([lane.get_total_number_of_customers() for lane in self.lanes])
        print(f"\nTotal number of customers waiting to checkout at {timestamp.strftime('%H:%M')} is: {total_customers}")

class CheckoutProcess:
    def __init__(self, customer):   #Initialize CheckoutProcess with a customer
        self.customer = customer

    def customer_details(self):   #Displaying the details of each customer
        self.customer.award_lottery_ticket()
        lottery_message = "Lucky customer, wins a lottery ticket!" if self.customer.has_lottery_ticket else "Hard luck, no lottery ticket this time!"
        cashier_till_time = self.customer.calculate_checkout_time(4)
        self_service_till_time = self.customer.calculate_checkout_time(6)
        print(f"### Customer details ###\nC{self.customer.customer_number} -> Items_in_basket: {self.customer.items_in_the_basket}, {lottery_message}")
        print(f"Time to process basket at cashier till: {cashier_till_time} Seconds")
        print(f"Time to process basket at self-service till: {self_service_till_time} Seconds")

class SimulationSystem:
    def __init__(self):   #Initialize SimulationSystem with a Lanemanager
        self.lane_manager = LaneManager()
        self.customers = []
        self.start_time = datetime.now()
        self.simulation_duration = timedelta(seconds=30)  # Set the simulation duration to 30 seconds
        self.time_interval = 10  # Set the time interval to desired no.of seconds between simulations

    def initiate_simulation(self):   #Set up lanes and display initial lane status
        self.lane_manager.set_up_lanes()
        self.lane_manager.display_lane_status()

        while datetime.now() - self.start_time < self.simulation_duration:
            self.run_continuous_simulation()
            time.sleep(self.time_interval)  # Pause between simulations
        self.end_simulation()

    def run_continuous_simulation(self):
        print("\n### Continuous Simulation Running ###")
        num_customers = random.randint(1, 10)  # Adjust the number of customers as needed

        for _ in range(num_customers):
            customer = Customer()
            self.customers.append(customer)
            lane_type = "self_service" if random.choice([True, False]) else "regular"
            self.lane_manager.assign_customers_to_lanes(customer, lane_type)

        self.lane_manager.display_lane_status()   #Display lane status after customer assignment
        self.lane_manager.close_or_open_lanes()
        self.lane_manager.display_total_customers(datetime.now())

        for customer in self.customers:   #Processing each customer's checkout details
            checkout_process = CheckoutProcess(customer)
            checkout_process.customer_details()
            print("\n")
            time.sleep(1)  # Pause between customers for readability

    def end_simulation(self):
        print("\n### Simulation Ended ###")

if __name__ == "__main__":   #Create and run the simulation
    simulation_system = SimulationSystem()
    simulation_system.initiate_simulation()

### CODE ENDED ###


#Reference: Lecture slides, Youtube videos and ChapGPT used for getting ideas




