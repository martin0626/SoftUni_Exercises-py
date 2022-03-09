from django import forms

from TodoApp.Todo.models import Todo
from TodoApp.users.forms import BootsTrapMixin


class CreateTodoForm(BootsTrapMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({
            'rows': 3,
        })

    class Meta:
        model = Todo
        fields = ['title', 'description']
