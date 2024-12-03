import json
import os.path
import uuid


class BibliotequeController:

    __biblioteque_adress = "biblioteque.json"

    def open_biblioteque(self):
        with open(
            self._BibliotequeController__biblioteque_adress, "r"
        ) as biblioteque_opened_for_reading:
            biblioteque_data = json.load(biblioteque_opened_for_reading)
        return biblioteque_data

    def add_to_biblioteque(self, data):
        with open(
            self._BibliotequeController__biblioteque_adress, "w"
        ) as biblioteque_opened_for_writing:
            json.dump(data, biblioteque_opened_for_writing)

    def main_menu(self):
        return input(
            "Добро пожаловать в нашу электронной библиотеке! Ниже представлены доступные команды, для продолжения - введите соответствующую цифру: \n \
            1 - Добавить книгу \n \
            2 - Удалить книгу \n \
            3 - Найти книгу \n \
            4 - Отобразить все книги \n \
            5 - Изменить статус книги по id \n \
            6 - Выйти \n"
        )

    def search_menu(self):
        return input(
            "Выберите параметр поиска: \n \
            1 - Искать по названию \n \
            2 - Искать по автору \n \
            3 - Искать по году издания \n"
        )

    def show_search_results(self, results):
        for result in results:
            print(
                f"id: {result} \n \
                    Название: {results[result]["title"]} \n \
                    Автор: {results[result]["author"]}  \n \
                    Год издания: {results[result]["year"]}  \n \
                    Статус: {results[result]["status"]} \n"
            )

    def search_by_title(self, title):
        books = self.open_biblioteque()
        results = {}
        for book in books:
            if title == books[book]["title"]:
                results[book] = books[book]
        if len(results) != 0:
            self.show_search_results(results)
        else:
            return "Такой книги на данный момент нет."

    def search_by_author(self, author):
        books = self.open_biblioteque()
        results = {}
        for book in books:
            if author == books[book]["author"]:
                results[book] = books[book]
        if len(results) != 0:
            self.show_search_results(results)
        else:
            return "Такого автора на данный момент нет."

    def search_by_year(self, year):
        books = self.open_biblioteque()
        results = {}
        for book in books:
            if year == books[book]["year"]:
                results[book] = books[book]
        if len(results) != 0:
            self.show_search_results(results)
        else:
            return "Такого года на данный момент нет."

    def input_main_book_info(self):
        title = input("Введите название книги: \n")
        author = input("Введите автора книги: \n")
        year = input("Введите год издания книги: \n")
        status = "в наличии"
        return title, author, year, status

    def get_the_book_information(self):
        # title, author, year, status = self.input_main_book_info()
        title = input("Введите название книги: \n")
        author = input("Введите автора книги: \n")
        year = input("Введите год издания книги: \n")
        status = "в наличии"
        id = uuid.uuid4()
        data = {
            "title": title,
            "author": author,
            "year": year,
            "status": status,
        }
        return id, data

    def list_books(self):
        if os.path.exists(self._BibliotequeController__biblioteque_adress):
            biblioteque_data = self.open_biblioteque()
            for id in biblioteque_data.keys():
                print(f"id: {id}")
                print(f"Название: {biblioteque_data[id]["title"]}")
                print(f"Автор: {biblioteque_data[id]["author"]}")
                print(f"Год издания: {biblioteque_data[id]["year"]}")
                print(f"Статус: {biblioteque_data[id]["status"]} \n")

        else:
            print("К сожалению библиотека еще не создана.")

    def delete_the_book(self):
        print(
            "Книги удаляются по ID. Если вы не помните ID, рекомендуем вывести весь список книг."
        )
        question = input(
            "Вы действительно хотите удалить книгу? Если да, нажмите 1, если нет - любую кнопку. \n"
        )
        if int(question) == 1:
            biblioteque_data = self.open_biblioteque()
            book_id = input("Введите ID книги: \n")
            if book_id in tuple(biblioteque_data.keys()):
                biblioteque_data.pop(book_id)
                self.add_to_biblioteque(biblioteque_data)

    def change_status(self):
        print(
            "Статус у книги изменяется по ID. Если вы не помните ID, рекомендуем вывести весь список книг."
        )
        question = input(
            "Вы действительно хотите изменить статус у книги? Если да, нажмите 1, если нет - любую кнопку. \n"
        )
        if int(question) == 1:
            biblioteque_data = self.open_biblioteque()
            book_id = input("Введите ID книги: \n")
            if book_id in tuple(biblioteque_data.keys()):
                print(f"Статус: {biblioteque_data[book_id]["status"]} \n")
                status = input(
                    "Доступно два статуса. Введите соответствующую цифру: \n \
                    1 = в наличии \n \
                    2 = выдана \n"
                )
                if int(status) == 1:
                    biblioteque_data[book_id]["status"] = "в наличии"
                if int(status) == 2:
                    biblioteque_data[book_id]["status"] = "выдана"

                self.add_to_biblioteque(biblioteque_data)


if __name__ == "__main__":
    while True:
        action = BibliotequeController()
        main_request = action.main_menu()

        if int(main_request) == 1:
            id, data = action.get_the_book_information()
            if not os.path.exists("biblioteque.json"):
                data_for_dumping = {str(id): data}
                action.add_to_biblioteque(data_for_dumping)
            else:
                biblioteque_data = action.open_biblioteque()
                biblioteque_data[str(id)] = data
                action.add_to_biblioteque(biblioteque_data)

        if int(main_request) == 2:
            action.delete_the_book()

        if int(main_request) == 3:
            search_request = action.search_menu()
            if int(search_request) == 1:
                searching_title = input("Напишите название книги: \n")
                action.search_by_title(searching_title)

            if int(search_request) == 2:
                searching_author = input("Напишите автора книги: \n")
                action.search_by_author(searching_author)

            if int(search_request) == 3:
                searching_year = input("Напишите автора книги: \n")
                action.search_by_year(searching_year)

        if int(main_request) == 4:
            action.list_books()

        if int(main_request) == 5:
            action.change_status()

        if int(main_request) == 6:
            print("Спасибо за ваш визит! Ждем вас еще!")
            break
