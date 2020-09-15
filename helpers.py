from werkzeug.exceptions import BadRequest

all_players = [
{'id': 1, 'name': 'Reece James', 'team':'Chelsea'},
{'id': 2, 'name': 'Mateo Kovacic', 'team': 'Chelsea'},
{'id': 3, 'name': 'Timo Werner', 'team': 'Chelsea'}
]

def index(req):
    return [p for p in all_players], 200

def show(req, uid):
    return find_by_uid(uid), 200

def create(req):
    new_player = req.get_json()
    new_player['id'] = sorted([c['id'] for c in all_players])[-1] + 1
    all_players.append(new_player)
    return new_player, 201

def destroy(req, uid):
    player = find_by_uid(uid)
    all_players.remove(player)
    return player, 204

def update(req, uid):
    player = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        player[key] = val
    return player, 200

def find_by_uid(uid):
    try:
        return next(player for player in all_players if player['id'] == uid)
    except:
        raise BadRequest(f"We don't have that player with id {uid}!")
