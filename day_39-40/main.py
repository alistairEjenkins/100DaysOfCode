#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from customer import Customer
from pprint import pprint


dm = DataManager()
fs = FlightSearch()



# get prices data
sheet_data = dm.get_destination_data()
print(sheet_data)

# if no IATA code get IATA code
for index,destination in enumerate(sheet_data):
    if not destination[1]:
        destination[1] = fs.get_iata(destination[0])
        #update IATA codes on prices worksheet
        dm.set_destination_data(destination,index, column='IATA')

for index, destination in enumerate(sheet_data):
#     try:
#         flight_details = fs.get_cheapest_flight(destination[1], destination[2])
#     except:
    print("no direct flights")
    flight_details = fs.get_cheapest_flight(destination[1], destination[2], stop_overs=1)
    # else:
    #     print("nxt dest")
        # print(f'flights found: {destination[0]} £{flight_details[0]}')
        # destination[2] = flight_details[0]
        # # update prices worksheet to include new lowest price
        #dm.set_destination_data(destination, index, column="lowest price")
        #fd = FlightData(flight_details)
        # print(fd)
        # # nm = NotificationManager(fd)







