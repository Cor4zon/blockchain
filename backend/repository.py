import abc


class AbstractRepository(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def create(cls, item):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def read(cls, pk):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def read_filtered(cls, filter_dict):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def read_all(cls):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def delete(cls, pk):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def update(cls, pk, data):
        raise NotImplementedError


class VotingRepository(AbstractRepository):
    @classmethod
    def create(cls, item):
        pass

    @classmethod
    def read(cls):
        pass

    @classmethod
    def read_filtered(cls, filter_dict):
        pass

    @classmethod
    def delete(cls, pk):
        pass

    @classmethod
    def update(cls, pk, data):
        pass


class CustomService():
    def __init__(self, repository):
        self.repository = repository

    def create(self, model):
        self.repository.create(model)

    def read(self, pk):
        return self.repository.read(pk)

    def read_filtered(self, project_pk):
        return self.repository.read_filtered(project_pk)

    def read_all(self):
        return self.repository.read_all()

    def delete(self, pk):
        return self.repository.delete(pk)

    def update(self, pk, data):
        return self.repository.update(pk, data)


VotingService = CustomService(VotingRepository)