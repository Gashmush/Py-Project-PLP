from .models import Worker
from django import forms

class WorkerForm(forms.ModelForm):
    class Meta:
        model=Worker
        fields=['category','status','first_name','last_name','age','salary','contact','location','gender','photo']