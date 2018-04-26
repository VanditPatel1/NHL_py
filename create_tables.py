
player_meta = \
"""
CREATE TABLE player_meta (
    ID INT NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    team VARCHAR(40),
    number INT,
    position VARCHAR(20),
    PRIMARY KEY (ID)
)
"""

shot_table = \
"""
CREATE TABLE shots (
    ID INT NOT NULL,
    PLAYER_ID INT NOT NULL,
    x_coord INT,
    y_coord INT,
    game VARCHAR(30),
    date DATETIME
    period INT,
    time VARCHAR(20),
    goalie VARCHAR(50),
    type VARCHAR(30),
    goal BOOLEAN,
    strength VARCHAR(20),
    assist_1 VARCHAR(50),
    assist_2 VARCHAR(50),
    game_winning BOOLEAN,
    empty_net BOOLEAN
)
"""
