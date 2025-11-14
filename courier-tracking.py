

class Courier:
    def __init__(self, tracking_id, sender, receiver):
        self.tracking_id = tracking_id
        self.sender = sender
        self.receiver = receiver
        self.status = "Pickup"

    def update_status(self, new_status):
        flow = {
            "Pickup": "In Transit",
            "In Transit": "Out for Delivery",
            "Out for Delivery": "Delivered"
        }

        if new_status == flow.get(self.status):
            self.status = new_status
            print(f"Status updated to: {self.status}")
        else:
            print(f"Invalid transition: {self.status} → {new_status}")

    def track(self):
        print("\n--- Tracking Information ---")
        print(f"Tracking ID: {self.tracking_id}")
        print(f"Sender: {self.sender}")
        print(f"Receiver: {self.receiver}")
        print(f"Current Status: {self.status}")
        print("-------------------------------\n")


# Demo
parcel = Courier("CT2025", "Devi Priyanka", "Keerthana")

parcel.track()
parcel.update_status("In Transit")
parcel.track()
parcel.update_status("Out for Delivery")
parcel.track()
parcel.update_status("Delivered")
parcel.track()
