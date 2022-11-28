from django import forms
from .models import Dogwalking, Review


class DogwalkingForm(forms.ModelForm):
    class Meta:
        model = Dogwalking
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
