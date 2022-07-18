from odoo import fields, models, api


class BookLocation(models.Model):
    _name = "book.location"
    _description = "Book Location"

    name = fields.Char('Name')

    books = fields.One2many("library.book", "location")

    total_available_books = fields.Integer(compute='_compute_total_available_books')

    @api.depends('books')
    def _compute_total_available_books(self):
        tot_books = 0
        for record in self:
            current_location = record.name
            for record_inside_books in self.books:
                if record_inside_books.location.name == current_location:
                    tot_books +=1
            record.total_available_books = tot_books
            tot_books = 0

