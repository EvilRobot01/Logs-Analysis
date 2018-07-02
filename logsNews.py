# coding: utf-8
# !/usr/bin/env python3

import psycopg2

query_1 = """select title,count(*) as popularity from articles,
        log where log.path = '/article/' || articles.slug group by
        articles.title,articles.author order by popularity desc limit 3;"""

query_2 = """select  authors.name, author,count(*) as popularity from articles,
        log,authors where log.path = '/article/' || articles.slug and
        authors.id = articles.author group by
        authors.name,articles.author order by popularity desc;"""

query_3 = "select * from error_table where con_error > 1"

query_1_return = dict()
query_2_return = dict()
query_3_return = dict()


def fetch_query(query):
    """Connect  to the database and extract the information requested"""
    try:
        db = psycopg2.connect("dbname=news")
    except:
        print "database was not located"
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

query_1_return['results'] = fetch_query(query_1)
query_2_return['results'] = fetch_query(query_2)
query_3_return['results'] = fetch_query(query_3)


def print_top_articles():
    """ask to extract the answer to  top articles"""
    print "\n1) What are the most popular three articles of all time?"
    print_format_articles(query_1_return)


def print_top_authors():
    """ask to extract the answer to top author"""
    print "\n2) Who are the most popular article authors of all time?"
    print_format_authors(query_2_return)


def print_top_error_days():
    """ask to extract the answer to number of errors"""
    print "\n3) On which days did more than 1% of requests lead to errors?"
    print_format_error(query_3_return)


def print_format_articles(data_in):
    print " ---------------------------------------------------------------"
    for row in data_in['results']:
        print ('\t' + str(row[0]) + ' |====> ' + str(row[1]) + ' views')


def print_format_authors(data_in):
    print " ---------------------------------------------------------------"
    for row in data_in['results']:
        print ('\t' + str(row[0]) + ' |====> ' + str(row[2]) + ' views')


def print_format_error(data_in):
    print " ---------------------------------------------------------------"
    for row in data_in['results']:
        print ('\t' + str(row[0]) + ' |====> ' + str(row[1]) + '% errors')

if __name__ == '__main__':
    """print out the answers """
    print_top_articles()
    print_top_authors()
    print_top_error_days()
