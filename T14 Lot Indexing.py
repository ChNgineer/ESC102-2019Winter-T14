import sys

class car:
    def __init__ (self, VIN, model, colour, year, index):
        self.VIN = str(VIN)
        self.model = model
        self.colour = colour
        self.year = year
        self.index = index

    def __str__ (self):
        return (self.VIN + "\nModel: " + self.model + "\nColour: " + self.colour + "\nYear: " + self.year + "\nParking: " + self.index + "\n")

VIN_library = {}

def insert_car():
    '''
    Insert a new car parked into the lot by a stocker.
    '''
    VIN = input("Enter new Vehicle Identification Number: \n")
    model = input("Enter new vehicle model: \n")
    colour = input("Enter new vehicle colour: \n")
    year = input("Enter new vehicle model-year: \n")
    index = input("Enter new vehicle parking index: \n")
    new_car = car(VIN, model, colour, year, index)
    if(VIN in VIN_library):
        print("Identical VIN detected in Library\n Check Vehicle for fraud\n")
    else:
        VIN_library[VIN] = new_car

def delete_car_by_VIN(VIN):
    '''
    Deletes the car object. Returns -1 if no car with the VIN is found. Returns -1 if deletion is aborted.
    '''
    if(VIN not in VIN_library):
        print("404: Car not found.\n")
        return -1
    else:
        prompt = input("Are you sure you want to delete " + VIN + "? (Y/N)\n").upper()
        while(True):
            if(prompt == "Y"):
                print("Car successfully deleted.\n")
                del VIN_library[VIN]
                return 1
            elif(prompt == "N"):
                print("Deletion aborted\n")
                return -1
            else:
                prompt = input().upper()

def replace_car_by_VIN(VIN):
    '''
    Replaces an existing car with a new car by using identical VIN.
    '''
    if(VIN not in VIN_library):
        print("404: Car not found.\n")
        return -1
    else:
        prompt = input("Are you sure you want to replace " + VIN + "? (Y/N)\n").upper()
        while(True):
            if(prompt == "Y"):
                del VIN_library[VIN]
                model = input("Enter new vehicle model: \n")
                colour = input("Enter new vehicle colour: \n")
                year = input("Enter new vehicle model-year: \n")
                index = input("Enter new vehicle parking index: \n")
                new_car = car(VIN, model, colour, year, index)
                VIN_library[new_car.VIN] = new_car
                return 1
            elif(prompt == "N"):
                print("Replacement aborted\n")
                return -1
            else:
                prompt = input().upper

def search_for_car_by_VIN(VIN):
    '''
    Returns the car object. Returns -1 if no car with the VIN is found.
    '''
    if(VIN not in VIN_library):
        print("404: Car not found.\n")
        return False
    else:
        print("Car successfully located:\n")
        print(VIN_library[VIN])
        return VIN_library[VIN]

def delete_car_by_index(index):
    '''
    Deletes the car object with matching index attribute. Returns -1 if no car has matcing index, or deletion is aborted.
    '''
    if(search_for_car_by_index(index) == False):
        print("Parking spot is either empty or out of bounds.\n")
        return -1
    else:
        prompt = input("Are you sure you want to delete the car at " + index + "? (Y/N)\n").upper()
        while(True):
            if(prompt == "Y"):
                print("Car successfully deleted.\n")
                del VIN_library[search_for_car_by_index(index).VIN]
                return 1
            elif(prompt == "N"):
                print("Deletion aborted\n")
                return -1
            else:
                prompt = input().upper()

def replace_car_by_index(index):
    '''
    Replaces an existing car with a new car by using identical index.
    '''
    if(search_for_car_by_index(index) == False):
        print("Parking spot is either empty or out of bounds.\n")
        return -1
    else:
        prompt = input("Are you sure you want to replace the car at " + index + "? (Y/N)\n").upper()
        while(True):
            if(prompt == "Y"):
                VIN = input("Enter new vehicle VIN: \n")
                del VIN_library[search_for_car_by_index(index).VIN]
                model = input("Enter new vehicle model: \n")
                colour = input("Enter new vehicle colour: \n")
                year = input("Enter new vehicle model-year: \n")
                new_car = car(VIN, model, colour, year, index)
                VIN_library[new_car.VIN] = new_car
                return 1
            elif(prompt == "N"):
                print("Replacement aborted\n")
                return -1
            else:
                prompt = input().upper

