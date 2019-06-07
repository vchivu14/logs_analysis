#!/usr/bin/env python

import psycopg2


# Connects us to our database, runs the query and returns the results
def run_query(query):
    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# Returns the first 3 most accessed articles
def get_top_articles():
    query = """
        SELECT articles.title, COUNT(*) AS num
        FROM articles
        JOIN log
        ON articles.slug = substring(log.path, 10)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3;
    """
    # Runs the query
    results = run_query(query)

    # Prints the results
    print('\nTOP 3 MOST ACCESSED ARTICLES ARE:')
    print(" ")
    item = 1
    for i in results:
        print(str(item) + ". " + i[0] + " has " + str(i[1]) + " views.")
        item += 1


# Returns the most popular article authors
def get_top_authors():
    query = """
        SELECT authors.name, COUNT(*) AS num
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON articles.slug = substring(log.path, 10)
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 3;
    """
    # Runs the query
    results = run_query(query)

    # Prints the results
    print('\nTOP 3 MOST POPULAR AUTHORS ARE:')
    print(" ")
    item = 1
    for i in results:
        print(str(item) + ". " + i[0] + " with " + str(i[1]) + " views.")
        item += 1


# Returns the days with requests leading to most errors
def get_most_errors():
    query = """
        SELECT errorlogs.date,
        round(100.0*errorcount/logcount, 2) AS percent
        FROM logs, errorlogs
        WHERE logs.date = errorlogs.date
        AND errorcount > logcount/100;
    """
    # Runs the query
    results = run_query(query)

    # Prints the results
    print('\nDAYS WHEN MORE THAN 1% OF REQUESTS LEAD TO ERRORS:')
    print(" ")
    for i in results:
        print("On " + str(i[0]) + " we got " + str(i[1]) + "%" + " errors.")
        print(" ")


print("Fetching results...\n")
get_top_articles()
get_top_authors()
get_most_errors()
