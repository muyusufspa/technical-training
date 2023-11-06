{
    "name": "Estate",  # The name that will appear in the App list
    "version": "16.0",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'menues/estate_property_menu.xml',
        'views/estate_property_tree_views.xml',
    ],
    "installable": True,
    'license': 'LGPL-3',
}
