from django import forms 

class FormularioCurso(forms.Form):
    nombre = forms.CharField(label="Curso", max_length=50)
    inscriptos = forms.IntegerField(label="Inscriptos")
    profesor = forms.CharField(max_length=50)
    solo_empresas = forms.BooleanField(label="Es para empresas", required=False)
    TURNOS = (
        ("M", "Mañana"),
        ("T", "Tarde"),
        ("N", "Noche")
    )
    turno = forms.ChoiceField(choices=TURNOS, required=True)
    fecha_inicio = forms.DateField(input_formats=["%d/%m/%Y"], label="Fecha de inicio")
    fecha_fin = forms.DateField(input_formats=["%d/%m/%Y"], label="Fecha de Fin")
    email = forms.EmailField(label="Correo Electronico", required=False)