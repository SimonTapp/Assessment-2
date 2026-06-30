class Requisition:

    requisition_counter = 10000

    def __init__(self, date, staff_name, staff_id):

        self.date = date
        self.staff_name = staff_name
        self.staff_id = staff_id

        Requisition.requisition_counter += 1

        self.requisition_id = Requisition.requisition_counter

        self.date = date
        self.staff_name = staff_name
        self.staff_id = staff_id

        self.items = {}
        self.total = 0
        self.status = "Pending"
        self.approval_reference_number = "Not available"

    def add_item(self, item_name, item_price):

        self.items[item_name] = item_price
        self.total += item_price

    def requisition_approval(self):

        if self.total < 500:

            self.status = "Approved"
            self.approval_reference_number = "Approval Reference Number: " + str(self.staff_id) + str(self.requisition_id)[-3:]

        else:

            self.status = "Pending"
            self.approval_reference_number = "Approval Reference Number: Not available"





test = Requisition("29/06/2026", "Simon", "FNA234")
test.add_item(item_name="mouse", item_price=200)
test.add_item(item_name="keyboard", item_price=200)
test.requisition_approval()
print(test.items)
print(test.total)
print(test.approval_reference_number)
print(test.requisition_id)
print(test.staff_id)
print(test.staff_name)
print(test.status)