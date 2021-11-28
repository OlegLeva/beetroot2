class Person:
    def __init__(self, firstname, lastname, phone):
        self.firstname = firstname
        self.lastname = lastname
        if not (type(phone) == str and phone.isdigit()) and type(phone) != int:
            raise TypeError(f'{phone} most be integer')
        self.phone = int(phone)

    def get_phone(self):
        return self.phone
