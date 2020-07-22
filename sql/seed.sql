/* ========================================
 CREATE VALUE TABLE
========================================== */
CREATE TABLE IF NOT EXISTS value
(
    id      INTEGER not null
        primary key,
    content VARCHAR
);

CREATE INDEX IF NOT EXISTS ix_value_content
    on value (content);

CREATE INDEX IF NOT EXISTS ix_value_id
    on value (id);

/* ========================================
 CREATE PRINCIPLE TABLE
========================================== */

CREATE TABLE IF NOT EXISTS principle
(
    id      INTEGER not null
        primary key,
    content VARCHAR
);

CREATE INDEX IF NOT EXISTS ix_principle_content
    on principle (content);

CREATE INDEX IF NOT EXISTS ix_principle_id
    on principle (id);

/* ========================================
 SEEDING PRINCIPLE
========================================== */
INSERT INTO principle (content)
    VALUES
        ("Customer satisfaction by early and continuous delivery of valuable software"),
        ("Welcome changing requirements, even in late development"),
        ("Deliver working software frequently (weeks rather than months)"),
        ("Close, daily cooperation between business people and developers"),
        ("Projects are built around motivated individuals, who should be trusted"),
        ("Face-to-face conversation is the best form of communication (co-location)"),
        ("Working software is the primary measure of progress"),
        ("Sustainable development, able to maintain a constant pace"),
        ("Continuous attention to technical excellence and good design"),
        ("Simplicity—the art of maximizing the amount of work not done—is essential"),
        ("Best architectures, requirements, and designs emerge from self-organizing teams"),
        ("Regularly, the team reflects on how to become more effective, and adjusts accordingly");

/* ========================================
 SEEDING VALUES
========================================== */
INSERT INTO value (content)
    VALUES
        ("Individuals and interactions over processes and tools"),
        ("Working software over comprehensive documentation"),
        ("Customer collaboration over contract negotiation"),
        ("Responding to change over following a plan");