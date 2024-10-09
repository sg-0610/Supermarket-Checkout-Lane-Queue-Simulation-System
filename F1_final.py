#F1:Done By->Hamza Ali Khan-001345840


import random
from datetime import datetime

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

class RegularLane(Lane):   #Initialize a Regular lane
    def __init__(self, lane_number):
        super().__init__("regular", lane_number, number_of_checkout_tills=1, lane_capacity=5)

class SelfServiceLane(Lane):   #Initialize a Self-service lane
    def __init__(self, lane_number):
        super().__init__("self_service", lane_number, number_of_checkout_tills=8, lane_capacity=15)


class Customer:   #Initialize a Customer with unique ID or number
    customer_count = 0
    def __init__(self):
        Customer.customer_count += 1
        self.customer_number = Customer.customer_count
        self.items_in_the_basket = random.randint(1, 30)
    def get_the_items_count(self):
        return self.items_in_the_basket

class LaneManager:
    def __init__(self):   #Initialize a Lane Manager for managing lanes
        self.regular_lanes = [RegularLane(i + 1) for i in range(5)]   #Generating 5 regular lane
        self.self_service_lane = SelfServiceLane(6)   #Generating a self-service lane
        self.lanes = self.regular_lanes + [self.self_service_lane]   #Combined list of regular and self service lanes
        self.customers_list = []

    def set_up_lanes(self):
        self.lanes[0].open()  # Open the first regular lane
        self.lanes[-1].open()  # Open the self-service lane

    def initiate_simulation(self):   #Starting the simulation by generating random no.of customers
        timestamp = datetime.now()
        number_of_customers = random.randint(1, 10)   #Generating random no.of cusomers upto 10

        print("\n### Assigning customers to lanes ###")

        for i in range(number_of_customers):
            customer = Customer()
            self.customers_list.append(customer)
            lane_type = "self_service" if random.choice([True, False]) else "regular"
            self.assign_customers_to_lanes(customer, lane_type)

        self.close_or_open_lanes()   # Close or open lanes as per the demand

    def assign_customers_to_lanes(self, customer, lane_type):   #Assigning generated customers to lanes of specified type
        open_lanes = [lane for lane in self.lanes if lane.lane_status == 'open' and lane.lane_type == lane_type]

        if open_lanes:
            selected_lane = random.choice(open_lanes)
            selected_lane.add_customer(customer)
            print(f"Customer C{customer.customer_number} assigned to {lane_type} lane {selected_lane.lane_number}.")
        else:
            print(f"No open {lane_type} lanes available. Customer C{customer.customer_number} not assigned.")

    def close_or_open_lanes(self):   #Open or close lanes based upon the no.of customers
        closed_lanes = [lane for lane in self.lanes if lane.lane_status == 'closed']

        for lane in closed_lanes:
            if len(lane.customers_list) > 0:
                print(f"{lane.lane_type.capitalize()} Lane {lane.lane_number} opened due to demand.")
                lane.open()

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

    def display_total_customers(self, timestamp):   #Display the total no.of customers waiting to checkout
        total_customers = sum([lane.get_total_number_of_customers() for lane in self.lanes])
        print(f"\nTotal number of customers waiting to checkout at {timestamp.strftime('%H:%M')} is: {total_customers}")

if __name__ == "__main__":
    lane_manager = LaneManager()   #Creating object or instance for class LaneManager
    lane_manager.set_up_lanes()

    print("### Lane status at the starting of simulation ###")   # Displaying the initial lane status
    for lane in lane_manager.lanes:
        lane.display_lane_status()

    lane_manager.initiate_simulation()   # Initiate the simulation and assign customers to lanes
    lane_manager.close_or_open_lanes()   # Close or open lanes based on the demand
    lane_manager.display_total_customers(datetime.now())   # Displaying the total number of customers waiting to checkout

    print("\n### Lane status after customer assignment ###")   # Displaying the lane status after customer assignment
    for lane in lane_manager.lanes:
        lane.display_lane_status()

### CODE ENDED ###

#Reference: Lecture slides, Youtube videos and ChapGPT used for getting ideas

