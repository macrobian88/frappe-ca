import frappe

def has_app_permission(doc, user):
    # Example: Allow only users with the "Manager" role
    if "Manager" in frappe.get_roles(user):
        return True
    return False
