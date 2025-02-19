{
    "name": "Grading Management",
    "summary": "Grading Management",
    "description": "Grading management module",
    "version": "17.0.1.0.0",
    "category": "Training",
    "depends": ["base",'mail','hr'],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/base_menu.xml",
        "views/grade_view.xml",
        "views/wage_inherited_view.xml"

    ],
    "application": True,
}