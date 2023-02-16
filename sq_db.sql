CREATE TABLE IF NOT EXISTS mainmenu (
id integer PRIMARY KEY AUTOINCREMENT,
name text NOT NULL,
topic text NOT NULL,
article text NOT NULL
);
CREATE TABLE IF NOT EXISTS comments (
id integer PRIMARY KEY AUTOINCREMENT,
name_for_comment text NOT NULL,
text_for_comment text NOT NULL,
);