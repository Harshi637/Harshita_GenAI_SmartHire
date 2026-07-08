def build_search_query(profile):

    skills = profile.get("skills", [])

    education = profile.get("education", [])

    experience = profile.get("experience", [])

    # Convert dictionaries into strings
    experience = [str(x) for x in experience]

    education = [str(x) for x in education]

    skills = [str(x) for x in skills]

    query = f"""
Target Role:
{profile.get("target_role","")}

Skills:
{", ".join(skills)}

Experience:
{" ".join(experience)}

Education:
{" ".join(education)}
"""

    return query