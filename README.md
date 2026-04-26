Smart Study Tutoring Services - Multi-Agent SystemProject Overview
-This project is an implementation of a One-Person Company (OPC) managed through a Multi-Agent System (MAS).
The business, Smart Study Tutoring Services, provides quality online tutoring in science, math, and programming.
By utilizing specialized digital agents, a single Founder can efficiently manage business operations, scheduling, and marketing without the need for additional human staff.
System ArchitectureThe system is built using Object-Oriented Programming (OOP) principles in Python.
It features a central Founder object that interacts with three specialized digital agents to facilitate decision-making.
Digital Agents & ResponsibilitiesFinance Agent: Manages fee structures, student payments, and financial reporting.
Marketing Agent: Handles social media promotion and student recruitment strategies.
Operations Agent: Coordinates tutoring schedules and session bookings.
Technical ImplementationThe project demonstrates the following OOP concepts:
Inheritance: Specific agents inherit core functionalities from a base Agent class.
Encapsulation: Business data is securely managed within Task and Recommendation objects.
Interaction Flow: The Founder creates Tasks, which are processed by Agents to produce Recommendations for a final business decision.
How to Run\Open the provided Google Colab link. Run the code cells to see the interaction between the Founder and the digital agents.The console will output the task processing logs and the Founder's final decision.
