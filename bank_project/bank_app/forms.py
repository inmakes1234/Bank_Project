from django import forms
from .models import Account_application

class DateInput(forms.DateInput):
    input_type = 'date'


class Account_applicationForm(forms.ModelForm):
    class Meta:
        model = Account_application
        fields = '__all__'

        widgets = {
            'dob': DateInput(),
        }
        labels = {
            'p_name': 'Name',
            'dob': 'Date of Birth',
            'age':'Age',
            'gender': 'Gender',
            'phn': 'Phone',
            'email': 'Email',
            'address': 'Address',
            'district': 'District',
            'branch':'Branch',
            'account_type':'Account Type',
        }

