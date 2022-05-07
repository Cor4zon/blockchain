from django.db import models


class Voting(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.title)


class VotingOption(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    voting = models.ForeignKey(Voting, on_delete = models.CASCADE, default=None)
    pubkey = models.TextField(unique=True)
    privkey = models.TextField()

    def __str__(self):
        return str(self.title)


class Voter(models.Model):
    pubkey = models.TextField(unique=True)
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE, default=1, null=True, blank=True)
    voteFor = models.ForeignKey(VotingOption, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.pubkey)
