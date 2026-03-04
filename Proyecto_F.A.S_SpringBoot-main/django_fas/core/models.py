from django.contrib.auth.models import AbstractUser
from django.db import models


class Rol(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    LIDER = 'LIDER', 'Líder'
    JUGADOR = 'JUGADOR', 'Jugador'


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, max_length=50)
    num_documento = models.BigIntegerField(unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    rol_principal = models.CharField(max_length=10, choices=Rol.choices)


class Ubicacion(models.Model):
    localidad = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)

    class Meta:
        unique_together = ('localidad', 'barrio')

    def __str__(self) -> str:
        return f'{self.localidad} - {self.barrio}'


class Escuela(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, blank=True, null=True, unique=True)
    ubicaciones = models.ManyToManyField(Ubicacion, related_name='escuelas')

    def __str__(self) -> str:
        return self.nombre


class Lider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lider')
    escuela = models.ForeignKey(
        Escuela,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='lideres',
    )


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    rango_edad = models.CharField(max_length=30)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='categorias')

    def __str__(self) -> str:
        return f'{self.nombre} ({self.rango_edad})'


class Jugador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='jugador')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='jugadores')
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='jugadores')
    posicion = models.CharField(max_length=100, blank=True)
    numero_camiseta = models.IntegerField(blank=True, null=True)


class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_superficie = models.CharField(max_length=200)
    direccion = models.CharField(max_length=100)
    estado_disponible = models.BooleanField(default=True)
    horario_disponibilidad = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.PROTECT, related_name='canchas')


class Entrenamiento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    lugar = models.CharField(max_length=100)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='entrenamientos')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='entrenamientos')
    creador = models.ForeignKey(User, on_delete=models.PROTECT, related_name='entrenamientos_creados')
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.PROTECT, related_name='entrenamientos')


class EstadoTorneo(models.TextChoices):
    PROXIMO = 'PROXIMO', 'Próximo'
    EN_CURSO = 'EN_CURSO', 'En curso'
    FINALIZADO = 'FINALIZADO', 'Finalizado'
    CANCELADO = 'CANCELADO', 'Cancelado'


class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.CharField(max_length=500, blank=True)
    cupo_maximo = models.IntegerField()
    cupos_disponibles = models.IntegerField()
    estado = models.CharField(max_length=20, choices=EstadoTorneo.choices)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='torneos')
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.PROTECT, related_name='torneos')


class EstadoInscripcion(models.TextChoices):
    ACTIVA = 'ACTIVA', 'Activa'
    CANCELADA = 'CANCELADA', 'Cancelada'
    FINALIZADA = 'FINALIZADA', 'Finalizada'


class InscripcionTorneo(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='inscripciones')
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='inscripciones_torneo')
    lider = models.ForeignKey(Lider, on_delete=models.CASCADE, related_name='inscripciones_torneo')
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=EstadoInscripcion.choices)
