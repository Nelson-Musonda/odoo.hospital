{
    "name": "Hospital Management",
    "author": "Nelson Musonda",
    "licence": "LGPL-3",
    "version": "1.0.0",
    "category": "health",
    "depends": ["sale_management", "account_accountant"],
    "data": [
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/test_view.xml',
        'views/inherit_views.xml',
        'views/doctor_view.xml',
        'reports/report_test.xml',
        'reports/report_inherits.xml',
        "views/menu.xml"
    ],
    'installable': True,
    'application': True,
     'auto_install': False
}