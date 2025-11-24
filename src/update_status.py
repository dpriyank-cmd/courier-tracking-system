

class Parcel:
    def __init__(self, parcel_id):
        self.parcel_id = parcel_id
        self.status = "Order Placed"

    def update_to_in_transit(self):
        allowed_previous = ["Order Placed", "Pickup"]
        
        if self.status in allowed_previous:
            self.status = "In Transit"
            print(f"🚚 Parcel {self.parcel_id} is now In Transit.")
        else:
            print(f"❌ Invalid transition: {self.status} → In Transit")

    def __str__(self):
        return f"Parcel {self.parcel_id} → Current Status: {self.status}"


# ---------- Test (Simulating the System Action) ----------
if __name__ == "__main__":
    parcel = Parcel("CT-1002")

    print(parcel)
    parcel.update_to_in_transit()
    print(parcel)
