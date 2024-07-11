from flask import Flask, render_template, request, jsonify
from pypokerengine.api.game import setup_config, start_poker
from app.backend.game.fish_player_setup import FishPlayer
from app.backend.game.test_player import ConsolePlayer
import openai

app = Flask(__name__)

def create_game_config():
    config = setup_config(max_round=10, initial_stack=100, small_blind_amount=5)
    config.register_player(name="fish_player", algorithm=FishPlayer())
    config.register_player(name="human_player", algorithm=ConsolePlayer())
    return config

@app.route('/tutorials', methods=['POST'])
def start_game():
    game_config = create_game_config()
    game_result = start_poker(game_config, verbose=1)
    return jsonify(game_result)

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.get_json()
    
    game_state = data.get('game_state')
    user_action = data.get('user_action')
    
    prompt = f"Game State: {game_state}\nUser Action: {user_action}\nProvide recommendations for next steps and why"
        
    response = openai.ChatCompletion.create(
        model="gpt-4o", messages=[{"role": "user", "content": prompt}]
    )

    recommendation = response.choices[0].text.strip()
     
    return render_template(
        "recommendations.html",
        recommendation=recommendation,
    )

if __name__ == '__main__':
    app.run(debug=True)


