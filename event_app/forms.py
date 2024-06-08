from django import forms

from event_app.models import Event


class EventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        for field in self.visible_fields():
            if isinstance(field.field.widget, forms.CheckboxInput):
                field.field.widget.attrs['class'] = 'form-check-input'
            else:
                field.field.widget.attrs['class'] = 'form-control w-25'

    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['user', ]

        widgets = {
            "datetime": forms.DateTimeInput(attrs={
                'type': 'datetime-local',  # Ensure it's a datetime-local input
                'class': 'my-custom-class',  # Custom CSS class
                'placeholder': 'Select date and time',  # Placeholder text
            }),
        }
