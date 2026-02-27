from django import forms
from .models import TaskModel
from category.models import TaskCategory

class TaskModelForm(forms.ModelForm):
    taskCategory = forms.ModelMultipleChoiceField(
        queryset=TaskCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    # class Meta:
    #     model = TaskModel
    #     fields = ['taskTitle', 'taskDescription', 'is_completed', 'taskAssignDate']
    #     widgets = {
    #         'taskAssignDate': forms.DateInput(attrs={'type': 'date'}),
    #     }
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription', 'is_completed', 'taskAssignDate']
        widgets = {
            'taskTitle': forms.TextInput(attrs={'class': 'form-control'}),
            'taskDescription': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'taskAssignDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
