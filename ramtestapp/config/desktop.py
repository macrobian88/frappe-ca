from frappe import _

def get_data():
    return [
        {
            "module_name": "RamTestApp",
            "color": "#FF5733",  # Custom color
            "icon": "/assets/ramtestapp/app-logo.png",  # Corrected logo path
            "type": "module",
            "label": _("RamTestApp"),
        }
    ]

