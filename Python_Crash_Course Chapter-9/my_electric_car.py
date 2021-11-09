
from electric_car2 import ElectricCar


my_tesla = ElectricCar("lesla", "kd-f-d9", 2020)

print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()