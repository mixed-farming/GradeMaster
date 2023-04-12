from django import forms
from .models import Item, Document


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name','age','sex','memo', 'section', 'roll_no', 'science', 'maths', 'english', 'sst')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'Entry example: Manoj Mallya'}),
                    'age': forms.NumberInput(attrs={'min':1}),
                    'sex': forms.RadioSelect(),
                    'memo': forms.Textarea(attrs={'rows':4}),
                    'section': forms.TextInput(),
                    'roll_no': forms.NumberInput(attrs={'min':1}),
                    'science': forms.NumberInput(),
                    'english': forms.NumberInput(),
                    'sst': forms.NumberInput(),
                    'maths': forms.NumberInput()
                  }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name', 'description', 'file')
