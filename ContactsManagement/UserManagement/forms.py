from django import forms
from UserManagement.models import User

class UserLoginForm(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label.title()
            self.fields[field].widget.attrs['autocomplete'] = "new-password"
    
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {'password': forms.PasswordInput}
        

class UserRegisterForm(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label.title()
            self.fields[field].widget.attrs['autocomplete'] = "new-password"
    
    class Meta:
        model = User
        fields = ('email', 'password', 'secret_code')
        widgets = {'password': forms.PasswordInput}        
