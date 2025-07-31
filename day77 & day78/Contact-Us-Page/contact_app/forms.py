from django import forms
from .models import Contact

# ✅ Manual form
class ManualContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name must not contain numbers")
        return name

# ✅ ModelForm
class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name must not contain numbers")
        return name
