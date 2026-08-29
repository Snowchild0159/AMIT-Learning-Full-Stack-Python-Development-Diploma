from django import forms
from .models import Department




class DepartmentForm(forms.ModelForm) : 
    
    name = forms.CharField(required=True , min_length=3 , max_length=100 , widget=forms.widgets.TextInput(attrs={"class" : "form-control" }))
    city = forms.CharField(required=True , min_length=3 , max_length=100 , widget=forms.widgets.TextInput(attrs={"class" : "form-control" }))
    streat = forms.CharField(required=True , min_length=3 , max_length=100 , widget=forms.widgets.TextInput(attrs={"class" : "form-control" }))
    state = forms.CharField(required=True , min_length=3 , max_length=100 , widget=forms.widgets.TextInput(attrs={"class" : "form-control" }))
    
    def clean_name(self):
        value = self.cleaned_data.get("name") 
        
        if value == "ahmed" : 
            raise forms.ValidationError("Name can't be ahmed ")
        else : 
            return value
    class Meta : 
        model = Department
        # fields = "__all__"
        fields = ["name" , "city" , "streat" , "state"]