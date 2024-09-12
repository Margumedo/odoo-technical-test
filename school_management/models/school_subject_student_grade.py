from odoo import api, models, fields

class SchoolSubjectStudentGrade(models.Model):
    _name = 'school.subject.student.grade'
    _description = 'Final Grade for Each Student in Each Subject'

    student_id = fields.Many2one('school.student', string='Student', required=True)
    subject_id = fields.Many2one('school.subject', string='Subject', required=True)  # Asegúrate de que este campo exista
    final_exam_grade = fields.Float(string='Final Exam Grade', compute='_compute_final_exam_grade', store=True)

    @api.depends('subject_id.evaluation_ids.result_ids')
    def _compute_final_exam_grade(self):
        """Calcula la nota final del estudiante para esta materia."""
        for grade in self:
            total_grades = 0.0
            total_evaluations = 0
            # Recorre todas las evaluaciones de la materia
            for evaluation in grade.subject_id.evaluation_ids:
                # Recorre todos los resultados de las evaluaciones
                for result in evaluation.result_ids:
                    if result.student_id == grade.student_id:
                        total_grades += result.grade
                        total_evaluations += 1
            # Asigna la nota final para cada estudiante en esta materia
            grade.final_exam_grade = total_grades / total_evaluations if total_evaluations > 0 else 0.0
