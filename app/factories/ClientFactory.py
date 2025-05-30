from django.contrib.auth.hashers import make_password
from ..models import Usuario, Cliente
from datetime import date

class ClientFactory:

    def crear_usuario(self, rut, nombre, apellido, nombre_usuario, contraseña, correo, telefono):
        rut = self.processRut(rut)
        if self.checkRut(rut):
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
            cliente = Cliente(
                usuario=usuario
            )
            cliente.save()
            return cliente
        else:
            raise ValueError("RUT inválido")

    def processRut(self, rut):
        rut = rut.replace(".","").upper()
        return rut

    def checkRut(self, rut):
        try:
            id, dv = rut.split("-")
            id = list(map(int,reversed(id)))
            serial = [2,3,4,5,6,7]

            s = 0
            for i in range(len(id)):
                s += id[i]*serial[i%6]
            s = 11 - (s%11)
            if s == 11:
                s = "0"
            elif s == 10:
                s = "K"
            else:
                s = str(s)

            return dv == s

        except Exception:
            return False
        