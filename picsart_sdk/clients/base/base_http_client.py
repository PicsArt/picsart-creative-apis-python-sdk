from abc import ABC, abstractmethod


class BaseHttpClient(ABC):

    @abstractmethod
    def post(self, url, payload, files, headers): ...

    @abstractmethod
    def get(self, url, headers): ...
