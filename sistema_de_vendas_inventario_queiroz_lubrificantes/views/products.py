from ..components import Button, Column, Divider, Label, Row, Table
from ..views import ViewModel, view_controller


class Model(ViewModel):
    def __init__(self) -> None:
        self.id = "products"

    def update(self):
        self.m_table = Table(
            headings=["Nome", "Marca", "Referencia", "Preco", "Quantidade"],
            data_source=view_controller.database.produto.listar,
            filter_source=view_controller.database.produto.buscar,
            style={"flex": 1},
        )

        view_controller.update_main(
            [
                Column(
                    [
                        Label("Produtos"),
                        Divider(),
                        self.m_table,
                        Divider(),
                        Row(
                            [
                                Button(
                                    "Criar Produto",
                                    lambda _: view_controller.redirect_to(
                                        "product_create"
                                    ),
                                    {"flex": 1, "padding_right": 10},
                                ),
                                Button(
                                    "Alterar Produto",
                                    lambda _: self.product_update_handle(),
                                    {"flex": 1, "padding_right": 10},
                                ),
                                Button(
                                    "Excluir Produto",
                                    lambda _: self.product_delete_handle(),
                                    {"flex": 1},
                                ),
                            ]
                        ),
                    ],
                    {"flex": 1},
                )
            ]
        )

    def product_delete_handle(self):
        product = self.m_table.selected()
        if not product or "id" not in product:
            return

        view_controller.database.produto.excluir(product["id"])
        self.m_table.update()

    def product_update_handle(self):
        product = self.m_table.selected()
        if not product:
            return

        view_controller.redirect_to("product_update", product)


view_controller.register_model(Model())
