from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import *
# class ContactForm(forms.Form):
#     name = forms.CharField(label="Your name", max_length=100, widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'required': 'required',
#         }))
#     email = forms.EmailField(label="Your email", max_length=100, 
#                              widget=forms.EmailInput(attrs={
#             'class': 'form-control',
#             'required': 'required',
#         }))
#     phone = forms.CharField(label="Your phone", max_length=10, 
#                             widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'required': 'required',
#         }))
#     subject = forms.CharField(label="Subject", max_length=100, 
#                               widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'required': 'required',
#         }))
#     message = forms.CharField(label="Message", widget=forms.Textarea(attrs={
#             'class': 'form-control',
#             'required': 'required',
#         }))






#     def clean_phone(self):
#         phone = self.cleaned_data['phone']

#         if not phone.startswith('98') or phone.startswith('97'):
#             raise forms.ValidationError("Please enter a phone number that's valid for Nepal")


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
        # fields = '__all__'





# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'profile_pic']






class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['title', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }



