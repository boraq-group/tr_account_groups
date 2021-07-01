from odoo import api, models, fields
from odoo.addons.base.models.ir_model import IrModelData


class AccountGroup(models.Model):
    _inherit = "account.group"

    def name_get(self):
        return [(record.id, record.name) for record in self]


class JournalEntry(models.Model):
    _inherit = "account.move"


class JournalItem(models.Model):
    _inherit = "account.move.line"

    account_group_id = fields.Many2one('account.group', "Account Group", related="account_id.group_id", store=True)
