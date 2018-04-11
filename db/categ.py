""" Count subcategore in DB"""
from sqlalchemy import create_engine

ENGINE = create_engine('mysql://sql11229446:3bMtQsxd8c@sql11.freemysqlhosting.net/sql11229446')
for row in ENGINE.execute('SELECT COUNT(parent_id) FROM `oc_category` WHERE `parent_id`=20'):
    desctops = dict(row)
    quantity_desktops = (desctops['COUNT(parent_id)'])
for row in ENGINE.execute('SELECT COUNT(parent_id) FROM `oc_category` WHERE `parent_id`=18'):
    laptops = dict(row)
    quantity_laptops = (laptops['COUNT(parent_id)'])
for row in ENGINE.execute('SELECT COUNT(parent_id) FROM `oc_category` WHERE `parent_id`=25'):
    components = dict(row)
    quantity_components = (components['COUNT(parent_id)'])
