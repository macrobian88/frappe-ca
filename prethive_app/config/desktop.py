from frappe import _
 
 
def get_data():
	return [
		{
			"module_name": "prethive_app",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Prethive"),
		}
	]
