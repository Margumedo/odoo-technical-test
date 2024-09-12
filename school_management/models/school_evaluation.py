from odoo import models, fields

class SchoolEvaluation(models.Model):
    _name = 'school.evaluation'
    _description = 'School Evaluation'

    name = fields.Char(string='Evaluation Name', required=True)
    date = fields.Date(string='Date', required=True)
    subject_id = fields.Many2one('school.subject', string='Subject', required=True)
    teacher_id = fields.Many2one('school.teacher', string='Teacher', required=True)
    student_ids = fields.Many2many('school.student', string='Students')
    result_ids = fields.One2many('school.evaluation.result', 'evaluation_id', string='Results')  # Relación con resultados
