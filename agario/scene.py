from abc import ABC, abstractmethod


class Scene(ABC):
    @abstractmethod
    def update(self, events) -> None:
        pass

    @abstractmethod
    def draw(self, screen) -> None:
        pass
