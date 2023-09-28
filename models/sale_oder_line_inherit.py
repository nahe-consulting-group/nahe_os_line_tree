from odoo import api, fields, models


class SaleOrderLineInherit(models.Model):
    _inherit = "sale.order.line"

    related_partner_id = fields.Many2one(
        "res.partner",
        string="Cliente relacionado",
        related="order_id.partner_id",
        readonly=True,
        store=True,
    )

    related_date_order = fields.Datetime(
        string="Fecha de orden relacionada",
        related="order_id.date_order",
        readonly=True,
        store=True,
    )

    qty_not_delivered = fields.Float(
        string="Cantidad Pendiente",
        compute="_compute_qty_not_delivered",
        store=True,
    )

    @api.depends("product_uom_qty", "qty_delivered")
    def _compute_qty_not_delivered(self):
        for record in self:
            record.qty_not_delivered = record.product_uom_qty - record.qty_delivered
