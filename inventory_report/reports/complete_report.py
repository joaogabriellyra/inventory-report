from .simple_report import SimpleReport
from datetime import date
from collections import Counter


def generate_product(list):
    output = ""
    for product in list:
        output += f"- {product}: {list[product]}\n"
    return output


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(lista_de_produtos):
        data_fabricacao_antiga = str(date.max)
        data_validade = str(date.max)
        data_hoje = str(date.today())
        nome_das_empresas = []
        for produto in lista_de_produtos:
            if produto["data_de_fabricacao"] < data_fabricacao_antiga:
                data_fabricacao_antiga = produto["data_de_fabricacao"]
            if data_hoje <= produto["data_de_validade"] < data_validade:
                data_validade = produto["data_de_validade"]
            nome_das_empresas.append(produto["nome_da_empresa"])
        empresas = Counter(nome_das_empresas)
        emp_mais_produtos = empresas.most_common(1)[0][0]
        return (
            f"Data de fabricação mais antiga: {data_fabricacao_antiga}\n"
            f"Data de validade mais próxima: {data_validade}\n"
            f"Empresa com mais produtos: {emp_mais_produtos}\n"
            f"Produtos estocados por empresa:\n{generate_product(empresas)}"
        )
