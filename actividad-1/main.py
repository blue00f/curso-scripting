from personajes import Guerrero, Mago, Demonio

guerrero1 = Guerrero("Darius", 500, 1, 50, 25, 30)
mago1 = Mago("Lux", 300, 1, 20, 60, 5)
demonio1 = Demonio("Aatrox", 550, 1, 40, 20, 40)

print("\nEstadisticas iniciales\n")
guerrero1.mostrarEstadisticas()
mago1.mostrarEstadisticas()
demonio1.mostrarEstadisticas()

print("Los 3 personajes subieron de nivel\n")
guerrero1.subirNivel()
mago1.subirNivel()
demonio1.subirNivel()

print("Estadisticas despues de subir de nivel\n")
guerrero1.mostrarEstadisticas()
mago1.mostrarEstadisticas()
demonio1.mostrarEstadisticas()

print(f"Pelea entre {guerrero1.getNombre()} y {mago1.getNombre()}")

if mago1.getVelocidad() >= guerrero1.getVelocidad():
  # Primero ataca el mago
  for i in range(8):
    mago1.atacar(guerrero1)

  # Ahora ataca el guerrero
  if guerrero1.getPuntosDeVida() >= 0:
    for i in range(4):
      guerrero1.atacar(mago1)

print("\nEstadisticas despues de los ataques")
guerrero1.mostrarInfo()
mago1.mostrarInfo()

print(f"\nEl guerrero {guerrero1.getNombre()} subio de nivel por ganar la batalla")
guerrero1.subirNivel()
guerrero1.subirNivel()
guerrero1.mostrarEstadisticas()

print(f"\nPelea entre {guerrero1.getNombre()} y {demonio1.getNombre()}")

if guerrero1.getVelocidad() >= demonio1.getVelocidad():
  # Primero ataca el guerrero
  for i in range(10):
    guerrero1.atacar(demonio1)

  # Ahora ataca el demonio
  if demonio1.getPuntosDeVida() >= 0:
    for i in range(8):
      demonio1.atacar(guerrero1)

print("\nEstadisticas despues de los ataques")
guerrero1.mostrarInfo()
demonio1.mostrarInfo()
