# __manifest__.py

{
    'name': 'Custom Product Label',
    'version': '1.0',
    'depends': ['base', 'product'],
    'data': [
        'report/product_label_template.xml',
        'views/product_label_view.xml',
    ],
}
