from abc import ABC, abstractmethod

class Personaje(ABC):
  def __init__(self, nombre, puntosDeVida, nivel, ataque, velocidad, defensa):
    self.nombre = nombre
    self.puntosDeVida = puntosDeVida
    self.nivel = nivel
    self.ataque = ataque
    self.velocidad = velocidad
    self.defensa = defensa

  def getNombre(self):
    return self.nombre

  def getPuntosDeVida(self):
    return self.puntosDeVida

  def setPuntosDeVida(self, nuevaVida):
    self.puntosDeVida = nuevaVida

  def getVelocidad(self):
    return self.velocidad

  def getDefensa(self):
    return self.defensa

  @abstractmethod
  def subirNivel(self):
    pass

  def atacar(self, personajeRival):
    if personajeRival.getPuntosDeVida() <= 0:
      print("DEJALO, YA ESTA MUERTO")
    elif self.getPuntosDeVida() <= 0:
      print(f"{self.getNombre()} ESTAS MUERTO, NO PODES ATACAR")
    else:
      cantidadDeDanio = self.ataque + self.velocidad - personajeRival.getDefensa()
      nuevaVidaRival = personajeRival.getPuntosDeVida() - cantidadDeDanio
      personajeRival.setPuntosDeVida(nuevaVidaRival)
      print(f"{self.nombre} LE HIZO {cantidadDeDanio} DE ATAQUE A {personajeRival.nombre}")

  def mostrarEstadisticas(self):
    print(f"Nombre: {self.nombre}")
    print(f"Nivel: {self.nivel}")
    print(f"Puntos de vida: {self.puntosDeVida}")
    print(f"Ataque: {self.ataque}")
    print(f"Velocidad: {self.velocidad}")
    print(f"Defensa: {self.defensa}\n")

  def mostrarInfo(self):
    if self.puntosDeVida <= 0:
      print(f"Nombre: {self.nombre}")
      print(f"Vida: MUERTO")
    else:
      print(f"Nombre: {self.nombre}")
      print(f"Vida: {self.puntosDeVida}")

class Guerrero(Personaje):
  def __init__(self, nombre, puntosDeVida, nivel, ataque, velocidad, defensa):
    super().__init__(nombre, puntosDeVida, nivel, ataque, velocidad, defensa)

  def subirNivel(self):
    self.nivel += 1
    self.puntosDeVida += 300
    self.ataque += 20
    self.velocidad += 10
    self.defensa += 15


class Mago(Personaje):
  def __init__(self, nombre, puntosDeVida, nivel, ataque, velocidad, defensa):
    super().__init__(nombre, puntosDeVida, nivel, ataque, velocidad, defensa)

  def subirNivel(self):
    self.nivel += 1
    self.puntosDeVida += 50
    self.ataque += 5
    self.velocidad += 40
    self.defensa += 5

class Demonio(Personaje):
  def __init__(self, nombre, puntosDeVida, nivel, ataque, velocidad, defensa):
    super().__init__(nombre, puntosDeVida, nivel, ataque, velocidad, defensa)

  def subirNivel(self):
    self.nivel += 1
    self.puntosDeVida += 350
    self.ataque += 20
    self.velocidad += 5
    self.defensa += 18
    