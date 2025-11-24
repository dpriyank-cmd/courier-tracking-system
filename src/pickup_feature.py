# Parcel Pickup Request Feature

class PickupRequest:

    def __init__(self, parcel_id, pickup_location, user):
        self.parcel_id = parcel_id
        self.pickup_location = pickup_location
        self.user = user
        self.status = "Request Created"

    def update_status(self, new_status):
        allowed_status = ["Request Created", "Pickup Scheduled", "Agent Assigned", "Completed"]
        if new_status in allowed_status:
            self.status = new_status
        else:
            print("❌ Invalid status")

    def __str__(self):
        return f"[{self.parcel_id}] Pickup → {self.status} at {self.pickup_location} (User: {self.user})"


# ---- Test Case ----

pickup = PickupRequest("CT-002", "Hyderabad-Hitech City", "Priyanka")

print(pickup)
pickup.update_status("Pickup Scheduled")
print(pickup)
pickup.update_status("Agent Assigned")
print(pickup)
pickup.update_status("Completed")
print(pickup)
