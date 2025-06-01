import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

# Basic skill list (expandable)
SKILL_KEYWORDS = {
    "python", "java", "c++", "c", "sql", "excel", "powerpoint", "html", "css", "javascript",
    "machine learning", "deep learning", "nlp", "tensorflow", "pytorch", "scikit-learn",
    "data analysis", "data visualization", "communication", "leadership", "teamwork",
    "problem solving", "public speaking", "project management", "cloud computing",
    "aws", "azure", "google cloud", "git", "github"
}

def extract_skills(text):
    doc = nlp(text.lower())
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    found_skills = set()

    for skill in SKILL_KEYWORDS:
        if skill in text.lower():
            found_skills.add(skill)
    return found_skills
