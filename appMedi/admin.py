from django.contrib import admin

from .models.user import User
from .models.account import Account
from .models.persona import Persona
from .models.paciente import Paciente
from .models.familiar import Familiar
from .models.personalMedico import Personalmedico
from .models.signosVitales import Signosvitales
from .models.diagnostico import Diagnostico
from .models.historiaClinica import Historiaclinica

# Register your models here.

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Persona)
admin.site.register(Paciente)
admin.site.register(Familiar)
admin.site.register(Personalmedico)
admin.site.register(Signosvitales)
admin.site.register(Diagnostico)
admin.site.register(Historiaclinica)