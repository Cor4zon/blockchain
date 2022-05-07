from django.contrib import admin

from backend.models import Voting, VotingOption, Voter


@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    pass


@admin.register(VotingOption)
class VotingOptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    pass
