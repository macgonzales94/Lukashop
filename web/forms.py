from django import forms

class DateInput(forms.DateInput,):
    input_type = "date"

class ClienteForm(forms.Form):
    SEXO_CHOICES = (
        ("M","Masculino"),
        ("F","Femenino")
    )


    dni = forms.CharField(label="DNI",max_length=8)
    nombres = forms.CharField(label="Nombres",max_length=200,required=True)
    apellidos = forms.CharField(label="Apellidos",max_length=200,required=True)
    email = forms.EmailField(label="Email",required=True)
    direccion = forms.CharField(label="Direccion",widget=forms.Textarea)
    telefono = forms.CharField(label="telefono",max_length=20)
    sexo = forms.ChoiceField(label="sexo",choices=SEXO_CHOICES)
    fecha_nacimiento = forms.DateField(label="Fecha Nacimiento",input_formats=["%Y-%m-%d"],widget=DateInput())
    
