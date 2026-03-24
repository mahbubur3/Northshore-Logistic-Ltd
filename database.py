import sqlite3

conn = sqlite3.connect('northshore.db')
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS Customers (#
    id_customer INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT UNIQUE,
    address TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS Shipments (
    id_shipment INTEGER PRIMARY KEY AUTO_INCREMENT,
    order_number TEXT NOT NULL,
    id_sender INTEGER,
    id_receiver INTEGER,
    item_description TEXT,
    status TEXT,
    delivery_date TEXT,
    cost REAL,
    payment_status TEXT,
    FOREIGN KEY(id_sender) REFERENCES Customers(id_customer)
    FOREIGN KEY(id_receiver) REFERENCES Customers(id_customer)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS Drivers (
    id_driver INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    license_number TEXT UNIQUE,
    phone TEXT,
    shift TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS Vehicles (
    id_vehicle INTEGER PRIMARY KEY AUTO_INCREMENT,
    type TEXT,
    capacity INTEGER,
    status TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS Warehouses (
    id_warehouse INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT,
    location TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS Inventory (
    id_inventory INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_warehouse INTEGER,
    item_name TEXT,
    quantity INTEGER,
    reorder_level INTEGER,
    FOREIGN KEY (id_warehouse) REFERENCES Warehouses(id_warehouse)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS Assignments (
    id_assignment INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_shipment INTEGER,
    id_driver INTEGER,
    id_vehicle INTEGER,
    route_details TEXT,
    FOREIGN KEY (id_shipment) REFERENCES Shipments(id_shipment),
    FOREIGN KEY (id_driver) REFERENCES Drivers(id_driver),
    FOREIGN KEY (id_vehicle) REFERENCES Vehicles(id_vehicle)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS Incidents (
    id_incident INTEGER PRIMARY KEY AUTOINCREMENT,
    id_shipment INTEGER,
    description TEXT,
    date_reported TEXT,
    status TEXT,
    FOREIGN KEY (id_shipment) REFERENCES Shipments(id_shipment)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id_user INTEGER PRIMARY KEY AUTO_INCREMENT,
    username TEXT UNIQUE,
    password_hash TEXT,
    role TEXT
)
""")

conn.commit()
conn.close()