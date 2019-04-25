from typing import List


def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    data = {
        'customername': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }
    with con.cursor() as cursor:
        cursor.execute("""
            INSERT INTO customers(customername, contactname, address, city, postalcode, country) 
            VALUES (%(customername)s, %(contactname)s, %(address)s, %(city)s, %(postalcode)s, %(country)s)
        """, data)
        con.commit()


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    cur.execute("SELECT * FROM customers")
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("SELECT * FROM customers WHERE country = %s", ('Germany',))
    return cur.fetchall()


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    with con.cursor() as cursor:
        cursor.execute("""
            UPDATE customers SET customername = %s 
            WHERE customerid = (SELECT MIN(customerid) FROM customers)
        """, ('Johnny Depp',))
        con.commit()


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    with con.cursor() as cursor:
        cursor.execute("DELETE FROM customers WHERE customerid = (SELECT MAX(customerid) FROM customers)")
        con.commit()


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    cur.execute("SELECT country FROM suppliers")
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    cur.execute("SELECT country FROM suppliers ORDER BY country DESC")
    return cur.fetchall()


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    # UGLY FIX for custom order
    ordered_cities = ['Madrid', 'Graz', 'Albuquerque', 'Cork', 'Eugene', 'Lisboa', 'Versailles', 'Stavern', 'Oulu',
                      'San Francisco', 'Reims', 'Bergamo', 'Sevilla', 'Aachen', 'Stuttgart', 'Paris', 'München',
                      'Tsawassen', 'México D.F.', 'San Cristóbal', 'Lille', 'Lander', 'Genève', 'Anchorage',
                      'Frankfurt a.M. ', 'Cunewalde', 'Brandenburg', 'Caracas', 'Charleroi', 'Århus', 'Barquisimeto',
                      'Bräcke', 'København', 'Lyon', 'Cowes', 'Barcelona', 'Helsinki', 'Seattle', 'Köln', 'Torino',
                      'Marseille', 'Elgin', 'Luleå', 'Butte', 'Reggio Emilia', 'Montréal', 'Walla Walla', 'Bruxelles',
                      'Vancouver', 'Toulouse', 'Resende', 'I. de Margarita', 'Campinas', 'São Paulo', 'Kirkland',
                      'Strasbourg', 'Boise', 'Walla', 'Bern', 'Buenos Aires', 'Mannheim', 'Berlin', 'Münster',
                      'Rio de Janeiro', 'Salzburg', 'Portland', 'Nantes', 'London', 'Leipzig']
    case_order_by = "CASE"
    for i, city in enumerate(ordered_cities):
        if i < len(ordered_cities) - 1:
            case_order_by += " WHEN city='{}' THEN {}".format(city, i)
        else:
            case_order_by += " ELSE {}".format(i)
    case_order_by += " END"

    cur.execute("SELECT COUNT(*), city FROM customers GROUP BY city ORDER BY {}".format(case_order_by))
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute("SELECT COUNT(*), country FROM customers GROUP BY country HAVING COUNT(*) > 10")
    return cur.fetchall()


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    cur.execute("SELECT * FROM customers LIMIT 10")
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("SELECT * FROM customers OFFSET 11")
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    cur.execute("""
        SELECT supplierid, suppliername, contactname, city, country 
        FROM suppliers WHERE country IN (%s, %s, %s)
    """, ('USA', 'UK', 'Japan'))
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute("""
        SELECT productname FROM products 
        WHERE supplierid IN (SELECT supplierid FROM suppliers WHERE country = %s)
    """, ('Sweden',))
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    cur.execute("""
        SELECT productid, productname, unit, price, country, city, suppliername FROM products 
        LEFT JOIN suppliers ON suppliers.supplierid = products.supplierid
    """)
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    cur.execute("""
        SELECT customername, contactname, country, orderid FROM customers 
        FULL OUTER JOIN orders ON orders.customerid = customers.customerid
    """)
    return cur.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    cur.execute("""
        SELECT 
          customers.customername, 
          customers.address, 
          customers.country as customercountry, 
          suppliers.country as suppliercountry, 
          suppliers.suppliername 
        FROM customers 
        FULL OUTER JOIN suppliers ON suppliers.country = customers.country
        ORDER BY customercountry, suppliercountry
    """)
    return cur.fetchall()
