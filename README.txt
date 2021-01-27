================================================================================================
NOTES
------------------------------------------------------------------------------------------------
This is a prototype of a solution to be implemented.
The goal of this prototype is to demonstrate the benefits of a digital organizational structure
such as dictionaries and hash tables in automotive inventory management. In its current state,
the prototype is not meant for commercial use and is for educational purposes only. As of its
latest iteration, the interface of this model is still limited to the I/O terminal which it is
run in. This will be addressed in later iterations where a proper GUI will be implemented to
assist in increasing the usability of the model.
================================================================================================
AUTHORS: Ryan Chen, Martin Licht, Richard Marchelletta
================================================================================================
CONTENTS
------------------------------------------------------------------------------------------------
INSERT

Prompts the user 5 times for information regarding the car to be inserted into the dictionary.
1. Vechicle Identification Number
2. Vehicle model
3. Vehicle colour
4. Vehicle year of commission
5. Vehicle parking lot index
These 5 attributes are then stored in a "car" class, which is then stored in a dictionary
initialized upon the start of the program.
------------------------------------------------------------------------------------------------
SEARCH

prompts the user for either the VIN or the parking index of the car, and returns the "car" class
which contains the remaining 4 attributes of the car, which are then printed. The search
function via VIN for vehicles is the most likely to be used by the dealer to identify where the
car is stored. The VIN is unique to each vehicle, and should be in the possession of the 
dealership. Upon entering the VIN of the vehicle, the parking lot index is presented to the
technician.
------------------------------------------------------------------------------------------------
REPLACE

prompts the user for either the VIN or the parking index of the car, and allows the user to
modify information on the corresponding car. This is designed for the user to correct mistakes
in entries.This function can also be used in order to modify the stock, if inventory is shifted
to different parking spaces than specified.
------------------------------------------------------------------------------------------------
DELETE

prompts the user for either the VIN or the parking index of the car, and will remove the car
corresponding object from the dictionary. This is meant to be used when sales occur or when
inventory goes missing.
------------------------------------------------------------------------------------------------
SAVE

Creates or overrides a text file under "save_file.txt" and writes the information of "car"
objects currentlyin the dictionary into the file in the order: VIN, model, colour, year, index.
These attributes are separated via \t (tab characters). They are written into the file without
headers. This may require additional training to get the hang of over time, if users were to
read directly from the text file in order to view their entire inventory at once.
------------------------------------------------------------------------------------------------
LOAD

Reads from a previous save file named "save_file.txt" and puts it in the dictionary, where it
can be modified. by other functions.
================================================================================================