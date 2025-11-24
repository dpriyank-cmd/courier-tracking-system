class PickupRequestDB:
    storage = []

    def insert(self, request):
        self.storage.append(request)
        print("Stored in database simulation:", self.storage)
db = PickupRequestDB()
db.insert({"pickup_id": 1, "status": "pending"})
