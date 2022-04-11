from django import forms

from main.models import Worker, Project, Membership


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = "__all__"
        widgets = {
            'work_experience': forms.widgets.DateInput(attrs={'type': 'date'}),
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        
        
class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = "__all__"
        widgets = {
            'date_joined': forms.widgets.DateInput(attrs={'type': 'date'})
        }