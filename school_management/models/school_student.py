from odoo import models, fields, api
from datetime import date

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Birth Date')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    average_grade = fields.Float(string='Average Grade', compute='_compute_average_grade', store=True)  # Promedio General del Estudiante
    subject_ids = fields.Many2many('school.subject', string='Subjects')
    final_exam_grades = fields.One2many('school.subject.student.grade', 'student_id', string='Final Exam Grades')  # Notas Finales por Materia

    @api.depends('birth_date')
    def _compute_age(self):
        """Calcula la edad basada en la fecha de nacimiento."""
        for record in self:
            if record.birth_date:
                today = date.today()
                birthdate = record.birth_date
                record.age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            else:
                record.age = 0

    @api.depends('subject_ids.evaluation_ids.result_ids')
    def _compute_average_grade(self):
        """Calcula el promedio general del estudiante basado en todas las evaluaciones."""
        for student in self:
            total_grades = 0.0
            total_evaluations = 0
            # Recorre todas las materias en las que el estudiante está inscrito
            for subject in student.subject_ids:
                # Recorre todas las evaluaciones de la materia
                for evaluation in subject.evaluation_ids:
                    # Recorre todos los resultados de las evaluaciones
                    for result in evaluation.result_ids:
                        if result.student_id == student:
                            total_grades += result.grade
                            total_evaluations += 1
            # Calcula el promedio si hay evaluaciones
            student.average_grade = total_grades / total_evaluations if total_evaluations > 0 else 0.0
