Supermarket Checkout Lane Queue Simulation

Overview

This project simulates the operations of a supermarket checkout lane management system using Python. The system models customer queues at both regular and self-service checkout lanes, dynamically managing lane operations based on customer traffic. The goal is to simulate real-world scenarios where supermarket managers need to optimize queue lengths, reduce wait times, and open or close lanes depending on the number of customers.

This project showcases object-oriented programming principles, event-driven simulation, and Python-based implementation of queue management, all executed in a command-line environment.

Features

	•	Dynamic Lane Management: Automatically opens and closes lanes based on customer demand and queue length.
	•	5 regular lanes with cashier-operated tills.
	•	1 self-service lane with 8 unmanned tills.
	•	Customer Queue Simulation: Customers are generated randomly, each with a shopping basket containing a variable number of items.
	•	Customer Assignment: Customers are assigned to lanes based on the number of items in their basket.
	•	Customers with less than 10 items prefer self-service lanes.
	•	Regular lanes are open to all customers and can be used when self-service lanes are full.
	•	Checkout Process: The time required to process each customer is proportional to the number of items in their basket. Customers leave the queue once processed.
	•	Queue Balancing: Customers are moved between lanes to balance waiting times. Idle or underused lanes may be closed to save resources.
	•	Simulation Events:
	•	Enter Lane: Customers join a lane.
	•	Checkout: Customers at the front of the lane are processed.
	•	Leave Lane: Customers exit the lane once processed.
	•	Open Lane: A new lane is opened if demand increases.
	•	Close Lane: An underused lane is closed.
Project Structure
.
├── main.py                # Main program entry point
├── customer.py            # Customer class and related functions
├── lane.py                # Lane class for regular and self-service lanes
├── checkout_system.py      # Checkout system to manage lane operations
├── README.md              # Project documentation
└── requirements.txt       # List of dependencies (if any)

Installation and Setup
1) Clone the repository
git clone https://github.com/yourusername/supermarket-queue-simulation.git
cd supermarket-queue-simulation
2) Install Dependencies (if applicable)
pip install -r requirements.txt
3) Run the Simulation
python main.py

Usage

	•	The simulation will automatically generate a random number of customers and assign them to available lanes.
	•	As the simulation runs, it will dynamically open or close lanes depending on the number of customers waiting.
	•	The user can monitor the checkout process through the command-line output, where customer queues and lane statuses are displayed.

 Example
 Here is an example of how the system operates:

 [INFO] 2 customers generated.
[INFO] Customer 1 (5 items) assigned to self-service lane.
[INFO] Customer 2 (15 items) assigned to regular lane.
[INFO] Self-service lane processing customer 1.
[INFO] Regular lane processing customer 2.
[INFO] Regular lane opened to accommodate more customers.

Future Improvements

	•	Implement a graphical user interface (GUI) for better visualization of lane queues and customer movements.
	•	Add more dynamic behaviors such as real-time customer entry and leaving based on service times.
	•	Introduce metrics for analyzing average waiting times, lane utilization, and customer satisfaction.

 Contributions

Contributions are welcome! Please follow these steps if you’d like to contribute to this project:

	1.	Fork the repository.
	2.	Create a new feature branch: git checkout -b feature-branch-name.
	3.	Commit your changes: git commit -m 'Add some feature'.
	4.	Push to the branch: git push origin feature-branch-name.
	5.	Open a pull request.

 Contact

Feel free to reach out with any questions or suggestions:

	•	Saksham Gupta: sg0165t@gre.ac.uk
	•	GitHub: github.com/sg-0610
