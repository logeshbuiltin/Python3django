from django import forms


class AccountLoginForm(forms.Form):

    email = forms.EmailField(label='', max_length=254, required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control', 'id': 'txtEmail', 'autocomplete': True, 'autofocus': True, 'required': True,
            'placeholder': 'Email Address'
        }))
    password = forms.CharField(label='', max_length=45, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 'id': 'txtPassword', 'autocomplete': False, 'required': True,
            'placeholder': 'Password'
        }))

    def clean(self):
        return self.cleaned_data


class SetPasswordForm(forms.Form):
    email = forms.EmailField(label='', max_length=254, required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control', 'id': 'txtEmail', 'autocomplete': True, 'autofocus': True, 'required': True,
            'placeholder': 'Email Address'
        }))
    password = forms.CharField(label='', max_length=45, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 'id': 'txtPassword', 'autocomplete': False, 'required': True,
            'placeholder': 'Password'
        }))
    confirm_password = forms.CharField(label='', max_length=45, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 'id': 'txtPasswordConfirm', 'autocomplete': False, 'required': True,
            'placeholder': 'Password'
        }))

    def clean(self):
        return self.cleaned_data


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='', max_length=254, required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control', 'id': 'txtEmail', 'autocomplete': True, 'autofocus': True, 'required': True,
            'placeholder': 'Email Address'
        }))

    def clean(self):
        return self.cleaned_data