{
    'name': 'School Management',
    'version': '16.0.1.0.0',
    'summary': 'Manage School Subjects, Students, Teachers and Evaluations',
    'description': 'Modulo para el manejo de perfiles de escuela, Estudiantes, Profesores y Evaluaciones',
    'category': 'Educacion',
    'author': 'Maicol Argumedo',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/school_subject_views.xml',
        'views/school_student_views.xml',
        'views/school_teacher_views.xml',
        'views/school_evaluation_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
