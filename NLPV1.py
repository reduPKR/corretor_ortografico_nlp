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

            self.remover_palavras_repetidas(normalizada)

            #print(f"Total de tokens {len(tokens)}")
            #print(f"Total de palavras {len(palavras)}")

            self.testar(normalizada);
            print(f"lógia foi corrigida para {self.corretor('lógia', normalizada)}")
            print(f"lóigica foi corrigida para {self.corretor('lóigica', normalizada)}")
            print(f"lórica foi corrigida para {self.corretor('lórica', normalizada)}")
            print(f"lgóica foi corrigida para {self.corretor('lgóica', normalizada)}")


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

    def corretor(self,palavra, normalizada):
        variantes = self.gerar_palavras(palavra, normalizada)
        #print(variantes)

        #retorna a variante com maior probalidade de ser a palavra correta
        return max(variantes, key=self.calcular_propabilidade)

    def gerar_palavras(self, palavra, normalizada):
        fatias = []
        palavras = []
        melhores = []

        for i in range(len(palavra) + 1):
            fatias.append((palavra[:i], palavra[i:]))
            palavras = self.insere_letras(fatias)
            palavras += self.delete_letras(fatias)
            palavras += self.troca_letras(fatias)
            palavras += self.inverter_letras(fatias)

        return set(palavras)

    def insere_letras(self,fatias):
        novas_palavras = []

        letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
        for esquerdo, direito in fatias:
            for letra in letras:
                novas_palavras.append(esquerdo + letra + direito)

        return novas_palavras

    def delete_letras(self, fatias):
        novas_palavras = []

        for esquerdo, direito in fatias:
            novas_palavras.append(esquerdo + direito[1:])

        return novas_palavras

    def troca_letras(self,fatias):
        novas_palavras = []

        letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
        for esquerdo, direito in fatias:
            for letra in letras:
                novas_palavras.append(esquerdo + letra + direito[1:])

        return novas_palavras

    def inverter_letras(self,fatias):
        novas_palavras = []

        for esquerdo, direito in fatias:
            if len(direito) > 1 :
                novas_palavras.append(esquerdo + direito[1] + direito[0] + direito[2:])

        return novas_palavras

    def calcular_propabilidade(self, variante):
        return self.frequencia[variante] / self.total_palavras

    def testar(self,normalizada):
        palavras = self.criar_dados_teste()
        self.avaliador(palavras, normalizada)

    def criar_dados_teste(self):
        lista_palavras = []
        with open("dados/palavras.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                correta, incorreta = linha.split()
                lista_palavras.append((correta, incorreta))

        return lista_palavras

    def avaliador(self, palavras, normalizada):
        qtde_palavras = len(palavras)
        acertos = 0
        desconhecida = 0

        for correta,incorreta in palavras:
            desconhecida += (correta not in normalizada)

            retorno = self.corretor(incorreta, normalizada)
            if retorno == correta:
                acertos += 1


        taxta_acerto = round(acertos*100/qtde_palavras, 2)
        taxta_desconhecida = round(desconhecida * 100 / qtde_palavras, 2)
        print(f"taxa de acerto {taxta_acerto} % de {qtde_palavras} palavras")
        print(f"taxa de palavras desconhecidas: {taxta_desconhecida}")