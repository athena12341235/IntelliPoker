from flask import Flask, request, jsonify
from pypokerengine.api.game import setup_config, start_poker
from poker.backend.game.fish_player_setup import FishPlayer
from poker.backend.game.test_player import ConsolePlayer

app = Flask(__name__)

def create_game_config():
    config = setup_config(max_round=10, initial_stack=1000, small_blind_amount=50)
    config.register_player(name="AI_Player", algorithm=FishPlayer())
    config.register_player(name="Human_Player", algorithm=ConsolePlayer())  # This can be changed to another AI for testing
    return config

@app.route('/game', methods=['POST'])
def start_game():
    game_config = create_game_config()
    game_result = start_poker(game_config, verbose=1)
    return jsonify(game_result)


