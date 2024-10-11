from collections import deque

class Courier:
    def __init__(self, courier_id, name):
        self.courier_id = courier_id
        self.name = name

    def __str__(self):
        return f"Courier ID: {self.courier_id}, Name: {self.name}"


class Parcel:
    def __init__(self, parcel_id, destination):
        self.parcel_id = parcel_id
        self.destination = destination

    def __str__(self):
        return f"Parcel ID: {self.parcel_id}, Destination: {self.destination}"


class Action:
    def __init__(self, action_type, courier, parcel):
        self.action_type = action_type  
        self.courier = courier
        self.parcel = parcel


class CourierServiceManager:
    def __init__(self):
        self.available_couriers = []  
        self.delivery_queue = deque()  
        self.undo_stack = []  

   
    def add_courier(self, courier_id, name):
        courier = Courier(courier_id, name)
        self.available_couriers.append(courier)
        print(f"Added Courier: {courier}")

    
    def add_parcel(self, parcel_id, destination):
        parcel = Parcel(parcel_id, destination)
        self.delivery_queue.append(parcel)
        print(f"Added Parcel to delivery queue: {parcel}")

    
    def assign_courier(self):
        if not self.available_couriers:
            print("No available couriers to assign.")
            return

        if not self.delivery_queue:
            print("No parcels to deliver.")
            return

        
        courier = self.available_couriers.pop(0)
        parcel = self.delivery_queue.popleft()

        
        self.undo_stack.append(Action("assign", courier, parcel))

        print(f"Assigned {courier.name} to deliver {parcel}")

    
    def undo_last_action(self):
        if not self.undo_stack:
            print("No actions to undo.")
            return

        
        last_action = self.undo_stack.pop()

        if last_action.action_type == "assign":
            
            self.delivery_queue.appendleft(last_action.parcel)
            self.available_couriers.insert(0, last_action.courier)
            print(f"Undo: Unassigned {last_action.courier.name} from delivering {last_action.parcel}")

    
    def show_available_couriers(self):
        if not self.available_couriers:
            print("No available couriers.")
        else:
            print("Available Couriers:")
            for courier in self.available_couriers:
                print(courier)

    
    def show_pending_parcels(self):
        if not self.delivery_queue:
            print("No parcels in the queue.")
        else:
            print("Pending Parcels:")
            for parcel in self.delivery_queue:
                print(parcel)

    
    def show_undo_stack(self):
        if not self.undo_stack:
            print("No actions to undo.")
        else:
            print("Undo History:")
            for action in self.undo_stack:
                print(f"{action.courier.name} was assigned to {action.parcel}")



def main():
    manager = CourierServiceManager()

    while True:
        print("\nCourier Service Management")
        print("1. Add Courier")
        print("2. Add Parcel to Delivery Queue")
        print("3. Assign Courier to Parcel")
        print("4. Undo Last Courier Assignment")
        print("5. Show Available Couriers")
        print("6. Show Pending Parcels")
        print("7. Show Undo History")
        print("8. Exit")
        choice = input("Choose an option (1-8): ")

        if choice == "1":
            courier_id = input("Enter Courier ID: ")
            name = input("Enter Courier Name: ")
            manager.add_courier(courier_id, name)

        elif choice == "2":
            parcel_id = input("Enter Parcel ID: ")
            destination = input("Enter Parcel Destination: ")
            manager.add_parcel(parcel_id, destination)

        elif choice == "3":
            manager.assign_courier()

        elif choice == "4":
            manager.undo_last_action()

        elif choice == "5":
            manager.show_available_couriers()

        elif choice == "6":
            manager.show_pending_parcels()

        elif choice == "7":
            manager.show_undo_stack()

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
