from django import forms
from User.models import User1,Post

class RegForm(forms.ModelForm):  
    class Meta:
        model = User1
        fields = ("first_name","last_name","username",'email','password')
        labels = {
            "first_name" : 'First Name',
            "last_name"     :  "Last Name",
            "username"  :  "Username",
            'email' :   'Email',
            'password'  :  "password"
        }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'})
        }
        

class PostForm(forms.ModelForm):  
    class Meta:
        model = Post
        fields = ( 'text',)
        labels = {
            "text" : 'Text',
    
        }
        widgets = {
            'text':forms.Textarea(attrs={'class':'form-control'}),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label='Passward',strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))



    
