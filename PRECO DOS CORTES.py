
class Cabelo:
     _id: int
     _nome: str
     _preco: float

     def _init_(self, id, nome, preco):
         self._nome = nome
         self._preco = preco
         self._id = id

     @property
     def nome(self):
         return self._nome

      @nome.setter
      def nome(self, ):
          self._nome = nome

      @property
      def preco(self):
          return self._id

      @preco.setter
      def preco(self, preco):
          self._preco = preco
