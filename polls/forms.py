import django.forms as forms


class ChoiceForm(forms.ModelForm):
    label_choice = forms.CharField(label='Text of choice', max_length=1000)