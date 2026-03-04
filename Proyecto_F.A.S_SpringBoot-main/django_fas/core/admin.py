from django.contrib import admin

from .models import (
    Cancha,
    Categoria,
    Entrenamiento,
    Escuela,
    InscripcionTorneo,
    Jugador,
    Lider,
    Torneo,
    Ubicacion,
    User,
)

admin.site.register(User)
admin.site.register(Ubicacion)
admin.site.register(Escuela)
admin.site.register(Lider)
admin.site.register(Categoria)
admin.site.register(Jugador)
admin.site.register(Cancha)
admin.site.register(Entrenamiento)
admin.site.register(Torneo)
admin.site.register(InscripcionTorneo)
