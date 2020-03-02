from django.db import models


# Create your models here.
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)


class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fk_id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


class TipoUsuario(models.Model):
    id_tipoUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    fechaNacimiento = models.DateField()
    mail = models.EmailField()
    sexo = models.CharField(max_length=1)
    cedula = models.CharField(max_length=8)
    contrasena = models.CharField(max_length=25)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    imagen = models.ImageField
    fk_id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fk_id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fk_id_tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)


class Estadistica(models.Model):
    id_estadistica = models.AutoField(primary_key=True)
    fecha_muestra = models.DateField
    estatura = models.IntegerField
    peso = models.IntegerField
    imc = models.IntegerField
    tcalzado = models.IntegerField
    fk_id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Velocidad(models.Model):
    id_velocidad = models.AutoField(primary_key=True)
    fecha_muestra = models.DateField
    fk_id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Alcance(models.Model):
    id_alcance = models.AutoField(primary_key=True)
    fecha_muestra = models.DateField
    fk_id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class capacidadDeSaltoVertical(models.Model):
    id_capacidadsaltovertical = models.AutoField(primary_key=True)
    fecha_muestra = models.DateField
    fk_id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
