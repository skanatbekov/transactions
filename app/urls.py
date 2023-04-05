from . import app, db
from . import views


app.add_url_rule('/admin/transaction/create', view_func=views.admin_transaction_create, methods=['POST', 'GET'])

app.add_url_rule('/transaction/list', view_func=views.transactions_list)

app.add_url_rule('/admin/transaction/<int:transaction_id>/update', view_func=views.admin_transaction_update, methods=['POST', 'GET'])

app.add_url_rule('/admin/transaction/<int:transaction_id>/delete', view_func=views.admin_transaction_delete, methods=['POST', 'GET'])


app.add_url_rule('/register', view_func=views.user_register, methods=['POST', 'GET'])
app.add_url_rule('/login', view_func=views.user_login, methods=['POST', 'GET'])
app.add_url_rule('/logout', view_func=views.user_logout)
