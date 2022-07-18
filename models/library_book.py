from datetime import datetime, date
from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'

    _inherit = ['mail.thread',"library.book",'mail.activity.mixin']

    isbn = fields.Char('ISBN', tracking = True, required=True)    

    description = fields.Text('Descripcion')

    status = fields.Selection(string='Status',
        selection=[('not_published', 'Not Published'), ('available', 'Available'), ('borrowed', 'Borrowed'),('lost', 'Lost')], default='available' )
    
    current_borrower_id =  fields.Many2one('res.partner', string='Current borrower', tracking = True)
    
    return_date = fields.Datetime('Return Date')

    location =  fields.Many2one('book.location', string='Current Location')

    def action_lease(self):
        return {
              'name': 'Book Lease',              
              "view_mode": 'form',              
              'res_model': 'package.borrower.wizard',
              'type': 'ir.actions.act_window',
              'target': 'new',
              'context': self.env.context,
              }

    @api.onchange('date_release')
    def _onchange_date_release(self):

        if self.date_release != False :            
            if self.date_release > date.today():
                self.status = 'not_published'


    @api.constrains('isbn')
    def _check_unique_isbn(self):        
        if self.search_count([('isbn', '=', self.isbn)]) > 1:        
            raise ValidationError(f"Existing ISBN -- {self.isbn} for this book: {self.name}")