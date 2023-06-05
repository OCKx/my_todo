from django import forms
from .models import Member, ListItem

class UserForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'pin']


class TodoList(forms.ModelForm):
    class Meta:
        model = ListItem
        fields = ['list', 'date']