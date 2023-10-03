from abc import ABC,abstractmethod
class acta(ABC):
    @abstractmethod
    def calificar(self) -> None :
        pass

    @abstractmethod
    def nombrar(self) -> None:
        pass


