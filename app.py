from flask import Flask, json, jsonify, request, redirect
from flask_cors import CORS
from dotenv import load_dotenv
import psycopg2
import os

load_dotenv("sensitive.env")

HOST = os.getenv('HOST')
DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
PORT = os.getenv('PORT')

app = Flask(__name__)

CORS(app)

try:
    con = psycopg2.connect(
            dbname=DATABASE, 
            user=DATABASE_USERNAME, 
            password=DATABASE_PASSWORD, 
            host=HOST, 
            port=PORT)

    cur = con.cursor()

    # @app.route('/')
    # def fetch_all_players():
    #     cur.execute('SELECT player_name FROM player')
    #     rows = cur.fetchall()
    #     print(rows)

    #     return jsonify(rows)




    # @app.route('/')
    # def fetch_pluribus_hole_cards():
    #     cur.execute('''
    #         select lookup.hole_cards from cash_hand_player_statistics as hand
	#             join lookup_hole_cards as lookup
	# 	        on lookup.id_holecard = hand.id_holecard
    #             where id_player = 6 and lookup.id_gametype = 1;
    #     ''')
    #     rows = cur.fetchall()

    #     return jsonify(rows)

    @app.route('/api/hands')
    def fetch_all_hands():
        cur.execute('''
        select hand.id_hand, lookup_h1.card h1, lookup_h2.card h2, lookup_c1.card c1,  lookup_c2.card c2,  lookup_c3.card c3,  lookup_c4.card c4,  lookup_c5.card c5 from cash_hand_player_statistics as hand
                join lookup_cards as lookup_h1
					on holecard_1 = lookup_h1.id_card
				join lookup_cards as lookup_h2
					on holecard_2 = lookup_h2.id_card
                join cash_hand_summary as summary
                    on hand.id_hand = summary.id_hand
                left join lookup_cards as lookup_c1
                    on card_1 = lookup_c1.id_card
                left join lookup_cards as lookup_c2
                    on card_2 = lookup_c2.id_card
                left join lookup_cards as lookup_c3
                    on card_3 = lookup_c3.id_card
                left join lookup_cards as lookup_c4
                    on card_4 = lookup_c4.id_card
                left join lookup_cards as lookup_c5
                    on card_5 = lookup_c5.id_card
            where id_player = 6;
        ''')
        rows = cur.fetchall()

        return jsonify(rows)


    @app.route('/hole_cards')
    def fetch_hole_cards():
        cur.execute('SELECT hole_cards from lookup_hole_cards')
        rows = cur.fetchall()

        return jsonify(rows)

    
except:
    @app.route('/')
    def error():
        return "ERROR"


    