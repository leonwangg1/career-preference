from sqlite3 import connect

# Create a new SQLite database
db_path = "leacreer_db.sqlite"
conn = connect(db_path)
cursor = conn.cursor()

# Executing the SQL commands to create the schema and tables in SQLite

# Table Creation
cursor.execute('''
CREATE TABLE QUESTION_GROUP (
    GROUP_ID INTEGER NOT NULL PRIMARY KEY,
    TITLE TEXT NOT NULL,
    DESCRIPTION TEXT,
    DISPLAY_ORDER INTEGER NOT NULL DEFAULT 1,
    ACTIVE INTEGER NOT NULL DEFAULT 1
)''')

cursor.execute('''
CREATE TABLE QUESTION (
    QUESTION_ID INTEGER NOT NULL PRIMARY KEY,
    GROUP_ID INTEGER NOT NULL,
    FIELD_TYPE TEXT NOT NULL,
    FIELD_LABEL TEXT NOT NULL,
    PLACEHOLDER TEXT,
    POSSIBLE_VALUES TEXT,
    INPUT_LIMIT INTEGER NOT NULL DEFAULT 0,
    REQUIRED INTEGER NOT NULL DEFAULT 0,
    DISPLAY_SIZE INTEGER NOT NULL DEFAULT 1,
    DISPLAY_ORDER INTEGER NOT NULL DEFAULT 1,
    ACTIVE INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (GROUP_ID) REFERENCES QUESTION_GROUP(GROUP_ID) ON DELETE CASCADE
)''')

cursor.execute('''
CREATE TABLE SUBMISSION (
    SUBMISSION_ID TEXT NOT NULL PRIMARY KEY,
    CREATED_AT TEXT NOT NULL,
    IP_ADDRESS TEXT,
    COMPLETED_AT TEXT
)''')

cursor.execute('''
CREATE TABLE SUBMISSION_RESPONSE (
    SUBMISSION_ID TEXT NOT NULL,
    QUESTION_ID INTEGER NOT NULL,
    RESPONSE TEXT NOT NULL,
    PRIMARY KEY (SUBMISSION_ID, QUESTION_ID),
    FOREIGN KEY (SUBMISSION_ID) REFERENCES SUBMISSION(SUBMISSION_ID) ON DELETE CASCADE,
    FOREIGN KEY (QUESTION_ID) REFERENCES QUESTION(QUESTION_ID) ON DELETE RESTRICT
)''')

# Insertion of sample data
question_group_data = [
    (1, 'Personal Details', None, 1, 1),
    (2, 'Skills & Experience', 'Please select all the areas that apply to you', 2, 1),
    (3, 'Interests', 'Please select all areas that interest you', 3, 1),
    (4, 'Preferences', None, 4, 1),
    (5, 'Progression', 'Where do you see yourself in the future?', 5, 1),
]

