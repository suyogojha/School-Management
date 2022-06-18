from django import forms
from .models import StudentInfo

class CreateStudent(forms.ModelForm):
    class Meta:
        model = StudentInfo
        exclude = ("student_img", "fathers_img", "mothers_img", )

        widgets = {
            'academic_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Academic Year'}),
            'admission_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Admission Date'}),
            'admission_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admission ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'class_type': forms.Select(attrs={'class': 'form-control'}),
            'section_type': forms.Select(attrs={'class': 'form-control'}),
            'shift_type': forms.Select(attrs={'class': 'form-control'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fathers Name'}),
            'fathers_nid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fathers ID'}),
            'fathers_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fathers Number'}),
            'mothers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mothers Name'}),
            'mothers_nid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mothers ID'}),
            'mothers_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mothers Number'}),
        }

