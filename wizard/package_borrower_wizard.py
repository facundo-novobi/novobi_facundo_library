from pkg_resources import require
from odoo import models, fields


class PackageBorrowerWizard(models.TransientModel):
    _name = 'package.borrower.wizard'    
    _description = 'Package Borrower Wizard'

    borrower = fields.Many2one('res.partner', string='Borrower', required=True)    
    return_date = fields.Date('Return Date', required=True)    
    book_id = fields.Many2one('library.book', string="Book")


    def action_confirm_borrower(self):
        for record in self:            
            record.book_id = self.env.context['active_id']
            self.book_id.current_borrower_id = self.borrower
            self.book_id.status = 'borrowed'            
        return
    
    def action_cancel(self):
        return

        
            