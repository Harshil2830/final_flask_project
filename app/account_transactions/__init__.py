import csv
import logging
import os

from flask import Blueprint, render_template, abort, url_for, current_app
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound

from app.db import db
from app.db.models import Transaction, User
from app.account_transactions.forms import csv_upload
from werkzeug.utils import secure_filename, redirect

account_transactions = Blueprint('account_transactions', __name__,
                                 template_folder='templates')


@account_transactions.route('/account_transactions', methods=['GET'], defaults={"page": 1})
@account_transactions.route('/account_transactions/<int:page>', methods=['GET'])
def account_transactions_browse(page):
    page = page
    per_page = 1000
    pagination = Transaction.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('browse_transactions.html', data=data, pagination=pagination)
    except TemplateNotFound:
        abort(404)


@account_transactions.route('/account_transactions/upload', methods=['POST', 'GET'])
@login_required
def account_transactions_upload():
    form = csv_upload()
    if form.validate_on_submit():
        log = logging.getLogger("uploads")

        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        list_account_transactions = []
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list_account_transactions.append(Transaction(row['\ufeffAMOUNT'], row['TYPE']))
                current_user.balance += float(row['\ufeffAMOUNT'])

        current_user.transactions = list_account_transactions
        db.session.commit()
        log.info(filename + " was just uploaded.")
        return redirect(url_for('account_transactions.account_transactions_browse'))

    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)
