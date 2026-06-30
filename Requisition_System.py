# Creates a class called Requisition to store the details for each requisition
class Requisition:

    # Creates a class variable for the requisition ID counter
    requisition_counter = 10000

    # Creates the init method and takes in the date, staff name, and staff ID
    def __init__(self, date, staff_name, staff_id):

        # Stores the date, staff name, and staff ID inside the object
        self.date = date
        self.staff_name = staff_name
        self.staff_id = staff_id

        # Adds 1 to the requisition counter each time a new object is created
        Requisition.requisition_counter += 1

        # Gives the requisition its own ID using the counter
        self.requisition_id = Requisition.requisition_counter

        # Stores the date, staff name, and staff ID as object attributes
        self.date = date
        self.staff_name = staff_name
        self.staff_id = staff_id

        # Creates an empty dictionary to store any items added to the requisition
        self.items = {}

        # Sets the starting total to 0 before any items are added
        self.total = 0

        # Sets the starting status to Pending before the requisition is approved
        self.status = "Pending"

        # Sets the approval reference number to not available until the requisition is approved
        self.approval_reference_number = "Approval Reference Number: Not available"

    # Creates a method to add an item and price to the requisition
    def add_item(self, item_name, item_price):

        # Adds the item name and item price to the items dictionary
        self.items[item_name] = item_price

        # Adds the item price to the total
        self.total += item_price

    # Creates a method to check if the requisition should be approved automatically
    def requisition_approval(self):

        # Checks if the total is less than 500
        if self.total < 500:

            # If the total is less than 500, the requisition is approved
            self.status = "Approved"

            # Creates the approval reference number using the staff ID and last 3 digits of the requisition ID
            self.approval_reference_number = str(self.staff_id) + str(self.requisition_id)[-3:]

        else:

            # If the total is 500 or more, the requisition stays pending
            self.status = "Pending"

            # Keeps the approval reference number as not available
            self.approval_reference_number = "Not available"

    # Creates a method so a manager can respond to a pending requisition
    def requisition_response(self, response):

        # Only allows the response to work if the requisition is still pending
        if self.status == "Pending":

            # If the manager approves it, the status changes to Approved
            if response == "Approved":
                self.status = "Approved"

                # Creates the approval reference number once it has been approved
                self.approval_reference_number = str(self.staff_id) + str(self.requisition_id)[-3:]

            # If the manager does not approve it, the status changes to Not Approved
            elif response == "Not Approved":
                self.status = "Not Approved"

                # Keeps the approval reference number as not available
                self.approval_reference_number = "Not available"

    # Creates a method to display the requisition details
    def display_requisition(self):

        # Prints all the details stored inside the requisition object
        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $" + str(self.total))
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference_number)
        print()


# Creates a class to store the requisitions and display the statistics
class RequisitionStatistics:

    # Creates the init method for the statistics class
    def __init__(self):

        # Creates an empty list to store all of the requisition objects
        self.statistics = []

        # Sets all the counters to 0 before any requisitions are counted
        self.approved_requisitions = 0
        self.not_approved_requisitions = 0
        self.pending_requisitions = 0

    # Creates a method to add requisition objects into the statistics list
    def add_requisitions(self, requisition):

        # Adds the requisition object to the statistics list
        self.statistics.append(requisition)

    # Creates a method to count and display the requisition statistics
    def requisition_statistics(self):

        # Loops through each requisition object in the statistics list
        for each_requisition in self.statistics:

            # Checks if the requisition status is Approved
            if each_requisition.status == "Approved":

                # Adds 1 to the approved counter
                self.approved_requisitions += 1

            # Checks if the requisition status is Not Approved
            if each_requisition.status == "Not Approved":

                # Adds 1 to the not approved counter
                self.not_approved_requisitions += 1

            # Checks if the requisition status is Pending
            if each_requisition.status == "Pending":

                # Adds 1 to the pending counter
                self.pending_requisitions += 1

        # Prints the total number of requisitions stored in the list
        print("Total Requisitions: ", len(self.statistics))

        # Prints the total number of approved requisitions
        print("Approved Requisitions: " + str(self.approved_requisitions))

        # Prints the total number of not approved requisitions
        print("Not Approved Requisitions: " + str(self.not_approved_requisitions))

        # Prints the total number of pending requisitions
        print("Pending Requisitions: " + str(self.pending_requisitions))


# Creates the first test requisition object
test = Requisition("29/06/2026", "Simon", "FNA233")

# Adds two items to the first requisition
test.add_item(item_name="Mouse", item_price=200)
test.add_item(item_name="Keyboard", item_price=300)

# Checks if the first requisition should be approved automatically
test.requisition_approval()

# Tests the  response method
test.requisition_response("Approved")


# Creates the second test requisition object
test_2 = Requisition("30/06/2026", "Jill", "FNA234")

# Adds two items to the second requisition
test_2.add_item(item_name="mouse", item_price=200)
test_2.add_item(item_name="keyboard", item_price=400)

# Checks if the second requisition should be approved automatically
test_2.requisition_approval()

# Tests the response method by marking it as Not Approved
test_2.requisition_response("Not Approved")


# Creates the third test requisition object
test_3 = Requisition("1/07/2026", "Bob", "FNA235")

# Adds two items to the third requisition
test_3.add_item(item_name="mouse", item_price=200)
test_3.add_item(item_name="keyboard", item_price=200)

# Checks if the third requisition should be approved automatically
test_3.requisition_approval()

# Tests what happens if the response is Pending
test_3.requisition_response("Pending")


# Creates the fourth test requisition object
test_4 = Requisition("2/07/2026", "Ben", "FNA236")

# Adds two items to the fourth requisition
test_4.add_item(item_name="mouse", item_price=500)
test_4.add_item(item_name="keyboard", item_price=200)

# Checks if the fourth requisition should be approved automatically
test_4.requisition_approval()

# Tests what happens if the response is Pending
test_4.requisition_response("Pending")


# Creates the fifth test requisition object
test_5 = Requisition("3/07/2026", "Glen", "FNA237")

# Adds two items to the fifth requisition
test_5.add_item(item_name="mouse", item_price=500)
test_5.add_item(item_name="keyboard", item_price=200)

# Checks if the fifth requisition should be approved automatically
test_5.requisition_approval()

# Tests the response method by marking it as Approved
test_5.requisition_response("Approved")


# Displays all of the requisitions one by one
test.display_requisition()
test_2.display_requisition()
test_3.display_requisition()
test_4.display_requisition()
test_5.display_requisition()


# Creates the statistics object
statistics = RequisitionStatistics()

# Adds the requisition objects into the statistics list
statistics.add_requisitions(test)
statistics.add_requisitions(test_2)
statistics.add_requisitions(test_3)
statistics.add_requisitions(test_4)

# Displays the requisition statistics
statistics.requisition_statistics()