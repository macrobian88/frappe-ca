app_name = "ramtestapp"
app_title = "Ramtestapp"
app_publisher = "ram"
app_description = "test description"
app_email = "ram@walue.biz"
app_license = "MIT"

# Apps
# ------------------
required_apps = []

# Each item in the list will be shown as an app on the apps page
add_to_apps_screen = [
    {
        "name": "ramtestapp",
        "logo": "/assets/ramtestapp/logo.png",
        "title": "Ramtestapp",
        "route": "/ramtestapp",
        "has_permission": "ramtestapp.api.permission.has_app_permission"
    }
]

# Includes in <head>
# ------------------

# Include js, css files in header of desk.html
app_include_css = "/assets/ramtestapp/css/ramtestapp.css"
app_include_js = "/assets/ramtestapp/js/ramtestapp.js"

# Include js, css files in header of web template
web_include_css = "/assets/ramtestapp/css/ramtestapp.css"
web_include_js = "/assets/ramtestapp/js/ramtestapp.js"

# Include custom scss in every website theme (without file extension ".scss")
website_theme_scss = "ramtestapp/public/scss/website"

# Include js, css files in header of web form
webform_include_js = {"doctype": "public/js/doctype.js"}
webform_include_css = {"doctype": "public/css/doctype.css"}

# Include js in page
page_js = {"page": "public/js/file.js"}

# Include js in doctype views
doctype_js = {"doctype": "public/js/doctype.js"}
doctype_list_js = {"doctype": "public/js/doctype_list.js"}
doctype_tree_js = {"doctype": "public/js/doctype_tree.js"}
doctype_calendar_js = {"doctype": "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# Include app icons in desk
app_include_icons = "ramtestapp/public/icons.svg"

# Home Pages
# ----------
# Application home page (will override Website Settings)
home_page = "login"

# Website user home page (by Role)
role_home_page = {
    "Role": "home_page"
}

# Generators
# ----------
# Automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------
# before_install = "ramtestapp.install.before_install"
# after_install = "ramtestapp.install.after_install"

# Uninstallation
# --------------
# before_uninstall = "ramtestapp.uninstall.before_uninstall"
# after_uninstall = "ramtestapp.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# notification_config = "ramtestapp.notifications.get_notification_config"

# Permissions
# -----------
# permission_query_conditions = {
#     "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
# has_permission = {
#     "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events
# doc_events = {
#     "*": {
#         "on_update": "method",
#         "on_cancel": "method",
#         "on_trash": "method"
#     }
# }

# Scheduled Tasks
# ---------------
# scheduler_events = {
#     "all": ["ramtestapp.tasks.all"],
#     "daily": ["ramtestapp.tasks.daily"],
#     "hourly": ["ramtestapp.tasks.hourly"],
#     "weekly": ["ramtestapp.tasks.weekly"],
#     "monthly": ["ramtestapp.tasks.monthly"],
# }

# Testing
# -------
# before_tests = "ramtestapp.install.before_tests"

# Overriding Methods
# ------------------
# override_whitelisted_methods = {
#     "frappe.desk.doctype.event.event.get_events": "ramtestapp.event.get_events"
# }
# override_doctype_dashboards = {
#     "Task": "ramtestapp.task.get_dashboard_data"
# }

# Ignore links to specified DocTypes when deleting documents
# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# --------------
# before_request = ["ramtestapp.utils.before_request"]
# after_request = ["ramtestapp.utils.after_request"]

# Job Events
# ----------
# before_job = ["ramtestapp.utils.before_job"]
# after_job = ["ramtestapp.utils.after_job"]

# User Data Protection
# --------------------
# user_data_fields = [
#     {
#         "doctype": "{doctype_1}",
#         "filter_by": "{filter_by}",
#         "redact_fields": ["{field_1}", "{field_2}"],
#         "partial": 1,
#     },
#     {
#         "doctype": "{doctype_2}",
#         "filter_by": "{filter_by}",
#         "partial": 1,
#     },
#     {
#         "doctype": "{doctype_3}",
#         "strict": False,
#     },
#     {
#         "doctype": "{doctype_4}"
#     }
# ]

# Authentication and authorization
# --------------------------------
# auth_hooks = ["ramtestapp.auth.validate"]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
#     "Logging DocType Name": 30  # days to retain logs
# }

