from django.views.generic import ListView, DetailView, View
from .models import Team
from accounts.models import User
from matching.models import Match

class TeamListView(ListView):
    model = Team

    def get_queryset(self):
        query = f"SELECT team.*, match.status AS status FROM {Team._meta.db_table} team LEFT JOIN {Match._meta.db_table} match ON match.team_id = team.id WHERE match.user_id = {self.request.user.id} OR match.user_id IS NULL"
        return Team.objects.raw(query)

class TeamDetailView(DetailView):
    model = Team

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        all_matches = Match.objects.filter(team__id = context['object'].id).select_related('user')
        context['users'] = { status.fullname : [] for status in Match.Status.ALL }
        for matching in all_matches:
            context['users'][ Match.Status.EXPAND[matching.status].fullname ].append( matching.user )
        return context
