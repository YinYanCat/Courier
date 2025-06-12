from django.contrib.auth.hashers import make_password
from ..models import Usuario, Repartidor
from app.utils.Rut import checkRut, processRut

class CarrierFactory:
	def crear_usuario(self, rut, nombre, apellido, nombre_usuario, contraseña, correo, telefono):
		rut = processRut(rut)
		if checkRut(rut):
			usuario = Usuario(
				rut=rut,
				first_name=nombre,
				last_name=apellido,
				username=nombre_usuario,
				email=correo,
				telefono=telefono,
				is_superuser=False,
				is_staff=False
			)
			usuario.set_password(contraseña)
			usuario.save()
			repartidor = Repartidor(usuario=usuario)
			repartidor.save()
			return repartidor
		else:
			raise ValueError("RUT inválido")