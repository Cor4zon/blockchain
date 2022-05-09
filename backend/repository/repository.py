import abc

from backend.models import Voting, Voter, VotingOption


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
        voting = Voting(
            item["id"],
            item["title"],
            item["description"],
            item["deadline"]
        )
        voting.save()

    @classmethod
    def read(cls, pk):
        return Voting.objects.filter(pk=pk)[0]

    @classmethod
    def read_all(cls):
        return Voting.objects.all()

    @classmethod
    def read_filtered(cls, filter_dict):
        pass

    @classmethod
    def delete(cls, pk):
        Voting.objects.filter(pk=pk).delete()

    @classmethod
    def update(cls, pk, data):
        Voting.objects.filter(pk=pk).update(**data)


class VoterRepository:
    @classmethod
    def create(cls, item):
        voter = Voter(
            item["id"],
            item["pubkey"],
            item["voting_id"]
        )
        voter.save()

    @classmethod
    def read(cls, pk):
        return Voter.objects.filter(pk=pk)[0]

    @classmethod
    def read_all(cls):
        return Voter.objects.all()

    @classmethod
    def read_filtered(cls, filter_dict):
        pass

    @classmethod
    def delete(cls, pk):
        Voter.objects.filter(pk=pk).delete()

    @classmethod
    def update(cls, pk, data):
        Voter.objects.filter(pk=pk).update(**data)


class VotingOptionRepository:
    @classmethod
    def create(cls, item):
        voting_option = Voter(
            item["id"],
            item["title"],
            item["voting"],
            item["pubkey"],
            item["privkey"]
        )
        voting_option.save()

    @classmethod
    def read(cls, pk):
        return VotingOption.objects.filter(pk=pk)[0]

    @classmethod
    def read_all(cls):
        return VotingOption.objects.all()

    @classmethod
    def read_filtered(cls, filter_dict):
        pass

    @classmethod
    def delete(cls, pk):
        VotingOption.objects.filter(pk=pk).delete()

    @classmethod
    def update(cls, pk, data):
        VotingOption.objects.filter(pk=pk).update(**data)


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
VoterService = CustomService(VoterRepository)
VotingOptionService = CustomService(VotingOptionRepository)