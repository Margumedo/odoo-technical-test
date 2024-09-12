from odoo import models, fields

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'School Subject'

    name = fields.Char(string='Name', required=True)
    credits = fields.Integer(string='Credits')
    max_students = fields.Integer(string='Max Students')
    active = fields.Boolean(string='Active', default=True)
    student_ids = fields.Many2many('school.student', string='Students')
    teacher_id = fields.Many2one('school.teacher', string='Teacher')
    evaluation_ids = fields.One2many('school.evaluation', 'subject_id', string='Evaluations')
    student_grades = fields.One2many('school.subject.student.grade', 'subject_id', string='Student Grades')  # Relación con el campo inverso correcto
