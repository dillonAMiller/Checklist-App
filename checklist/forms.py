from django.db import models
from django import forms
from django.forms import ModelForm
from .models import item

item_is_displayed_choices = (
        ('0', 'No'),
        ('1', 'Yes'),
)

class displayedForm(ModelForm):
    class Meta:
        model = item
        fields = ['itemDisplayed']