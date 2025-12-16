from django import forms

class EmployeeForm(forms.Form):
    emp_id = forms.IntegerField(
        label="Employee ID",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Employee ID'
            }
        )
    )

    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name'
            }
        )
    )

    department = forms.CharField(
        label="Department",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Department'
            }
        )
    )

    salary = forms.IntegerField(
        label="Salary",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Salary'
            }
        )
    )

    def clean_salary(self):
        sal = self.cleaned_data['salary']
        if sal < 10000:
            raise forms.ValidationError("Salary must be greater than 10000")
        return sal


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Username'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password'
            }
        )
    )
