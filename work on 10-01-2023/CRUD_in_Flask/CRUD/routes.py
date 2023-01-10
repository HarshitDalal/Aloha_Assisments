from . import app
from flask import render_template, url_for, redirect, flash
from .forms import ERPForm
from .dbConfig.operations import ERPTable
from datetime import datetime


@app.route('/erp', methods=['GET', 'POST'])
def erp():
    emp = ERPTable()
    data = emp.select_all()
    form = ERPForm()
    if form.validate_on_submit():
        dob = datetime.strptime(str(form.dob.data), '%Y-%m-%d')
        emp.insert_data(form.fullname.data, form.email.data, form.phone.data, form.pos.data, form.address.data,
                        dob, form.company.data)
        emp.save()
        flash('Employee detail save successfully.', 'success')
        return redirect(url_for('erp'))
    return render_template('erp.html', form=form, data=data)


@app.route('/emp-detail/<int:eid>', methods=['GET', 'POST'])
def emp_detail(eid):
    emp = ERPTable()
    data = emp.select_by_id(eid)
    form = ERPForm()
    if form.validate_on_submit():
        dob = datetime.strptime(str(form.dob.data), '%Y-%m-%d')
        emp.update_data(eid, form.fullname.data, form.email.data, form.phone.data, form.pos.data, form.address.data,
                        dob, form.company.data)
        emp.save()
        flash('Employee detail save successfully.', 'success')
        return redirect(url_for('emp_detail', eid=eid))
    return render_template('emp_detail.html', data=data, form=form)
