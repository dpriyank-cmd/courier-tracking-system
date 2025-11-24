from pickup_form import create_pickup_form
from pickup_api import PickupRequestAPI
from pickup_db import PickupRequestDB

def process_pickup_workflow():
    print("\n----- PROCESSING PICKUP REQUEST -----")
    data = {"name": "Priya", "address": "Vizag", "date": "2025-11-22"}

    api = PickupRequestAPI()
    db = PickupRequestDB()

    if api.save_request(data):
        db.insert(data)
        print("Pickup Workflow Completed Successfully")

# Test
process_pickup_workflow()
