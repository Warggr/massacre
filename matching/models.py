from django.db import models
from teams.models import Team
from accounts.models import User

class Match(models.Model):
    class Status: # actually a namespace
        class Status:
            def __init__(self, code, fullname, description):
                self.code = code; self.fullname = fullname; self.description = description
        ADMIN = Status('A', 'admin', 'Admin')
        MEMBER = Status('M', 'member', 'Member')
        INTERESTED = Status('I', 'interested', 'Requested to join')
        OFFERED = Status('O', 'offered', 'Received offer to join')

        ALL = [ ADMIN, MEMBER, INTERESTED, OFFERED ]
        EXPAND = { status.code : status for status in ALL }
    status = models.CharField(max_length=1, choices=[(status.code, status.description) for status in Status.ALL ])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'team'], name='unique_user_x_team'
            )
        ]
