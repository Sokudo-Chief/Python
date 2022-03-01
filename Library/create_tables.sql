CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    author TEXT NOT NULL,
    toms INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS visitors (
    number INTEGER PRIMARY KEY,
    vis_name TEXT NOT NULL,
    surname TEXT NOT NULL,
    adress TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY,
    book_id INTEGER NOT NULL,
    visitor_number INTEGER NOT NULL
);