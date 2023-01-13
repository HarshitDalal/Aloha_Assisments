from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def engine(self, e_name: str, cc: int, e_type: str) -> None:
        pass

    @abstractmethod
    def wheels(self, num: int) -> None:
        pass

    def breaks(self, b_type: str) -> None:
        pass


class Bike(Vehicle):

    def __init__(self, m_name: str) -> None:
        self.__name = m_name
        self.__wheel_no = 0
        self.__break_type = ''
        self.__engine_detail = []

    def engine(self, e_name: str, cc: int, e_type: str) -> None:
        self.__engine_detail.append([e_name, cc, e_type])

    def breaks(self, b_type: str) -> None:
        self.__break_type = b_type

    def wheels(self, num: int) -> None:
        self.__wheel_no = num

    def __repr__(self):
        return f'Bike(name={self.__name}, wheel_no={self.__wheel_no}, break_type={self.__break_type}, engine_detail={self.__engine_detail})'


class Bajaj(Bike):
    __models = {}

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def add_model(self, name: str, detail: object) -> str:
        self.__models[name] = detail
        return f'Model add successfully'

    def remove_model(self, name: str) -> str:
        data = self.__models.pop(name)
        return f'Model {data} remove successfully'

    def update_model(self, name: str, detail: object) -> str:
        self.__models[name] = detail
        return f'Model {name} update successfully'

    def show_all(self) -> dict[Bike]:
        return self.__models

    def __del__(self):
        pass


# def create_bike(name: str, obj: object, wheel: int, b_type: str, e_name: str, cc: int, e_type: str) -> None:
#     obj.wheels(wheel)
#     obj.breaks(b_type)
#     obj.engine(e_name, cc, e_type)
#     obj.add_model(name, obj)
#     print(obj.show_all())


if __name__ == '__main__':
    name, wheel, b_type, e_name, cc, e_type = input().split()
    obj = Bajaj(name)
    obj.wheels(wheel)
    obj.breaks(b_type)
    obj.engine(e_name, cc, e_type)
    obj.add_model(name, obj)
    print(obj.show_all())


    # create_bike(name, obj, int(wheel), b_type, e_name, int(cc), e_type)
