from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list):
        nomes_empresas = []
        data_fabricacao = str(date.max)
        data_validade = str(date.max)
        data_hoje = str(date.today())
        for item in list:
            if item["data_de_fabricacao"] < data_fabricacao:
                data_fabricacao = item["data_de_fabricacao"]
            if data_hoje <= item["data_de_validade"] < data_validade:
                data_validade = item["data_de_validade"]
            nomes_empresas.append(item["nome_da_empresa"])
        empresa = Counter(nomes_empresas).most_common(1)[0][0]
        return (
            f"Data de fabricação mais antiga: {data_fabricacao}\n"
            f"Data de validade mais próxima: {data_validade}\n"
            f"Empresa com mais produtos: {empresa}"
        )
