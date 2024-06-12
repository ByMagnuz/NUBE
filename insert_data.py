from chat.models import Carrera, Persona, Mensaje
from datetime import date

# Insertar carreras
c1 = Carrera.objects.create(nombre='Arquitectura Moderna', status=False)
c2 = Carrera.objects.create(nombre='Ingeniería Estructural', status=False)
c3 = Carrera.objects.create(nombre='Diseño de Interiores', status=False)

# Insertar personas
p1 = Persona.objects.create(nombre='Carlos Alberto', ap_pat='Hernández', ap_mat='Pérez', usu='calberto', pass_field='newpassword123', fecha_nac=date(1990, 11, 15), carrera=c1, status=False)
p2 = Persona.objects.create(nombre='María Fernanda', ap_pat='Lozano', ap_mat='García', usu='mfernanda', pass_field='newpassword123', fecha_nac=date(1989, 5, 22), carrera=c1, status=False)
p3 = Persona.objects.create(nombre='Miguel Ángel', ap_pat='Sánchez', ap_mat='Martínez', usu='mangel', pass_field='newpassword123', fecha_nac=date(1991, 8, 19), carrera=c2, status=False)
p4 = Persona.objects.create(nombre='Ana Isabel', ap_pat='Ramírez', ap_mat='Torres', usu='aisabel', pass_field='newpassword123', fecha_nac=date(1992, 1, 3), carrera=c2, status=False)
p5 = Persona.objects.create(nombre='Luis Eduardo', ap_pat='Fernández', ap_mat='Ruiz', usu='leduardo', pass_field='newpassword123', fecha_nac=date(1988, 4, 9), carrera=c3, status=False)
p6 = Persona.objects.create(nombre='Laura Patricia', ap_pat='Gómez', ap_mat='Jiménez', usu='lpatricia', pass_field='newpassword123', fecha_nac=date(1993, 9, 25), carrera=c3, status=False)

# Insertar mensajes
Mensaje.objects.create(txt_mensaje='Hola a todos, soy Carlos Alberto.', persona=p1, status=False)
Mensaje.objects.create(txt_mensaje='Buenos días, soy María Fernanda.', persona=p2, status=False)
Mensaje.objects.create(txt_mensaje='Hola, soy Miguel Ángel.', persona=p3, status=False)
Mensaje.objects.create(txt_mensaje='Hola, soy Ana Isabel.', persona=p4, status=False)
Mensaje.objects.create(txt_mensaje='Hola, soy Luis Eduardo.', persona=p5, status=False)
Mensaje.objects.create(txt_mensaje='Hola, soy Laura Patricia.', persona=p6, status=False)

print("Datos insertados correctamente.")