def search_for_car_by_index(index):
    '''
    Returns the car object. Returns -1 if no car with the index is found.
    '''
    car_list = list(VIN_library.values())
    for i in car_list:
        this_car = i
        if this_car.index == index :
            print("Car successfully located:\n")
            print(this_car)
            return this_car
    print("404: Car not found.\n")
    return False

def load_save():
    '''
    Reads attributes of car objects from a text file, and transports them to the VIN_library data segment.
    '''
    if(input("Are you sure you want to load a new save? Current data will be lost. (Y/N)\n").upper() == "Y"):
        VIN_library.clear()
        with open("save_file.txt") as f:
            data = f.readlines()
            for line in data:
                dat = line.strip().split('\t')
                VIN, model, colour, year, index = dat[0], dat[1], dat[2], dat[3], dat[4]
                VIN_library[VIN] = car(VIN, model, colour, year, index)
        return VIN_library

def save():
    '''
    Writes attributes of car objects from the VIN_library data segment to a new save file.
    '''
    f = open("save_file.txt", "w")
    print("gets here")
    for i in VIN_library.values():
        f.write(str(i.VIN) + "\t" + str(i.model) + "\t" + str(i.colour) + "\t" + str(i.year) + "\t" + str(i.index) + "\t\n")
    f.close()

if(__name__ == "__main__"):
    while(True):
        user = str(input("Enter a command:\n======================\ninsert\tdelete\nreplace\tsearch\nload\tsave\nquit\n======================\n"))
        if(user.lower() == "insert"):
            print("Inserting... Please follow the prompts.\n")
            insert_car()
        elif(user.lower() == "delete"):
            clarification = input("Delete by (VIN/index)?\n")
            while(True):
                if(clarification.upper() == "VIN"):
                    delete_car_by_VIN(input("Enter VIN to be deleted\n"))
                    break
                elif(clarification.lower() == "index"):
                    delete_car_by_index(input("Enter index of car to be deleted\n"))
                    break
                elif(clarification.lower() == "back"):
                    break
                else:
                    clarification = input("Please input (VIN/index/back)\n")
        elif(user.lower() == "replace"):
            clarification = input("Replace by (VIN/index)?\n")
            while(True):
                if(clarification.upper() == "VIN"):
                    replace_car_by_VIN(input("Enter VIN to be replaced\n"))
                    break
                elif(clarification.lower() == "index"):
                    replace_car_by_index(input("Enter index of car to be replaced\n"))
                    break
                elif(clarification.lower() == "back"):
                    break
                else:
                    clarification = input("Please input (VIN/index/back)\n")
        elif(user.lower() == "search"):
            clarification = input("Search by (VIN/index)?\n")
            while(True):
                if(clarification.upper() == "VIN"):
                    search_for_car_by_VIN(input("Enter VIN to search\n"))
                    break
                elif(clarification.lower() == "index"):
                    search_for_car_by_index(input("Enter index to search\n"))
                    break
                elif(clarification.lower() == "back"):
                    break
                else:
                    clarification = input("Please input (VIN/index/back)\n")
        elif(user.lower() == "load"):
            clarification = input("Would you like to override your current work? (Y/N)?\n")
            while(True):
                if(clarification.upper() == "Y"):
                    load_save()
                    break
                elif(clarification.upper() == "N"):
                    break
                else:
                    clarification = input("Please answer (Y/N)\n")
        elif(user.lower() == "save"):
            clarification = input("Would you like to overwrite your previous save file? (Y/N)?\n")
            save_state = 0
            while(True):
                if(clarification.upper() == "Y"):
                    print("Saving... Please do not turn off your device!\n")
                    save()
                    save_state = 1
                    break
                elif(clarification.upper() == "N"):
                    break
                else:
                    clarification = input("Please answer (Y/N)\n")
            save_and_quit = input("Would you like to quit after saving? (Y/N)?\n")
            while(save_state == 1):
                if(save_and_quit.upper() == "Y"):
                    sys.exit()
                elif(save_and_quit.upper() == "N"):
                    break
                else:
                    save_and_quit = input("Please answer (Y/N)\n")
        elif(user.lower() == "quit"):
            clarification = input("Are you sure you want to quit (Y/N)?\n")
            while(True):
                if(clarification.upper() == "Y"):
                    sys.exit("Force Quit Program")
                elif(clarification.upper() == "N"):
                    break
                else:
                    clarification = input("Please answer (Y/N)\n")
        else:
            user = input("Please select a command shown above.\n")