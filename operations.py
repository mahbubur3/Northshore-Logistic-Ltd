import sqlite3

def connect():
    return sqlite3.connect("northshore.db")

def add_customer(name, phone, email, address):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO Customers (name, phone, email, address)
    VALUES (?, ?, ?, ?)
    """, (name, phone, email, address))

    conn.commit()
    conn.close()


def add_shipment(order_number, id_sender, id_receiver, item_description, status, cost, payment_status):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO Shipments 
    (order_number, id_sender, id_receiver, item_description, status, cost, payment_status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (order_number, id_sender, id_receiver, item_description, status, cost, payment_status))

    conn.commit()
    conn.close()


def assign_driver(id_shipment, id_driver, id_vehicle, route_details):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO Assignments (id_shipment, id_driver, id_vehicle, route_details)
    VALUES (?, ?, ?, ?)
    """, (id_shipment, id_driver, id_vehicle, route_details))

    conn.commit()
    conn.close()


def view_shipments():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Shipments")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


def update_shipment_status(id_shipment, new_status):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE Shipments
    SET status = ?
    WHERE shipment_id = ?
    """, (new_status, id_shipment))

    conn.commit()
    conn.close()


def add_incident(id_shipment, description, date_reported, status):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO Incidents (id_shipment, description, date_reported, status)
    VALUES (?, ?, ?, ?)
    """, (id_shipment, description, date_reported, status))

    conn.commit()
    conn.close()


