class CreatePass:
    pass


obj1 = CreatePass()
print(obj1)

class Sum():
    def add(self, a, b):
        return a+b

ob_sum = Sum()
meth_add = ob_sum.add(4,5)
print("The value of sum is {}".format(meth_add))

class BasicCalculator:
    def __init__(self, a, b):                              # init function is used to initialise the parameters/arguments
        self.x = a
        self.y = b

    def sum(self):
        return self.x+self.y

    def diff(self):
        return self.x-self.y

    def prod(self):
        return self.x*self.y

    def div(self):
        return self.x/self.y

obj_calc = BasicCalculator(15,10)
meth_sum = obj_calc.sum()
print("The sum of two values is {}".format(meth_sum))
meth_diff = obj_calc.diff()
print("The difference between two values is {}".format(meth_diff))
meth_prod = obj_calc.prod()
print("The product of two values is {}".format(meth_prod))
meth_div = obj_calc.div()
print("The quotient of two values is {}".format(meth_div))



# inheritance

class EmployeeDetails():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def details(self):
        print("The first name of employee is {} and the last name of employee is {}".format(self.first_name, self.last_name))

class EmployeeOfficialDetails(EmployeeDetails):
    def __init__(self, salary, id_number, first_name, last_name):
        self.salary = salary
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name

    def employee_details(self):
        print("The employee name is {} {} and id number is {} and his salary is {}".format(self.first_name, self.last_name,
                                                                                            self.id_number, self.salary))

obj_child = EmployeeOfficialDetails(10000, 23, "Deekshitha", "Manjunath")
det_emp = obj_child.employee_details()



class Vehicle():
    def __init__(self, colour, fuel_type):
        self.colour = colour
        self.fuel_type = fuel_type

    def type_vehicle(self):
        print("the colour of the vehicle is {} and the fuel type of vehicle is {}".format(self.colour, self.fuel_type))

class CarDetails():
    def __init__(self, veh_num, own_name):
        self.veh_num = veh_num
        self.own_name = own_name

    def car_details(self):
        print("the vehicle no of car is {} and owner name of car is {}".format(self.veh_num, self.own_name))

class VehicleDetails(Vehicle, CarDetails):
    def __init__(self, colour, fuel_type, veh_num, own_name):
        self.colour = colour
        self.fuel_type = fuel_type
        self.veh_num = veh_num
        self.own_name = own_name

    def details(self):
        print("the vehicle no of car is {} and owner name of car is {} and the colour of the vehicle is {} and the fuel type of vehicle is {}".format(self.veh_num, self.own_name, self.colour, self.own_name))

obj_veh = VehicleDetails("Red", "Petrol", 20 , "ABC")
det_car = obj_veh.details()