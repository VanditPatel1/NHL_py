
player_meta = \
"""
CREATE TABLE player_meta (
    ID INT NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    team VARCHAR(20),
    number INT,
    position VARCHAR(20),
    PRIMARY KEY (ID)
)
"""
