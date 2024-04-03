DROP TABLE IF EXISTS feedback;
DROP TABLE IF EXISTS analysis;

CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE analysis (
    feedback_id INTEGER PRIMARY KEY,
    sentiment TEXT,
    keywords TEXT,
    summary TEXT,
    recommended_actions TEXT 
);