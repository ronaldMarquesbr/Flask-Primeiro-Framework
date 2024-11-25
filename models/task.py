class Task:
    def __init__(self, id, title, description, completed=False) -> None:
        self.__id = id
        self.__title = title
        self.__description = description
        self.__completed = completed

    def to_dict(self):
        return {
            "id": self.__id,
            "title": self.__title,
            "description": self.__description,
            "completed": self.__completed
        }

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_completed(self):
        return self.__completed

    def set_title(self, title):
        self.__title = title

    def set_description(self, description):
        self.__description = description

    def set_completed(self, completed):
        self.__completed = completed
