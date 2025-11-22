# Courier / Parcel Tracking System Simulation

class Parcel:
    def __init__(self, id):
        self.id = id
        self.status = "Order Placed"

    def update_status(self, new_status):
        allowed = ["Pickup", "In Transit", "Out for Delivery", "Delivered"]
        if new_status in allowed:
            self.status = new_status
        else:
            print("Invalid status")

    def __str__(self):
        return f"Parcel {self.id} → Status: {self.status}"


# Test Case
parcel = Parcel("CT-001")

print(parcel)
parcel.update_status("Pickup")
print(parcel)
parcel.update_status("In Transit")
print(parcel)
parcel.update_status("Out for Delivery")
print(parcel)
parcel.update_status("Delivered")
print(parcel)
