from flask import Flask, render_template, request

from location_place import Place
from parser_question import Parser
from recherche_pageids_wiki import Wikipedia
# from recherche_texteintro_wiki import

app = Flask(__name__)

@app.route('/')
def chat_bot():
    """ Display Chatbot page """
    return render_template('GrandPy_Bot.html')

@app.route('/parser/question')
def parse_to_execute():
    """
        Parse the question asked 
        As input  : the question 'ask' as string
        In return : the parsed question 'ask_parse' as json
        (the variable 'ask_parse' is a string )
    """
    # retrieving of question 'ask' from url received
    ask = request.args.get('ask')
    # parsing of the question
    parse_list = Parser.parsing(ask)
    ask_parse = ' '.join(parse_list)
    # json formatting
    return {"ask_parse": ask_parse}

@app.route('/place')
def place_to_find():
    """ 
        Locate a spot from the parsed elements of a question 'ask'
        As input  : the parsed question 'ask' as string
        In return : name, address and coordinates of the spot as json
    """
    # retrieving of question 'ask' from url received
    ask = request.args.get('ask')
    # call to the Google Place API to locate the spot
    (spot_name, spot_address, spot_latt, spot_long) = Place.location(ask)
    # json formatting
    return {"name": spot_name, "address": spot_address, "latt":spot_latt, "long": spot_long}

@app.route('/wiki')
def wiki():
    """
        Get the wikipedia's story of the spot
        As input  : the name of the spot to discover
        In return : the wikipedia's summary of the spot
    """
    # retrieving of the 'spot_name' from url received
    spot_name = request.args.get('spot_name')
    # retrieving the wikipedia identifier of the spot
    # needed to obtain the wiki's story of the place 
    (title, pageid) = Wikipedia.page_id(spot_name)
    # call to the Wiki Media API for the spot's story
    story = Wikipedia.intro(pageid)
    data = {"title": title, "intro": story}
    return data


if __name__ == '__main__':
    app.run(debug=True, port='5000')
