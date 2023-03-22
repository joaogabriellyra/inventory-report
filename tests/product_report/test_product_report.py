from inventory_report.inventory.product import Product


def test_relatorio_produto():
    mock1 = "O produto RAÇÃO fabricado em 2022-04-04 por Agroneto com validade"
    mock2 = " até 2023-02-09 precisa ser armazenado Conservar em local fresco."
    produto = Product(
        1, "RAÇÃO", "Agroneto", "2022-04-04", "2023-02-09",
        "FR48", "Conservar em local fresco"
    )

    assert produto.__repr__() == mock1 + mock2
