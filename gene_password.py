import secrets
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

longitud_contraseña = 12  # Puedes ajustar la longitud según tus necesidades
contraseña_segura = generar_contraseña(longitud_contraseña)
print("Contraseña segura:", contraseña_segura)
