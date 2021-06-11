import datetime
import random
import psycopg2 as psg
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text, create_engine
from datetime import date
from PyQt6.QtWidgets import QTableWidgetItem

engine = None
cursor = None
conn = None
db_name = None


def create_database():
    global engine
    global cursor
    global conn
    global db_name
    engine = create_engine(
        'postgresql://{}:{}@localhost/postgres'.format("BdLabUser", "qwerty"), echo=True)
    conn = engine.raw_connection()
    cursor = conn.cursor()
    db_name = "lab2db{}".format(random.randint(0, 10000000))
    print(db_name)
    cursor.execute("commit")
    cursor.execute("create database " + db_name)
    conn.close()
    engine = create_engine(
        'postgresql://{}:{}@localhost/{}'.format("BdLabUser", "qwerty", db_name), echo=True)
    conn = engine.raw_connection()
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(open("sqlfuncs.sql").read())


def drop_database():
    global engine
    global cursor
    global conn
    global db_name
    conn.close()
    engine = create_engine(
        'postgresql://{}:{}@localhost/postgres'.format("BdLabUser", "qwerty"), echo=True)
    conn = engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute("drop database {}".format(db_name))
    cursor.execute("commit")
    conn.close()


def clear_tables(p, n, r):
    if p:
        cursor.callproc('clear_people')
    if n:
        cursor.callproc('clear_numbers')
    if r:
        cursor.callproc('clear_reservations')


def add_man(name, surname, age, phone, email):
    cursor.callproc("add_to_people", [name, surname, int(age), phone, email])


def add_number(floor, num, sea, price):
    cursor.callproc('add_to_numbers', [int(floor), int(num), sea, int(price)])


def print_all_numbers(obj):
    cursor.callproc('get_numbers')
    data = cursor.fetchall()
    table = obj.tableWidget_3
    table.setColumnCount(5)
    table.setRowCount(len(data))
    table.setHorizontalHeaderLabels(
        ['Id', 'Floor', 'Number of beds', 'Sea_view', 'Price'])
    for i in range(len(data)):
        for j in range(len(data[i])):
            table.setItem(i, j, QTableWidgetItem(str(data[i][j])))


def print_all_people(obj):
    cursor.callproc('get_people')
    data = cursor.fetchall()
    table = obj.tableWidget_4
    table.setColumnCount(6)
    table.setRowCount(len(data))
    table.setHorizontalHeaderLabels(
        ['Id', 'FirstName', 'Lastname', 'Age', 'Phone Number', 'Email'])
    for i in range(len(data)):
        for j in range(len(data[i])):
            table.setItem(i, j, QTableWidgetItem(str(data[i][j])))


def print_all_reservations(obj):
    cursor.callproc('get_reservations')
    data = cursor.fetchall()
    table = obj.tableWidget_5
    table.setColumnCount(7)
    table.setRowCount(len(data))
    table.setHorizontalHeaderLabels(
        ['Id', 'Human id', 'Number id', 'Arriving date', 'Number of days', 'Price', 'Finish status'])
    for i in range(len(data)):
        for j in range(len(data[i])):
            table.setItem(i, j, QTableWidgetItem(str(data[i][j])))


def print_apr_numbers_for_all(obj):
    cursor.callproc('find_apr_numbers')
    data = cursor.fetchall()
    table = obj.tableWidget_2
    table.setColumnCount(5)
    table.setRowCount(len(data))
    table.setHorizontalHeaderLabels(
        ['Id', 'Floor', 'Number of beds', 'Sea_view', 'Price'])
    for i in range(len(data)):
        for j in range(len(data[i])):
            table.setItem(i, j, QTableWidgetItem(str(data[i][j])))


def add_reservation(human_id, number_id, datefrom, num_of_days):
    datefrom = datefrom[6:] + datefrom[3:5] + datefrom[:2]
    cursor.callproc('add_to_reservations', [
                    int(human_id), int(number_id), datefrom, int(num_of_days)])


def print_apr_numbers_for_current_human(obj, num_people, datefrom, num_days):
    datefrom = datefrom[6:] + datefrom[3:5] + datefrom[:2]
    cursor.callproc('find_apr_numbers_for_human', [
                    int(num_people), datefrom, int(num_days)])
    data = cursor.fetchall()
    table = obj.tableWidget
    table.setColumnCount(5)
    table.setRowCount(len(data))
    table.setHorizontalHeaderLabels(
        ['Id', 'Floor', 'Number of beds', 'Sea_view', 'Price'])
    for i in range(len(data)):
        for j in range(len(data[i])):
            table.setItem(i, j, QTableWidgetItem(str(data[i][j])))


def edit_reservations(id, human_id, number_id, datefrom, num_of_days):
    datefrom = datefrom[6:] + datefrom[3:5] + datefrom[:2]
    cursor.callproc('update_reservations', [id, int(
        human_id), int(number_id), datefrom, int(num_of_days)])


def edit_people(id, name, lastname, age, phone, email):
    cursor.callproc('update_people', [
                    id, name, lastname, int(age), phone, email])


def edit_numbers(id, floor, num, sea, price):
    cursor.callproc('update_number', [id, int(
        floor), int(num), sea, int(price)])


def delete_number(id):
    cursor.callproc('delete_number', [id])


def delete_reservation(id):
    cursor.callproc('delete_reservation', [id])


def delete_human(id):
    cursor.callproc('delete_human', [id])


def find_human_by_lastname(obj, lastname):
    cursor.callproc('find_people', [lastname])
    data = cursor.fetchall()
    table = obj.tableWidget_6
    table.setColumnCount(13)
    table.setRowCount(len(data))
    table.setHorizontalHeaderLabels(['Human Id', 'FirstName', 'Lastname', 'Age', 'Phone Number', 'Email',
                                     'Reservation Id', 'Human id', 'Number id', 'Arriving date', 'Number of days', 'Price', 'Finish status'])
    for i in range(len(data)):
        for j in range(len(data[i])):
            table.setItem(i, j, QTableWidgetItem(str(data[i][j])))


def delete_human_by_lastname(lastname):
    cursor.callproc('delete_people', [lastname])
