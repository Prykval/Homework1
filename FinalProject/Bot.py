from abc import ABC, abstractmethod

class AbstractBot(ABC):
    def __init__(self, book: AddressBook):
        self.book = book

    @abc.abstractmethod
    def handle(self):
        pass

class AddBot(AbstractBot):
    def handle(self):
        record = self.create_record()
        self.book.add(record)

    def create_record(self):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value

        record = Record(name, phones, birth, email, status, note)
        return record

class SearchBot(AbstractBot):
    def handle(self) :
        print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")

        category = input('Search category: ')
        pattern = input('Search pattern: ')

        result = self.book.search(pattern, category)
        self.display_result(result)

    def display_result(self, result: list):
        for account in result:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
                result = f"_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
            print(result)

class EditBot(AbstractBot):
    def handle(self) :
        contact_name = input('Contact name: ')
        parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
        new_value = input("New Value: ")

        self.book.edit(contact_name, parameter, new_value)

class RemoveBot(AbstractBot):
    def handle(self):
        pattern = input("Remove (contact name or phone): ")
        self.book.remove(pattern)

class SaveBot(AbstractBot):
    def handle(self) :
        file_name = input("File name: ")
        self.book.save(file_name)

class LoadBot(AbstractBot):
    def handle(self):
        file_name = input("File name: ")
        self.book.load(file_name)

class CongratulateBot(AbstractBot):
    def handle(self):
        print(self.book.congratulate())

class ViewBot(AbstractBot):
    def handle(self) :
        print(self.book)

class ExitBot(AbstractBot):
    def handle(self):
        print("Bye!")
        exit()
