from django import forms
from .models import TeacherInfo

class CreateTeacher(forms.ModelForm):
    class Meta:
        model = TeacherInfo
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'teacher_img': forms.FileInput(attrs={'class': 'form-control'}),
            'passing_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Passing Year'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Joining Date'}),
            'admission_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admission ID'}),
            'dept_type': forms.Select(attrs={'class': 'form-control'}),
            'sub_type': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
        }