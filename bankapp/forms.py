from django import forms


class adduserform(forms.Form):
    fristname = forms.CharField(max_length=12, widget=forms.TextInput(attrs={"class":"form-control"}))
    lastname = forms.CharField(max_length=12, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(max_length=64, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(max_length=12, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    confrim_password = forms.CharField(max_length=12, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    username = forms.CharField(max_length=12, widget=forms.TextInput(attrs={"class":"form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("confirmpassword")
        if password1 != password2:
           msg="password mismatch"
           self.add_error("password",msg)


class loginform(forms.Form):
    username = forms.CharField(max_length=12, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=12, widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean(self):
        pass


class createaccountform(forms.Form):
    username = forms.CharField(max_length=12, widget=forms.TextInput(attrs={"class": "form-control"}))
    accountnum = forms.CharField(max_length=12, widget=forms.TextInput(attrs={"class": "form-control"}))
    acctype = forms.CharField(max_length=12, widget=forms.TextInput(attrs={"class": "form-control"}))
    min_bal = forms.CharField(max_length=12, widget=forms.TextInput(attrs={"class": "form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        min_bal = int(cleaned_data.get("min_bal"))
        acctype = cleaned_data.get("acctype")
        if min_bal < 2000:
            msg = "invalid bal plz provide value>2000"
            self.add_error("min_bal", msg)
        if acctype != "savings":
            msg = "u r not able to create acc"
            self.add_error("acctype", msg)
