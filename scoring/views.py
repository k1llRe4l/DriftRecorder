from django.shortcuts import render
from .models import Score

def leaderboard(request):
    scores = Score.objects.select_related('driver').order_by('-total_score')
    return render(request, 'index.html', {'scores': scores})

