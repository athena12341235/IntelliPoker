from flask import Flask, request, jsonify
from pypokerengine.api.game import setup_config, start_poker
from app.backend.game.fish_player_setup import FishPlayer
from app.backend.game.test_player import ConsolePlayer

app = Flask(__name__)

def create_game_config():
    config = setup_config(max_round=10, initial_stack=1000, small_blind_amount=50)
    config.register_player(name="ai_player", algorithm=FishPlayer())
    config.register_player(name="human_player", algorithm=ConsolePlayer())  # This can be changed to another AI for testing
    return config

@app.route('/tutorials', methods=['POST'])
def start_game():
    game_config = create_game_config()
    game_result = start_poker(game_config, verbose=1)
    return jsonify(game_result)

if __name__ == '__main__':
    app.run(debug=True)


