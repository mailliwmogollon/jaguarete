from django.db import models


# Create your models here.

class Categoria(models.Model):
    tipo = models.CharField(max_length=64, null=False)

    def __str__(self):
        return f"{self.tipo}"

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="clasificacion_categoria")
    titulo = models.CharField(max_length=250, null=False)
    descripcion = models.CharField(max_length=250, null=False)
    precio = models.CharField(max_length=2000, null=False)
    imagen = models.FileField(upload_to='imagenes/')

    def __str__(self):
        return f"Producto #{self.id}: {self.titulo} - {self.descripcion} - {self.categoria}"

class Carro(models.Model):
    
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        
        self.carro=carro

    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "titulo":producto.titulo,
                "precio":producto.precio,
                "cantidad":1
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()




   