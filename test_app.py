from ai_matcher import match_volunteer_to_opportunities

def test_ai_matcher_returns_list():
    volunteer = {
        "skills": "teaching coding",
        "location": "Mumbai",
        "availability": "weekends"
    }
    opportunities = [
        {
            "id": 1,
            "title": "Code Teacher",
            "ngo_name": "EduHelp",
            "required_skills": "coding teaching",
            "location": "Mumbai",
            "schedule": "weekends",
            "description": "Teach coding to kids"
        }
    ]
    results = match_volunteer_to_opportunities(volunteer, opportunities)
    assert isinstance(results, list)
    assert results[0]['match_score'] > 0

def test_ai_matcher_empty_opportunities():
    volunteer = {"skills": "teaching", "location": "Delhi", "availability": "weekdays"}
    results = match_volunteer_to_opportunities(volunteer, [])
    assert results == []