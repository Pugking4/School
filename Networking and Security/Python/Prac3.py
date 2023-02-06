cars = 100
space_in_cars = 4  # excluding the driver
drivers = 30 
passengers = 90

carsNeeded = drivers/space_in_cars
carsUnused = cars-carsNeeded
print(f"There are {carsUnused} cars unused.")
maxPassengers = cars/space_in_cars
print(f"You can drive a maxiumum of {maxPassengers} passengers.")
averagePassengers = passengers/cars
print(f"There is an average of {averagePassengers} passengers per car.")