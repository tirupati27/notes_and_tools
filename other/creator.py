sem1_structure = {
    "201 Programming in C and Python": {
        "Block-1 An Introduction to C": [
            "Unit-1 Basics of C",
            "Unit-2 Operators and Expressions",
            "Unit-3 Input/Output and Preprocessor",
            "Unit-4 Control Statements and Functions"
        ],
        "Block-2 Data Structures and Memory": [
            "Unit-1 Arrays and Strings",
            "Unit-2 Pointers and Dynamic Memory",
            "Unit-3 Structures and File Handling",
            "Unit-4 C and Python Comparison"
        ]
    },
    "208 Data Structures and Algorithms": {
        "Block-1 Data Structures Basics": [
            "Unit-1 Introduction to Data Structures",
            "Unit-2 Arrays and Linked Lists",
            "Unit-3 Stacks and Queues"
        ],
        "Block-2 Trees and Graphs": [
            "Unit-1 Trees and Binary Trees",
            "Unit-2 Binary Search Trees",
            "Unit-3 Graphs and Traversals"
        ],
        "Block-3 Sorting and Searching": [
            "Unit-1 Searching Algorithms",
            "Unit-2 Sorting Algorithms",
            "Unit-3 Hashing"
        ]
    },
    "211 Design and Analysis of Algorithms": {
        "Block-1 Introduction to Algorithms": [
            "Unit-1 Basics of an Algorithm and its properties",
            "Unit-2 Some pre‑requisites and Asymptotic Bounds",
            "Unit-3 Analysis of Simple Algorithm",
            "Unit-4 Solving Recurrences"
        ],
        "Block-2 Design Techniques‑I": [
            "Unit-1 Greedy Technique",
            "Unit-2 Divide & Conquer Technique",
            "Unit-3 Graph Algorithm‑I"
        ],
        "Block-3 Design Techniques‑II": [
            "Unit-1 Graph Algorithms‑II",
            "Unit-2 Dynamic Programming Technique",
            "Unit-3 String Matching Techniques"
        ],
        "Block-4 NP‑Completeness and Approximation Algorithm": [
            "Unit-1 NP‑Completeness",
            "Unit-2 NP‑Completeness and NP‑hard Problems",
            "Unit-3 Handling Intractability"
        ]
    },
    "212 Discrete Mathematics": {
        "Block-1 Elementary Logic and Proofs": [
            "Unit-1 Propositional Calculus and Truth Tables",
            "Unit-2 Predicates and Quantifiers",
            "Unit-3 Methods of Proof",
            "Unit-4 Normal Forms"
        ],
        "Block-2 Sets, Relations and Functions": [
            "Unit-1 Sets and Set Operations",
            "Unit-2 Relations: Properties and Types",
            "Unit-3 Functions: Types and Inverses",
            "Unit-4 Partial and Total Functions"
        ],
        "Block-3 Counting Principles": [
            "Unit-1 Basic Counting Techniques",
            "Unit-2 Permutations and Combinations",
            "Unit-3 Binomial Theorem",
            "Unit-4 Principle of Inclusion–Exclusion"
        ],
        "Block-4 Graph Theory": [
            "Unit-1 Definitions and Examples of Graphs",
            "Unit-2 Connectedness and Components",
            "Unit-3 Eulerian and Hamiltonian Graphs",
            "Unit-4 Trees and Traversals"
        ]
    },
    "213 Software Engineering": {
        "Block-1 An Overview of Software Engineering": [
            "Unit-1 Introduction to SE",
            "Unit-2 Software Processes and Life Cycle",
            "Unit-3 Software Project Management"
        ],
        "Block-2 Software Project Management": [
            "Unit-1 Project Planning",
            "Unit-2 Project Scheduling (PERT, CPM)",
            "Unit-3 Risk Management"
        ],
        "Block-3 Web, Mobile and CASE Tools": [
            "Unit-1 CASE Tools Overview",
            "Unit-2 Web Application and Mobile App Tools",
            "Unit-3 RAD and Prototyping Tools"
        ],
        "Block-4 Advanced Topics in Software Engineering": [
            "Unit-1 Software Metrics",
            "Unit-2 Software Quality and Standards",
            "Unit-3 Emerging Topics in SE"
        ]
    },
    "214 Professional Skills and Ethics": {
        "Block-1 Professional Skills Needed at the Workplace-I": [
            "Unit-1 The Process of Communication",
            "Unit-2 Team Building",
            "Unit-3 Motivation"
        ],
        "Block-2 Professional Skills Needed at the Workplace‑II": [
            "Unit-1 Interpersonal Skills and Presentation",
            "Unit-2 Leadership Skills",
            "Unit-3 Corporate Etiquette and Workplace Culture"
        ]
    },
    "215 Security and Cyber Laws": {
        "Block-1 Cyber Security Issues": [
            "Unit-1 Cyber Security Issues and Challenges",
            "Unit-2 Data Security and Management",
            "Unit-3 Cyber Threats, Attacks and Vulnerabilities"
        ],
        "Block-2 Cyber Laws": [
            "Unit-1 IT Act, Definitions and Scope",
            "Unit-2 Cyber Crimes and Penalties",
            "Unit-3 Cyber Ethics and Privacy"
        ]
    },
    "216 Internet Concepts and Web Design (Lab)": {
        "Lab-1 HTML and CSS": [
            "Unit-1 Introduction to HTML",
            "Unit-2 HTML Tags and Forms",
            "Unit-3 CSS Styling"
        ],
        "Lab-2 JavaScript and Hosting": [
            "Unit-1 Basics of JavaScript",
            "Unit-2 DOM Manipulation",
            "Unit-3 Hosting Web Pages"
        ]
    },
    "217 Software Engineering Lab": {
        "Lab-1 Project Documentation": [
            "Unit-1 Requirements Specification",
            "Unit-2 Use Case Diagrams",
            "Unit-3 Design and Testing"
        ],
        "Lab-2 Project Implementation": [
            "Unit-1 Implementation Techniques",
            "Unit-2 Project Demo and Review",
            "Unit-3 Final Submission"
        ]
    }
}

sem2_structure = {}
sem3_structure = {}
sem4_structure = {}

import subprocess
import os
parent_dir = "/mnt/c/Users/Tirupati Bala/MCA_CONTENT"
if os.path.isdir(parent_dir):
    parent_dir = "/mnt/c/Users/Tirupati Bala/MCA_CONTENT_2"
subprocess.run(f"mkdir '{parent_dir}'",shell=True, capture_output=True)

def create_directories(sem, sem_structure):
    sem_name= f"Semester {sem}"
    additional_folders = ["Assignment", "PYQ"]
    subprocess.run(f"mkdir '{parent_dir}/{sem_name}'",shell=True, capture_output=True)
    for ad_folder in additional_folders:
        subprocess.run(f"mkdir '{parent_dir}/{sem_name}/{ad_folder}'", shell=True, capture_output=True)
    if sem_structure:
        for course in sem_structure.keys():
            subprocess.run(f"mkdir '{parent_dir}/{sem_name}/{course}'",shell=True, capture_output=True)
            for block in sem_structure[course].keys():
                subprocess.run(f"mkdir '{parent_dir}/{sem_name}/{course}/{block}'",shell=True, capture_output=True)

create_directories(1, sem1_structure)
create_directories(2, sem2_structure)
create_directories(3, sem3_structure)
create_directories(4, sem4_structure)