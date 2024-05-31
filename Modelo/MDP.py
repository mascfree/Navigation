class MDP:
    def __init__(self, grafo, factor_descuento=0.9):
        """
        Inicializa un Proceso de Decisión de Markov (MDP).

        Args:
            grafo: Grafo que representa el entorno del MDP.
            factor_descuento: Factor de descuento para futuras recompensas (por defecto 0.9).
        """
        self.grafo = grafo
        self.factor_descuento = factor_descuento
        self.V = {nombre: 0 for nombre in grafo.nodos}  # Inicializar los valores de los estados en 0

    def iteracion_de_valor(self, max_iter=1000, tol=1e-6):
        """
        Realiza la Iteración de Valor para encontrar los valores óptimos de los estados.

        Args:
            max_iter: Número máximo de iteraciones (por defecto 1000).
            tol: Tolerancia para la convergencia (por defecto 1e-6).
        """
        for i in range(max_iter):
            delta = 0 # Variable para rastrear el cambio máximo en los valores de los estados durante esta iteración
            for nombre, nodo in self.grafo.nodos.items():
                v = self.V[nombre]
                self.V[nombre] = self.valor_de_estado(nodo)
                delta = max(delta, abs(v - self.V[nombre]))
            if delta < tol:
                break

    def valor_de_estado(self, nodo):
        """
        Calcula el valor de un estado dado según la ecuación de Bellman.

        Args:
            nodo: Nodo cuyo valor de estado se calculará.

        Returns:
            El valor de estado calculado para el nodo.
        """
        if nodo.estado.es_meta:
            return 0
        return max(
            self.ecuacion_de_bellman(nodo, accion)
            for accion in set(arista.accion for arista in nodo.estado.aristas)
        )

    def ecuacion_de_bellman(self, nodo, accion):
        """
        Calcula el valor de un estado según la ecuación de Bellman.

        Args:
            nodo: Estado actual.
            accion: Acción tomada desde el estado actual.

        Returns:
            El valor de estado calculado según la ecuación de Bellman.
        """
        return sum(
            arista.accion.probabilidad * (
                self.recompensa(nodo, accion, arista.destino) + 
                self.factor_descuento * self.V[arista.destino.nombre]
            )
            for arista in nodo.estado.aristas if arista.accion == accion
        )

    def recompensa(self, nodo, accion, siguiente_nodo):
        """
        Calcula la recompensa asociada a una acción que lleva de un estado a otro.

        Args:
            nodo: Estado actual.
            accion: Acción tomada.
            siguiente_nodo: Estado resultante de tomar la acción.

        Returns:
            La recompensa asociada a la transición.
        """
        if siguiente_nodo.es_mortal:
            return -100
        elif siguiente_nodo.es_meta:
            return 100
        else:
            return 1

    def imprimir_valores(self):
        """
        Imprime los valores de los estados después de la Iteración de Valor.
        """
        print("Valores de los estados después de la Iteración de Valor:")
        for estado, valor in self.V.items():
            print(f"Estado {estado}: {valor}")

    def iteracion_de_politica(self, max_iter=1000, tol=1e-6):
        """
        Realiza la Iteración de Política para encontrar la política óptima.

        Args:
            max_iter: Número máximo de iteraciones (por defecto 1000).
            tol: Tolerancia para la convergencia (por defecto 1e-6).

        Returns:
            La política óptima encontrada.
        """
        politica = {nombre: None for nombre in self.grafo.nodos}
        for i in range(max_iter):
            self.evaluacion_de_politica(politica, tol)
            politica_estable = True
            for nombre, nodo in self.grafo.nodos.items():
                mejor_politica = self.mejora_politica(nodo)
                if mejor_politica != politica[nombre]:
                    politica_estable = False
                    politica[nombre] = mejor_politica
            if politica_estable:
                break
        return politica

    def evaluacion_de_politica(self, politica, tol):
        """
        Realiza la evaluación de la política actual.

        Args:
            politica: La política actual a evaluar.
            tol: Tolerancia para la convergencia.
        """
        for i in range(1000):  # max_iter interno para evaluación de política
            delta = 0
            for nombre, nodo in self.grafo.nodos.items():
                v = self.V[nombre]
                accion = politica[nombre]
                if accion:
                    self.V[nombre] = self.ecuacion_de_bellman(nodo, accion)
                delta = max(delta, abs(v - self.V[nombre]))
            if delta < tol:
                break

    def mejora_politica(self, nodo):
        """
        Encuentra la mejor acción para un estado dado.

        Args:
            nodo: El nodo (estado) para el cual se busca la mejor acción.

        Returns:
            La mejor acción para el estado dado.
        """
        return max(
            (arista.accion for arista in nodo.estado.aristas),
            key=lambda accion: self.ecuacion_de_bellman(nodo, accion),
            default=None
        )

    def imprimir_politica(self, politica):
        """
        Imprime la política resultante.

        Args:
            politica: La política a imprimir.
        """
        print("Política resultante:")
        for estado, accion in politica.items():
            direccion = accion.direccion
            probabilidad = accion.probabilidad
            if direccion == "N":
                accion_con_flecha = "↑"
            elif direccion == "S":
                accion_con_flecha = "↓"
            elif direccion == "E":
                accion_con_flecha = "→"
            elif direccion == "W":
                accion_con_flecha = "←"
            else:
                accion_con_flecha = accion  # Si no es una dirección válida, imprime la acción tal como está
            print(f"Estado {estado}: {accion_con_flecha} (Probabilidad: {probabilidad})")
