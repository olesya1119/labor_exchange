class BaseModel:

    def __init__(self, id: int | str | None) -> None:
        if isinstance(id, str):
            if not id:
                self.id = None
            else:
                self.id = int(id)
        else:
            self.id = id

    def to_dict(self) -> dict:
        '''Метод возвращает словарь всех значений КРОМЕ id'''
        return {key: value for key, value in self.__dict__.items()
                if key != "id"}