question_data = [
     (6, 1, 'freetext', 'Name', 'e.g. John Doe', None, 100, 1, 1, 1, 1),
     (7, 1, 'freetext', 'PMKeyS', 'e.g. 8812388', None, 30, 1, 1, 2, 1),
     (8, 1, 'single_select', 'Current Employment Category', 'Select category', 'Engineering;Technical;Administration;Commercial;Logistics;Information Technology', 1, 1, 1, 3, 1),
     (9, 1, 'single_select', 'Current Substantive APS Level', 'Select level', 'APS4;APS5;APS6;EL1;EL2', 1, 1, 1, 4, 1),
     (10, 1, 'freetext', 'List all your relevant qualifications (1,500 character limit)', 'e.g. Secondary, Tertiary (Certificate I/II/III/IV, Diploma, Advanced Diploma/Associate Degree, Bachelor Degree, Bachelor Honours Degree/Graduate, Vocational Graduate Certificate, Graduate and Vocational Graduate Diploma, Masters Degree, Doctoral Degree)', None, 1500, 1, 5, 5, 1),
     (11, 1, 'freetext', 'List all your relevant training (1,500 character limit)', 'e.g. LSO1 course, MVT course, Systems Engineering Practitioner Course, Maintenance Engineering Practitioner Course, Reliability engineering Course, Requirements Engineering, EMEI Author.', None, 1500, 1, 5, 6, 1),
     (12, 2, 'multi_select', 'Identify experience with Capability Life Cycle phase', None, 'Strategy & Concepts;Risk Mitigation & Requirement Setting;Acquisition;In Service & Disposal', 0, 0, 4, 1, 1),
     (13, 2, 'multi_select', 'Select all relevant skills and experience', None, 'Tender;Specifications;Contract Negotiations;System Engineering Management Plan;User Elicitation Workshops;Test & Evaluation;Validation & Verification;RODUM Analysis;Maintenance Engineering;Supervisory Experience;Electrical / Mechanical Engineering Instructions;Chartered Status', 0, 1, 4, 2, 1),
     (14, 2, 'multi_select', 'Areas of expertise', None, 'Weapons;Safety / Human Factors;Electrical Systems;Communications;C4ISR;Soldier Ensemble;Survivability;CBRNE;Modelling;Testing;Simulation;Food Sciences;A Vehicles;B Vehicles;C & D Vehicles;Automotive', 0, 1, 4, 3, 1),
     (15, 2, 'freetext', 'Additional comments (1,500 character limit)', 'Describe anything else you think is relevant regarding your skills or experience.', None, 1500, 0, 5, 4, 1),
     (16, 3, 'multi_select', 'Areas of interest', None, 'Weapons;Safety / Human Factors;Electrical Systems;Communications;C4ISR;Soldier Ensemble;Survivability;CBRNE;Modelling;Testing;Simulation;Food Sciences;A Vehicles;B Vehicles;C & D Vehicles;Automotive', 0, 1, 4, 1, 1),
     (17, 3, 'multi_select', 'Communities of Practice', None, 'Vehicle & Mechanical Systems;Test & Evaluation;Survivability Systems;Systems Engineering & Systems Safety;C4ISR;Weapon Systems;Niche;', 0, 1, 4, 2, 1),
     (18, 4, 'multi_select', 'What skills and experience would you like to gain?', None, 'Tender;Specifications;Contract Negotiations;System Engineering Management Plan;User Elicitation Workshops;Test & Evaluation;Validation & Verification;RODUM Analysis;Maintenance Engineering;Supervisory Experience;Electrical / Mechanical Engineering Instructions;Chartered Status', 0, 1, 4, 1, 1),
     (19, 4, 'freetext', 'Other (1,500 character limit)', 'Describe any other career progression preferences, such as management/leadership, Chief Engineer, Project Engineer', None, 1500, 0, 5, 2, 1),
     (20, 5, 'multi_select', 'Roles', None, 'Chief Engineer;Principle Engineer;Senior Technical Manager;Technical Imaging;Specialist Engineer;Engineering Director;Senior Technical Manager;Senior Engineer;Senior Technical Advisor;ICT;Asset Manager;Business Operations Manager;Contract Manager', 0, 0, 4, 1, 1),
     (21, 5, 'multi_select', 'Are you interested in Promotion, ARP or Mobility at level?', None, 'Promotion;ARP;Mobility at level', 0, 0, 2, 2, 1),
     (22, 5, 'multi_select', 'Work Location', None, 'Victoria Barracks - Melbourne;Monegeetta;Laverton (PEC)', 0, 0, 2, 3, 1),
     (23, 5, 'freetext', 'Ideally, what is your next career move? (1,500 character limit)', 'e.g. Describe your next career move in an ideal world.', None, 1500, 0, 5, 4, 1)
]

cursor.executemany('INSERT INTO QUESTION_GROUP (GROUP_ID, TITLE, DESCRIPTION, DISPLAY_ORDER, ACTIVE) VALUES (?, ?, ?, ?, ?)', question_group_data)
cursor.executemany('INSERT INTO QUESTION (QUESTION_ID, GROUP_ID, FIELD_TYPE, FIELD_LABEL, PLACEHOLDER, POSSIBLE_VALUES, INPUT_LIMIT, REQUIRED, DISPLAY_SIZE, DISPLAY_ORDER, ACTIVE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', question_data)

# Committing changes and closing the connection
conn.commit()
conn.close()

# Return the path to the created SQLite database
db_path
