{
    "name": "Hospital Management",
    "author": "Nelson Musonda",
    "licence": "LGPL-3",
    "version": "1.0.0",
    "category": "health",
    "depends": ["sale_management"],
    "data": [
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/test_view.xml',
        'views/inherit_sale_order.xml',
        'views/doctor_view.xml',
        'reports/template_report_test.xml',
        'reports/action_report_test.xml',
        "views/menu.xml"
    ],
    'installable': True,
    'application': True,
     'auto_install': False
}