# Parcel Pickup Request Simulation

class PickupRequest:
    def __init__(self, parcel_id, user):
        self.parcel_id = parcel_id
        self.user = user
        self.status = "Pickup Requested"

    def confirm_pickup(self):
        self.status = "Pickup Confirmed"

    def cancel_request(self):
        self.status = "Cancelled"

    def __str__(self):
        return f"Parcel {self.parcel_id} → Request by {self.user} → Status: {self.status}"


# Test Case
request = PickupRequest("CT-110", "User123")

print(request)
request.confirm_pickup()
print(request)
request.cancel_request()
print(request)
