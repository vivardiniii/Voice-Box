from django import forms
#from django.apps import hashtag, post
from .models import Post
from .models import Hashtag
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #model = apps.get_model('hashtag', 'Hashtag')
        fields = ('user','title', 'text', 'date', 'image','hname')

class HashtagForm(forms.ModelForm):

    class Meta:
        model = Hashtag
        fields = ('hashname',)

class EditPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'date', 'image','hname')

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text='Enter your last name',
                                widget=forms.TextInput(attrs={'placeholder': 'Username'}), required=False)
    email = forms.EmailField(help_text='Enter your email id',
                             widget=forms.EmailInput(attrs={'placeholder': 'Mail id'}), required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
