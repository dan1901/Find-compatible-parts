from django import forms
from .models import Part

class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = [
            'category', 'car_model', 'original_part_name',
            'original_part_number', 'compatible_part_name',
            'compatible_part_number', 'description', 'additional_info'
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'browser-default'}),
            'car_model': forms.Select(attrs={'class': 'browser-default'}),
            'original_part_name': forms.TextInput(attrs={'class': 'validate'}),
            'original_part_number': forms.TextInput(attrs={'class': 'validate'}),
            'compatible_part_name': forms.TextInput(attrs={'class': 'validate'}),
            'compatible_part_number': forms.TextInput(attrs={'class': 'validate'}),
            'description': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'additional_info': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }