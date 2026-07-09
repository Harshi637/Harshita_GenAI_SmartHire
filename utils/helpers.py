def build_search_query(profile):

    domain = profile.get("career_domain", "")
    current_role = profile.get("current_role", "")
    target_role = profile.get("target_role", "")
    experience = profile.get("experience_level", "")

    skills = ", ".join(profile.get("skills", []))

    education = profile.get("education", [])

    if isinstance(education, list):

        education_text = ", ".join(
            str(item) for item in education
        )

    else:

        education_text = str(education)

    query = f"""
Career Domain:
{domain}

Current Role:
{current_role}

Target Role:
{target_role}

Experience Level:
{experience}

Education:
{education_text}

Skills:
{skills}
"""

    return query.strip()