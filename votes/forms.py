from django.forms import ModelForm
from .models import Candidate, Position

class NewCandidate(ModelForm):
    class Meta:
        model = Candidate
        exclude = ['id']

class NewPosition(ModelForm):
    class Meta:
        model = Position
        exclude = ['id']