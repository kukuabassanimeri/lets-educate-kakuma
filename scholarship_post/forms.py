from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ScholarshipPost, ContactUs

#Scholarship_blog user creation form
class ScholarshipUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password',
        })
#Scholarship_blog user login form
class ScholarshipUserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )
    
#scholarship_blog form post
class ScholarshipPostModelForm(forms.ModelForm):
    class Meta:
        model = ScholarshipPost
        fields = ['title', 'content', 'eligibility_criteria',
                'dead_line', 'link', 'created_at', 'created_by'
                ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'eligibility_criteria': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'dead_line': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'created_at': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
#scholarship_blog form contact us
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'phone_number', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }

