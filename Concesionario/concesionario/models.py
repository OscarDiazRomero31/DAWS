from django.db import models


class Coche(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Venta(models.Model):
    coche = models.ForeignKey(Coche, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    vendedor = models.ForeignKey('Personal', on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta de {self.coche} a {self.cliente} el {self.fecha}"


class Personal(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    cargo = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cargo})"


class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nombre_empresa


class ContratoProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    coche = models.ForeignKey(Coche, on_delete=models.CASCADE)
    fecha_contrato = models.DateField()

    def __str__(self):
        return f"Contrato de {self.proveedor} para {self.coche} el {self.fecha_contrato}"


class Mantenimiento(models.Model):
    coche = models.OneToOneField(Coche, on_delete=models.CASCADE)
    fecha_mantenimiento = models.DateField()
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"Mantenimiento de {self.coche} el {self.fecha_mantenimiento}"


class DireccionCliente(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    calle = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f"Dirección de {self.cliente}: {self.calle}, {self.ciudad}"


class TestDrive(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    coche = models.ForeignKey(Coche, on_delete=models.CASCADE)
    fecha = models.DateField()
    duracion = models.IntegerField(help_text="Duración en minutos")

    def __str__(self):
        return f"Test Drive de {self.cliente} con {self.coche} el {self.fecha}"


class CategoriaCoche(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    coches = models.ManyToManyField(Coche, related_name="categorias")

    def __str__(self):
        return self.nombre
