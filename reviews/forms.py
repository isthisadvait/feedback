from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label = "Your Name" , max_length=100)