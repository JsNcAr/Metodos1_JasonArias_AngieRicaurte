# -*- coding: utf-8 -*-

import numpy as np
"""## Problema

Un gancho puede realizar oscilaciones con amplitudes pequeñas en el plano del gancho alrededor de sus posiciones de equilibrio como se muestra en la figura. En las posiciones a) y b) el lado largo (base) se encuentra orientado de forma horizontal. Los otros dos lados tienen la misma longitud. Considerando que el periodo de oscilación es el mismo en los tres casos. 

¿Cuál es la ubicación del centro de masa del gancho?

![](https://raw.githubusercontent.com/diegour1/CompMetodosComputacionales/main/DataFiles/image1.PNG)


La figura no contiene ninguna información más alla de las dimensiones mostradas. En particular, no se sabe cómo se distribuye la masa. La base en la figura es de 0.42 m, y la altura de 0.1 m.

Siga los pasos siguientes para resolver el problema.

a) Construya la clase gancho con los siguientes atributos `mass`, `inertia`, `base`, `altura`, para ello cree el constructor de la clase Gancho, el cual debe recibir esos atributos como parametros y debe inicializar los atributos en el constructor. `inertia` se refiere a la inercia con respecto al centro de masa. Puede usar el siguiente [notebook](https://github.com/diegour1/CompMetodosComputacionales/blob/main/Notebooks/07%20-%20ObjectOrientedProgramming.ipynb) como referencia.
"""


class Gancho:

    def __init__(self, mass, inertia, base, altura):
        self.mass = mass
        self.inertia = inertia
        self.base = base
        self.altura = altura


# Codigo para verificar la respuesta (no modificar)

gancho_a = Gancho(1, 0.01, 0.42, 0.14)
print("Gancho a", gancho_a.mass, gancho_a.inertia, gancho_a.base,
      gancho_a.altura)
gancho_b = Gancho(3, 0.015, 0.3, 0.1)
print("Gancho b", gancho_b.mass, gancho_b.inertia, gancho_b.base,
      gancho_b.altura)
"""b) Argumente: Por qué se puede decir que el centro de masa del gancho se encuentra sobre la altura sobre del triangulo del gancho, altura en la figura (a) (la mediatriz de la base)?

Tu texto aqui

.

.

.

.

.

.

.

.

c) Copie su codigo anterior en esta sección, y ahora cree un metodo de la clase Gancho llamado `centro_de_masa(altura_cm)`  que asumiendo que la coordenada vertical del centro de masa se encuentra en `altura_cm` (ver figura), retorne un array con las dos dimensiones del centro de masa del gancho en las coordenadas de la figura mostrada.

![](https://raw.githubusercontent.com/diegour1/CompMetodosComputacionales/main/DataFiles/image3.png)
"""


class Gancho:

    def __init__(self, mass, inertia, base, altura):
        self.mass = mass
        self.inertia = inertia
        self.base = base
        self.altura = altura

    def centro_de_masa(self, altura_cm):
        base = self.base / 2

        cm = np.zeros(2)
        cm[0] = base
        cm[1] = altura_cm

        return cm


# Codigo para verificar la respuesta (no modificar)

gancho_a = Gancho(1, 0.01066, 0.42, 0.1)
print("centro de masa", gancho_a.centro_de_masa(0.75))
"""d) Copie su codigo anterior en esta sección, y ahora cree un metodo de la clase Gancho llamado `inertia_xy(altura_cm, x, y)`  que calcule un float que corresponde a la inercia respecto a cualquier punto `(x, y)` asumiendo que el centro de masa se encuentra en la altura `altura_cm`, de acuerdo a las coordenadas de la figura c)"""


class Gancho:

    def __init__(self, mass, inertia, base, altura):
        self.mass = mass
        self.inertia = inertia
        self.base = base
        self.altura = altura

    def centro_de_masa(self, altura_cm):
        base = self.base / 2

        cm = np.zeros(2)
        cm[0] = base
        cm[1] = altura_cm

        return cm

    def inertia_xy(self, altura_cm, x, y):
        cm = self.centro_de_masa(altura_cm)
        I = self.inertia + self.mass * (cm[0] - x)**2 + self.mass * (cm[1] -
                                                                     y)**2

        return I


# Codigo para verificar la respuesta (no modificar)

gancho_a = Gancho(1, 0.01066, 0.42, 0.10)
print("inertia punto (0.025, 0.03), altura cm 0.75:",
      gancho_a.inertia_xy(0.75, 0.025, 0.03))
"""e) Copie su codigo anterior en esta sección, y ahora cree un metodo de la clase Gancho llamado `periodo_oscilacion(altura_cm, x, y)`  que calcule un float que corresponde al periodo de oscilacion, con respecto a cualquier eje de rotación `(x, y)` asumiendo que el centro de masa esta en la altura `altura_cm`, de acuerdo a las coordenadas de la figura c)"""


class Gancho:

    def __init__(self, mass, inertia, base, altura):
        self.mass = mass
        self.inertia = inertia
        self.base = base
        self.altura = altura

    def centro_de_masa(self, altura_cm):
        base = self.base / 2

        cm = np.zeros(2)
        cm[0] = base
        cm[1] = altura_cm

        return cm

    def inertia_xy(self, altura_cm, x, y):
        cm = self.centro_de_masa(altura_cm)
        I = self.inertia + self.mass * (cm[0] - x)**2 + self.mass * (cm[1] -
                                                                     y)**2

        return I

    def periodo_oscilacion(self, altura_cm, x, y):
        I = self.inertia_xy(altura_cm, x, y)
        T = 2 * np.pi * np.sqrt(I / self.mass)

        return T


# Codigo para verificar la respuesta (no modificar)

gancho_a = Gancho(1, 0.01066, 0.42, 0.1)
print("perido de oscilacion con eje (0.025, 0.03), altura cm 0.75",
      gancho_a.periodo_oscilacion(0.75, 0.025, 0.03))
"""f) A partir de la clase Gancho construida, diseñe un metodo para calcular el centro de masa del gancho.

Retorne un array con las dos coordenadas del centro de masa del gancho.
"""

gancho1 = Gancho(1, 0.01066, 0.42, 0.1)
cm_gancho = np.zeros(2)

cm_gancho[0], cm_gancho[1] = gancho1.centro_de_masa(gancho1.altura / 3)

# codigo para verificar su codigo (no modificar)
print(cm_gancho)
"""g) Note que el centro de masa no depende de la distribución de la masa. Cómo resolveria el problema de forma análitica?

Tu texto aqui

.

.

.

.

.

.

.

.
"""