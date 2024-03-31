- Drops existing tables to avoid conflicts during schema initialization. 
DROP TABLE IF EXISTS feedback;
DROP TABLE IF EXISTS sentiment_analysis;
DROP TABLE IF EXISTS keywords;
DROP TABLE IF EXISTS summaries;

-- Creates a new table for student feedback.
CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feedback_text TEXT NOT NULL,
);

-- Creates a new table for sentiment analysis results.
CREATE TABLE sentiment_analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feedback_id INTEGER NOT NULL,
    sentiment_score REAL,
    sentiment_category TEXT,
    FOREIGN KEY (feedback_id) REFERENCES feedback(id)
);

-- Creates a new table for storing keywords extracted from feedback.
CREATE TABLE keywords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feedback_id INTEGER NOT NULL,
    keyword TEXT NOT NULL,
    importance_score REAL,
    FOREIGN KEY (feedback_id) REFERENCES feedback(id)
);

-- Creates a new table for feedback summaries.
CREATE TABLE summaries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feedback_id INTEGER NOT NULL,
    summary_text TEXT NOT NULL,
    FOREIGN KEY (feedback_id) REFERENCES feedback(id)
);