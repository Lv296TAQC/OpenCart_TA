"""
Counts the number of subcategories desktops in the database
"""
import pymysql

CONNECTION = pymysql.connect(host='sql11.freemysqlhosting.net',
                             user='sql11229446',
                             password='3bMtQsxd8c',
                             db='sql11229446',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    CURSOR = CONNECTION.cursor()
    SQL = "SELECT COUNT(parent_id) FROM `oc_category` WHERE `parent_id`=20"
    CURSOR.execute(SQL)
    for row in CURSOR:
        COUNT_CAT_DESKTOPS = (row['COUNT(parent_id)'])


finally:
    CONNECTION.close()
