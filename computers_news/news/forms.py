from .models import News
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'full_text', 'date']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter title...',
                'id': 'title'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Enter text...',
                'id': 'full_text'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter date and time...',
                'id': 'date'
            }),
        }
