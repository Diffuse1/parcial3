class vertice():
    def __init__(self,valor) -> None:
        self.valor = valor
        pass
    pass
class arista(vertice):
    def __init__(self, origen, destino,peso) -> None:
        super().__init__(origen)
        super().__init__(destino)
        self.arista = { super().__init__(origen):{super().__init__(destino):peso}}
    pass
class grafo (arista):
    def __init__(self, origen, destino, paso) -> None:
        super().__init__(origen, destino, paso)
    pass

    