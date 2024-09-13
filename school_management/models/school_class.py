from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char(string='Name', required=True)
    subject_id = fields.Many2one('school.subject', string='Subject', required=True)
    teacher_id = fields.Many2one('school.teacher', string='Teacher', required=True)
    student_ids = fields.Many2many('school.student', string='Enrolled Students')
    start_datetime = fields.Datetime(string='Start Date & Time', required=True)
    end_datetime = fields.Datetime(string='End Date & Time', required=True)

    @api.constrains('start_datetime', 'end_datetime')
    def _check_dates(self):
        """Validacion para asegurar que las clases son correctamente creadas"""
        for record in self:
            if record.start_datetime < datetime.now():
                raise ValidationError("la fecha de inicio no puede ser en le pasado")
            if record.end_datetime <= record.start_datetime:
                raise ValidationError("La fecha final debe ser mayor a la inicial")
