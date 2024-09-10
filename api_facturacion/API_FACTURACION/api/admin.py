from django.contrib import admin
from .models import Usuario
from .models import Producto
from .models import Licencia
from .models import Iva
from .models import Empresa
from .models import Cliente
from .models import Forma_pago
from .models import Detalle_empresa_iva
from .models import Detalle_empresa_producto
from .models import Detalle_empresa_cliente
from .models import Email

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Empresa)
admin.site.register(Licencia)
admin.site.register(Iva)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Forma_pago)
admin.site.register(Detalle_empresa_iva)
admin.site.register(Detalle_empresa_producto)
admin.site.register(Detalle_empresa_cliente)
admin.site.register(Email)
