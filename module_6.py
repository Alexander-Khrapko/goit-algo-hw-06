from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if len(value) !=10 or not value.isdigit():
            raise ValueError("Phone number must be of 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        p = self.find_phone(phone)
        if p:
            self.phones.remove(p)
        # if not p:
        #     raise ValueError("Phone number not found")
        # self.phones.remove(p)


    def edit_phone(self, old_phone, new_phone):
        # варіант з add_phone, remove_phone, find_phone
        if self.find_phone(old_phone):
            # але в середені remove_phone також викликається find_phone
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            raise ValueError("Phone not found")

        # варіант з add_phone, find_phone
        # p = self.find_phone(old_phone)
        # if p:
        #     self.phones.remove(p)
        #     self.add_phone(new_phone)
        # else:
        #     raise ValueError("Phone not found")

        # перший варіант де новий номер залишиться там де був старий, а не в кінці
        # for i, p in enumerate(self.phones):
        #     if p.value == old_phone:
        #         self.phones[i] = Phone(new_phone)
        #         return True
        # raise ValueError("Phone number not found")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        # у критеріях нічого не написано про delete
        # return self.data.pop(name, None)  # None, если запись не найдена
        return self.data.pop(name)

    def __str__(self):
        if not self.data:
            return "No records found"
        return "\n".join(str(record) for record in self.data.values())

