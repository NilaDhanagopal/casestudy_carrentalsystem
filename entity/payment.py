class Payment:
    def __init__(self, paymentID=0, leaseID=0, paymentDate="", amount=0.0):
        self.__paymentID = paymentID
        self.__leaseID = leaseID
        self.__paymentDate = paymentDate
        self.__amount = amount

    # Getters
    def get_paymentID(self):
        return self.__paymentID

    def get_leaseID(self):
        return self.__leaseID

    def get_paymentDate(self):
        return self.__paymentDate

    def get_amount(self):
        return self.__amount

    # Setters
    def set_paymentID(self, paymentID):
        self.__paymentID = paymentID

    def set_leaseID(self, leaseID):
        self.__leaseID = leaseID

    def set_paymentDate(self, paymentDate):
        self.__paymentDate = paymentDate

    def set_amount(self, amount):
        self.__amount = amount
