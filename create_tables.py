
player_meta = \
"""
CREATE TABLE player_meta (
    ID INT PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    team VARCHAR(40),
    number INT,
    position VARCHAR(20)
)
"""

shot_table = \
"""
CREATE TABLE shots (
    ID SERIAL PRIMARY KEY,
    player_id INT REFERENCES player_meta (ID),
    goalie_id INT,
    x_coord INT,
    y_coord INT,
    game VARCHAR(30),
    game_id INT,
    date TIMESTAMP,
    period INT,
    time VARCHAR(20),
    shot_type VARCHAR(30),
    goal BOOLEAN,
    strength VARCHAR(20),
    assist_1 VARCHAR(50),
    assist_2 VARCHAR(50),
    game_winning BOOLEAN,
    empty_net BOOLEAN
)
"""
