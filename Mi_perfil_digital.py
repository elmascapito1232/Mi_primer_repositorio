#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Samuel David Gutiérrez Machuca"
edad = 14
estatura = 1.60
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("Sxmu3l1t0", "elmascapito1232")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "No cap", "artista": "El Americano 4KT", "duracion": "2:40"},
{"titulo": "Calaveras Caras", "artista": "El Americano 4KT", "duracion": "3:07"},
{"titulo": "Andan Diciendo", "artista": "Arcángel", "duracion": "6:02"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")
