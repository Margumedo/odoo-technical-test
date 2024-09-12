from odoo import models, fields

class SchoolEvaluationResult(models.Model):
    _name = 'school.evaluation.result'
    _description = 'School Evaluation Result'

    evaluation_id = fields.Many2one('school.evaluation', string='Evaluation', required=True)
    student_id = fields.Many2one('school.student', string='Student', required=True)
    grade = fields.Float(string='Grade')
