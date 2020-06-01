from flask import render_template, redirect, url_for, request
from . import main
from ..models import Sources
from ..requests import get_articles, get_sources, topheadlines, everything, search_everything

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = "Home - News From Various News Sources"
    
    general_category = get_sources('general')
    business_category = get_sources('business')
    entertainment_category = get_sources('entertainment')
    sports_category = get_sources('sports')
    technology_category = get_sources('technology')
    science_category = get_sources('science')
    health_category = get_sources('health')

    return render_template('index.html', title = title, general = general_category, business = business_category, entertainment = entertainment_category, sports = sports_category,tech = technology_category, science = science_category, health = health_category) 
