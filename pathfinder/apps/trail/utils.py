import json
from .models import Spark

def construct_json(author_id):
    sparks = Spark.objects.filter(author=author_id)
    json_file = {}
    json_file['events'] = populate_events(sparks)
    return json.dumps(json_file)

def populate_events(sparks):
    events = []
    for spark in sparks:
        dict = {}
        if spark.url is not None:
            dict['media'] = format_media(spark.url)
        if spark.start_date is not None:
            dict['start_date'] = format_date(spark.start_date)
        if spark.end_date is not None:
            dict['end_date'] = format_date(spark.end_date)
        if spark.description is not None:
            dict['text'] = format_text(spark.name, spark.description)
        events.append(dict)
    return events

def format_media(url):
    dict = {}
    dict['url'] = url
    return dict

def format_date(date):
    dict = {}
    dict['month'] = date.month
    dict['day'] = date.day
    dict['year'] = date.year
    return dict

def format_text(name, description):
    dict = {}
    dict['headline'] = name
    dict['text'] = description
    return dict
