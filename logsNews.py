# coding: utf-8

import psycopg2

def fetch_query(query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    print results

def print_top_articles():
    print "\nWhat are the most popular three articles of all time?" 
    fetch_query("""select title,author,count(*) as popularity from articles,
        log where log.path like concat('%',articles.slug)  group by 
        articles.title,articles.author order by popularity desc limit 3;""")

def print_top_authors():
     print "\nWho are the most popular article authors of all time?"
     fetch_query("""select  authors.name, author,count(*) as popularity from articles,
        log,authors where log.path like concat('%',articles.slug) group by 
        authors.name,articles.author order by popularity desc;""")

def print_top_error_days():
      print "\nOn which days did more than 1% of requests lead to errors?"
      fetch_query("select * from error_table where con_error > 1")

if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_top_error_days()
