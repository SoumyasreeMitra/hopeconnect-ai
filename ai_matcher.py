import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_volunteer_to_opportunities(volunteer, opportunities):
    """
    AI-powered matching using TF-IDF vectorization and cosine similarity.
    Matches volunteer skills to opportunity required skills.
    """
    if not opportunities:
        return []

    # Build text profiles
    volunteer_profile = f"{volunteer['skills']} {volunteer['location']} {volunteer['availability']}"
    
    opportunity_profiles = [
        f"{opp['required_skills']} {opp['location']} {opp['schedule']}"
        for opp in opportunities
    ]

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    all_profiles = [volunteer_profile] + opportunity_profiles
    tfidf_matrix = vectorizer.fit_transform(all_profiles)

    # Cosine similarity between volunteer and each opportunity
    volunteer_vector = tfidf_matrix[0]
    opportunity_vectors = tfidf_matrix[1:]
    similarity_scores = cosine_similarity(volunteer_vector, opportunity_vectors)[0]

    # Rank opportunities by similarity score
    ranked = sorted(
        zip(opportunities, similarity_scores),
        key=lambda x: x[1],
        reverse=True
    )

    results = []
    for opp, score in ranked:
        results.append({
            **opp,
            "match_score": round(float(score) * 100, 2)
        })

    return results