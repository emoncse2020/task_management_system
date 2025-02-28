from django import forms
from tasks.models import Task, TaskDetail

#Django form
# class TaskForm(forms.Form):
#     title = forms.CharField(max_length=200, label="Task Title")
#     description = forms.CharField(widget=forms.Textarea,label="Task Description")
#     due_date = forms.DateField(widget=forms.SelectDateWidget, label="Due Date")
#     assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label="Assigned To", choices=[])


#     def __init__(self, *args, **kwargs):
#         # print(args,kwargs)
#         employees = kwargs.pop("employees",[])
#         super().__init__(*args, **kwargs)
#         # print(self.fields)
#         self.fields['assigned_to'].choices = [(emp.id, emp.name) for emp in employees]


class StyledFormMixin:
    """Mixing to apply style to form field"""


    default_classes = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder':f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                # print("inside  date")
                field.widget.attrs.update({
                    'class':"border-2 border-gray-300 p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                # print("inside checkbox")
                field.widget.attrs.update({
                    'class':"space-y-2"
                })
            else:
                # print("inside else")
                field.widget.attrs.update({
                    'class': self.default_classes
                })


#Django Model Form

class TaskModelForm(StyledFormMixin,forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to']
        widgets = {
            'due_date': forms.SelectDateWidget,
            'assigned_to': forms.CheckboxSelectMultiple
        }
        

        """Manual Widget """
        # widgets = {
        #     'title':forms.TextInput(attrs={
        #         'class': "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500",
        #         'placeholder':"Enter a descriptive task title"
        #     }),
        #     'description':forms.Textarea(attrs={
        #         'class': "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500",
        #         'placeholder':"Provide detailed task information",
        #         'rows':5,

        #     }),
        #     'due_date': forms.SelectDateWidget(attrs={
        #         'class': "border-2 border-gray-300 p-2  rounded-lg shadow-sm focus:border-rose-500 focus:ring-rose-500",
                
        #     }),
        #     'assigned_to': forms.CheckboxSelectMultiple(attrs={
        #         'class':"space-y-2" #adding space between checkbox for better readability
        #     })
        # }
    """Using mixing widget"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

class TaskDetailModelForm(StyledFormMixin,forms.ModelForm):
    
    class Meta:
        model = TaskDetail
        fields = ['priority', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
