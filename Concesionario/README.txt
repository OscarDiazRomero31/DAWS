Mi proyecto tratara del sistema de gestion que tiene un concesionario 

Modelo: Coche
Este modelo representa un coche en mi sistema de inventario. Cada coche tiene varias propiedades que describen sus características.
marca: (CharField) Este atributo almacena la marca del coche, como "Toyota" o "Ford". Es un campo de texto con una longitud máxima de 50 caracteres.
modelo: (CharField) Aquí guardo el modelo del coche, como "Corolla" o "Mustang". También es un campo de texto limitado a 50 caracteres.
año: (IntegerField) Representa el año de fabricación del coche. Es un campo numérico entero.
precio: (DecimalField) Este campo guarda el precio del coche, con hasta 10 dígitos en total y 2 decimales. Esto permite manejar grandes cantidades con precisión.
disponible: (BooleanField) Indica si el coche está disponible para la venta o no. Por defecto, está marcado como disponible (True).
matricula: (CharField, unique=True) Aquí guardo el número de matrícula o placa del coche, limitado a 10 caracteres y debe ser único.

Modelo: Cliente
Este modelo describe a los clientes que compran o están interesados en los coches.
nombre: (CharField) Almaceno el nombre del cliente, con un máximo de 100 caracteres.
apellido: (CharField) Aquí guardo el apellido del cliente, también con un límite de 100 caracteres.
email: (EmailField) El correo electrónico del cliente. Este campo valida que la entrada sea un formato de correo electrónico correcto.
telefono: (CharField) Almaceno el número de teléfono del cliente en formato de texto, con un máximo de 15 caracteres.
fecha_registro: (DateTimeField, auto_now_add=True) Este campo registra automáticamente la fecha y hora cuando el cliente fue añadido al sistema.

Modelo: Personal
Este modelo representa al personal de la empresa, como los vendedores.
nombre: (CharField) Aquí guardo el nombre del empleado, con un máximo de 100 caracteres.
apellido: (CharField) El apellido del empleado, también limitado a 100 caracteres.
email: (EmailField) El correo electrónico del empleado. Este campo se asegura de que el formato sea válido.
cargo: (CharField) Almaceno el cargo o puesto del empleado, como "Vendedor", con un límite de 50 caracteres.
fecha_nacimiento: (DateField, null=True, blank=True) La fecha de nacimiento del empleado. Es opcional, por lo que puede estar vacío (null=True y blank=True).

Modelo: Venta
Este modelo describe una venta de un coche a un cliente.
coche: (ForeignKey a Coche) Relaciona la venta con un coche específico. La relación es de muchos a uno (ManyToOne), porque un coche puede estar en muchas ventas, pero cada venta tiene un solo coche.
cliente: (ForeignKey a Cliente) Relaciona la venta con un cliente. También es una relación de muchos a uno, ya que un cliente puede hacer varias compras.
vendedor: (ForeignKey a Personal) El vendedor que realizó la venta. Es otra relación de muchos a uno, ya que un vendedor puede gestionar muchas ventas.
fecha: (DateField) Fecha en la que se realizó la venta.
num_factura: (CharField, null=True, blank=True) Número de factura relacionado con la venta. Puede estar vacío si no se ha generado aún.

Modelo: Mantenimiento
Este modelo representa el mantenimiento asociado a un coche.
coche: (OneToOneField a Coche) Cada coche tiene un único mantenimiento asociado. La relación es uno a uno.
fecha_mantenimiento: (DateField) La fecha en que se realizó el mantenimiento.
descripcion: (TextField) Aquí guardo una descripción detallada del mantenimiento realizado.
coste: (DecimalField) El coste del mantenimiento, con hasta 7 dígitos y 2 decimales para precisión.

Modelo: DireccionCliente
Este modelo almacena la dirección del cliente.
cliente: (OneToOneField a Cliente) Cada cliente tiene una dirección única asociada. Es una relación uno a uno.
calle: (CharField) La dirección del cliente, con un máximo de 100 caracteres.
ciudad: (CharField) La ciudad donde reside el cliente, con un máximo de 50 caracteres.
codigo_postal: (CharField) El código postal del cliente, con un máximo de 10 caracteres.
pais: (CharField) El país donde reside el cliente, con un máximo de 50 caracteres.
latitud: (FloatField, null=True, blank=True) Coordenada de latitud de la dirección, que es opcional.
longitud: (FloatField, null=True, blank=True) Coordenada de longitud de la dirección, también opcional.

Modelo: SeguroCoche
Este modelo describe el seguro de un coche.
coche: (OneToOneField a Coche) Cada coche tiene un seguro único asociado. Es una relación uno a uno.
numero_poliza: (CharField) El número de la póliza de seguro, con un máximo de 50 caracteres.
fecha_vencimiento: (DateField) La fecha en que expira la póliza de seguro.
cobertura: (CharField) La cobertura del seguro, que describe qué protege la póliza, con un máximo de 100 caracteres.

Modelo: CategoriaCoche
Este modelo representa diferentes categorías de coches, como "SUV" o "Deportivo".
nombre: (CharField) El nombre de la categoría, con un límite de 50 caracteres.
descripcion: (TextField) Una descripción detallada de la categoría.
coches: (ManyToManyField a Coche, related_name="categorias") Relación muchos a muchos. Un coche puede pertenecer a varias categorías y una categoría puede contener muchos coches.

Modelo: ContratoProveedor
Este modelo representa un contrato entre un proveedor y un coche, con atributos adicionales.
proveedor: (ForeignKey a Proveedor) El proveedor que firma el contrato. Relación muchos a uno, ya que un proveedor puede tener contratos con varios coches.
coche: (ForeignKey a Coche) El coche relacionado con el contrato. Relación muchos a uno, porque un coche puede estar asociado con varios proveedores.
fecha_contrato: (DateField) La fecha en la que se firmó el contrato.

Modelo: TestDrive
Este modelo representa un test drive de un coche realizado por un cliente.
cliente: (ForeignKey a Cliente) El cliente que realizó el test drive. Relación muchos a uno, ya que un cliente puede realizar varios test drives.
coche: (ForeignKey a Coche) El coche que el cliente probó. Relación muchos a uno, porque un coche puede ser probado varias veces.
fecha: (DateField) La fecha en que se realizó el test drive.
duracion: (IntegerField) La duración del test drive en minutos.

Modelo: Proveedor
Este modelo describe los proveedores de coches o piezas para la empresa.
nombre_empresa: (CharField) El nombre de la empresa proveedora, con un máximo de 100 caracteres.
contacto: (CharField) El nombre de la persona de contacto en la empresa, con un máximo de 100 caracteres.
email: (EmailField) El correo electrónico del proveedor.
telefono: (CharField) El número de teléfono del proveedor, con un máximo de 15 caracteres.
rating: (FloatField, null=True, blank=True) La calificación del proveedor, opcional.

Modelo: Habilidad
Este modelo representa una habilidad que un empleado puede tener.
nombre: (CharField) El nombre de la habilidad, como "Ventas" o "Mecánica", con un máximo de 100 caracteres.
