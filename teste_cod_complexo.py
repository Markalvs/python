from dataclasses import dataclass, asdict
from datetime import datetime
from collections import defaultdict
import json


@dataclass
class Venda:
    produto: str
    vendedor: str
    categoria: str
    quantidade: int
    preco_unitario: float
    data: datetime

    @property
    def faturamento(self) -> float:
        return self.quantidade * self.preco_unitario


class SistemaVendas:

    def __init__(self, vendas: list[Venda]):
        self.vendas = vendas

    def faturamento_total(self) -> float:
        return sum(v.faturamento for v in self.vendas)

    def produto_mais_vendido(self) -> str:
        quantidade_por_produto = defaultdict(int)

        for venda in self.vendas:
            quantidade_por_produto[venda.produto] += venda.quantidade

        return max(
            quantidade_por_produto,
            key=quantidade_por_produto.get
        )

    def faturamento_por_categoria(self) -> dict[str, float]:
        resultado = defaultdict(float)

        for venda in self.vendas:
            resultado[venda.categoria] += venda.faturamento

        return dict(resultado)

    def vendas_por_vendedor(self) -> dict[str, float]:
        resultado = defaultdict(float)

        for venda in self.vendas:
            resultado[venda.vendedor] += venda.faturamento

        return dict(resultado)

    def maior_venda(self) -> Venda:
        return max(
            self.vendas,
            key=lambda venda: venda.faturamento
        )

    def media_por_venda(self) -> float:
        if not self.vendas:
            return 0

        return self.faturamento_total() / len(self.vendas)

    def gerar_relatorio(self) -> dict:

        vendedor_destaque = max(
            self.vendas_por_vendedor(),
            key=self.vendas_por_vendedor().get
        )

        maior_venda = self.maior_venda()

        return {
            "faturamento_total": self.faturamento_total(),
            "media_por_venda": self.media_por_venda(),
            "produto_mais_vendido": self.produto_mais_vendido(),
            "vendedor_destaque": vendedor_destaque,
            "faturamento_por_categoria": self.faturamento_por_categoria(),
            "faturamento_por_vendedor": self.vendas_por_vendedor(),
            "maior_venda": {
                "produto": maior_venda.produto,
                "vendedor": maior_venda.vendedor,
                "valor": maior_venda.faturamento
            }
        }

    def exportar_json(self, arquivo: str) -> None:

        dados = []

        for venda in self.vendas:
            venda_dict = asdict(venda)
            venda_dict["data"] = venda.data.isoformat()
            venda_dict["faturamento"] = venda.faturamento
            dados.append(venda_dict)

        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)


def criar_vendas() -> list[Venda]:

    return [
        Venda(
            "Notebook",
            "Ana",
            "Eletrônicos",
            2,
            3500,
            datetime(2026, 8, 1)
        ),

        Venda(
            "Mouse",
            "Carlos",
            "Periféricos",
            10,
            120,
            datetime(2026, 8, 2)
        ),

        Venda(
            "Teclado",
            "Ana",
            "Periféricos",
            5,
            250,
            datetime(2026, 8, 3)
        ),

        Venda(
            "Monitor",
            "Mariana",
            "Eletrônicos",
            3,
            1800,
            datetime(2026, 8, 5)
        ),

        Venda(
            "Notebook",
            "Carlos",
            "Eletrônicos",
            1,
            3500,
            datetime(2026, 8, 7)
        ),

        Venda(
            "Headset",
            "Mariana",
            "Periféricos",
            8,
            300,
            datetime(2026, 8, 10)
        ),

        Venda(
            "Monitor",
            "Ana",
            "Eletrônicos",
            2,
            1800,
            datetime(2026, 8, 12)
        )
    ]


def main():

    try:

        vendas = criar_vendas()

        sistema = SistemaVendas(vendas)

        relatorio = sistema.gerar_relatorio()

        print("=" * 50)
        print("RELATÓRIO DE VENDAS")
        print("=" * 50)

        print(
            f"Faturamento total: "
            f"R$ {relatorio['faturamento_total']:,.2f}"
        )

        print(
            f"Média por venda: "
            f"R$ {relatorio['media_por_venda']:,.2f}"
        )

        print(
            f"Produto mais vendido: "
            f"{relatorio['produto_mais_vendido']}"
        )

        print(
            f"Vendedor destaque: "
            f"{relatorio['vendedor_destaque']}"
        )

        print("\nFATURAMENTO POR CATEGORIA")

        for categoria, valor in (
            relatorio["faturamento_por_categoria"].items()
        ):
            print(f"{categoria}: R$ {valor:,.2f}")

        print("\nFATURAMENTO POR VENDEDOR")

        for vendedor, valor in (
            relatorio["faturamento_por_vendedor"].items()
        ):
            print(f"{vendedor}: R$ {valor:,.2f}")

        print("\nMAIOR VENDA")

        maior = relatorio["maior_venda"]

        print(f"Produto: {maior['produto']}")
        print(f"Vendedor: {maior['vendedor']}")
        print(f"Valor: R$ {maior['valor']:,.2f}")

        sistema.exportar_json("vendas.json")

        print("\nArquivo 'vendas.json' criado com sucesso.")

    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")


if __name__ == "__main__":
    main()