class PickupRequestAPI:
    def save_request(self, data):
        print(f"Saving to backend: {data}")
        return True

# Test
api = PickupRequestAPI()
api.save_request({"name":"Priya","address":"Hyderabad","date":"2025-11-20"})
