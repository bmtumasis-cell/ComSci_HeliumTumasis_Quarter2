# Tumasis, Bleuzette Albrielle Felenash M.
# 9 - Helium

#Main parent class which contains name, bill amount, and calculating bill amount with getter and setter
class Patient:
    def __init__(self, name: str, bill_amount: float):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill_amount(self):
        return self.__bill_amount

#Senior patients with 20% discount
class SeniorPatient(Patient):
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    def calculate_bill_amount(self):
        return self.get_bill_amount() * 0.80

#PhilHealth patients with 15% discount
class PhilHealthPatient(Patient):
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    def calculate_bill_amount(self):
        return self.get_bill_amount() * 0.85

#Main Output
if __name__ == '__main__':
    print("\nHospital Billing System\n-----------------------")

    #For regular patients
    regular_patient = Patient("Juan Dela Cruz", 15000)
    print(f"Patient Name: {regular_patient.get_name()}")
    print(f"Original Bill: P{regular_patient.get_bill_amount():,.2f}")
    print(f"Final Bill: P{regular_patient.calculate_bill_amount():,.2f}\n")

    #For senior citizen patients with discount applied
    senior_patient = SeniorPatient("Maria Santos", 15000)
    print(f"Patient Name: {senior_patient.get_name()}")
    print(f"Original Bill: P{senior_patient.get_bill_amount():,.2f}")
    print(f"Final Bill: P{senior_patient.calculate_bill_amount():,.2f}\n")

    #For PhilHealth patients with discount applied
    philhealthpatient = PhilHealthPatient("Pedro Reyes", 15000)
    print(f"Patient Name: {philhealthpatient.get_name()}")
    print(f"Original Bill: P{philhealthpatient.get_bill_amount():,.2f}")
    print(f"Final Bill: P{philhealthpatient.calculate_bill_amount():,.2f}\n")
