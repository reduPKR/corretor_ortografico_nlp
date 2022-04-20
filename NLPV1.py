import nltk as nltk


# nltk.download('punkt')

class NLPV1:
    def abrir_arquivo(self):
        with open("dados/artigos.txt", "r", encoding="utf-8") as arq:
            artigos = arq.read()

            tokens = nltk.tokenize.word_tokenize(artigos)
            texto = self.separar_palavras(tokens)
            normalizada = self.normalizar(texto)
            palavras = self.remover_palavras_repetidas(normalizada)


            print(f"Total de tokens {len(tokens)}")
            print(f"Total de palavras {len(palavras)}")


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

    def remover_palavras_repetidas(self, palavras):
       return set(palavras)
