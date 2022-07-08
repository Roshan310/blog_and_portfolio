from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget = forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )

    description = forms.CharField(widget = forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Write a comment"
        }
    ))