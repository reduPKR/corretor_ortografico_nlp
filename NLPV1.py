import nltk as nltk


# nltk.download('punkt')


class NLPV1:
    total_palavras = 0
    frequencia = []
    def abrir_arquivo(self):
        with open("dados/artigos.txt", "r", encoding="utf-8") as arq:
            artigos = arq.read()

            tokens = nltk.tokenize.word_tokenize(artigos)
            texto = self.separar_palavras(tokens)

            normalizada = self.normalizar(texto)
            self.total_palavras = len(normalizada)
            self.frequencia = nltk.FreqDist(normalizada)

            palavras = self.remover_palavras_repetidas(normalizada)

            print(f"Total de tokens {len(tokens)}")
            print(f"Total de palavras {len(palavras)}")

            print(self.corretor('lógia'))


    def separar_palavras(self, tokens):
        palavras = []
        for item in tokens:
            if item.isalpha():
                palavras.append(item)

        return palavras


    def normalizar(self, palavras):
        normalizada = []
        for item in palavras:
            if item.isalpha():
                normalizada.append(item.lower())

        return normalizada

    def remover_palavras_repetidas(self,normalizada):
       return set(normalizada)

    def corretor(self,palavra):
        variantes = self.gerar_palavras(palavra)
        print(variantes)

        #retorna a variante com maior probalidade de ser a palavra correta
        return max(variantes, key=self.calcular_propabilidade)


    def gerar_palavras(self, palavra):
        fatias = []
        palavras = []
        for i in range(len(palavra)+1):
            fatias.append((palavra[:i], palavra[i:]))
            palavras = self.insere_letras(fatias)

        return palavras

    def insere_letras(self,fatias):
        novas_palavras = []

        letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
        for esquerdo, direito in fatias:
            for letra in letras:
                novas_palavras.append(esquerdo + letra + direito)

        return novas_palavras

    def calcular_propabilidade(self, variante):
        return self.frequencia[variante] / self.total_palavras