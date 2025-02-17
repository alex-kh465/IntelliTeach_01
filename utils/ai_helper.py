from groq import Groq
import json
import streamlit as st

API_KEY = st.secrets["api_keys"]["API_KEY"]
client = Groq(api_key=API_KEY)

def generate_lesson_plan(subject, topic, subtopics, lesson_type):
    if "uploaded_content" in st.session_state and st.session_state["uploaded_content"]:
        content = st.session_state["uploaded_content"]
        prompt = f"""
        Create a structured lesson plan for the subject based on the content: {content}.
        Subtopics include: {subtopics}.
        The lesson should follow a {lesson_type} approach.
        The plan should include:
        - Learning objectives
        - Key concepts
        - Activities or exercises
        - Summary and review points
        """
    else:
        prompt = f"""
        Create a structured lesson plan for the subject "{subject}" on the topic "{topic}".
        Subtopics include: {subtopics}.
        The lesson should follow a {lesson_type} approach.
        The plan should include:
        - Learning objectives
        - Key concepts
        - Activities or exercises
        - Summary and review points
        """

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are an expert lesson planner."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=2048,
    )

    return completion.choices[0].message.content.strip()

def generate_questions(subject, topic, num_questions, difficulty, question_types):
     # Check if uploaded document content exists
    if "uploaded_content" in st.session_state and st.session_state["uploaded_content"]:
        content = st.session_state["uploaded_content"]
        prompt = f"""
        Generate {num_questions} questions based on the "{content}".
        The difficulty level is {difficulty}.
        Include the following question types: {", ".join(question_types)}.
        Each question should be clear and well-structured.
        """

    else:
        prompt = f"""
        Generate {num_questions} questions for the subject "{subject}" on the topic "{topic}".
        The difficulty level is {difficulty}.
        Include the following question types: {", ".join(question_types)}.
        Each question should be clear and well-structured.
        """

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a question generation AI."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=2048,
    )

    return completion.choices[0].message.content.strip()


def generate_rubrics(subject, topic, difficulty, criteria):
    if "uploaded_content" in st.session_state and st.session_state["uploaded_content"]:
        content = st.session_state["uploaded_content"]
        prompt = f"""
            Generate a grading rubric for the content:"{content}".
            The difficulty level is {difficulty}.
            The assessment criteria include: {criteria}.
            Format the rubric as a table with grading levels (Excellent, Good, Satisfactory, Needs Improvement).
            """
    
    else:
        prompt = f"""
        Generate a grading rubric for the subject "{subject}" on the topic "{topic}".
        The difficulty level is {difficulty}.
        The assessment criteria include: {criteria}.
        Format the rubric as a table with grading levels (Excellent, Good, Satisfactory, Needs Improvement).
        """

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a rubric generation AI."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=2048,
    )

    return completion.choices[0].message.content.strip()

def generate_presentation(subject, topic, num_slides, additional_notes):
    if "uploaded_content" in st.session_state and st.session_state["uploaded_content"]:
        content = st.session_state["uploaded_content"]
        prompt = f"""
        Generate a well-structured PowerPoint presentation with {num_slides} slides.
        
        **Content:** {content}
        
        Each slide should include:
        - A short, meaningful title.
        - 3-5 bullet points summarizing key content but don't include the dot itself.
        - The slides should follow a logical structure.

        Use Addtional Notes:
        {additional_notes}

        Return the response **only as a valid JSON array**, formatted as:
        [
            {{"title": "Slide Title 1", "points": ["Point 1", "Point 2", "Point 3"]}},
            {{"title": "Slide Title 2", "points": ["Point 1", "Point 2"]}}
        ]
        """
    else:
        prompt = f"""
        Generate a well-structured PowerPoint presentation with {num_slides} slides.
        
        **Topic:** {topic}
        **Subject:** {subject}
        
        Each slide should include:
        - A short, meaningful title.
        - 3-5 bullet points summarizing key content but don't include the dot itself.
        - The slides should follow a logical structure.

        Use Addtional Notes:
        {additional_notes}

        Return the response **only as a valid JSON array**, formatted as:
        [
            {{"title": "Slide Title 1", "points": ["Point 1", "Point 2", "Point 3"]}},
            {{"title": "Slide Title 2", "points": ["Point 1", "Point 2"]}}
        ]
        """
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are an AI presentation assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2048,
            top_p=1
        )

        # Extract raw response
        raw_text = response.choices[0].message.content.strip()

        # Try extracting JSON safely
        json_start = raw_text.find("[")
        json_end = raw_text.rfind("]") + 1
        json_text = raw_text[json_start:json_end]

        slides_data = json.loads(json_text)  # Convert to list of dicts

        if not isinstance(slides_data, list):  # Validate structure
            raise ValueError("Generated content is not in list format.")

        return slides_data  # Return properly formatted slides

    except (json.JSONDecodeError, ValueError, IndexError) as e:
        st.error(f"⚠️ Error generating slides: {e}")
        return []

def generate_questions_paper(subject, num_questions, topics, difficulty_distribution):
    if "uploaded_content" in st.session_state and st.session_state["uploaded_content"]:
        content = st.session_state["uploaded_content"]
        prompt = f"Generate a structured question paper for the content '{content}' with {num_questions} questions.\n\n"
    else:
        prompt = f"Generate a structured question paper for the subject '{subject}' with {num_questions} questions.\n\n"
    for topic in topics:
        prompt += f"Topic: {topic['topic']}\n"
        for subtopic in topic['subtopics']:
            prompt += f" - Subtopic: {subtopic}\n"

    prompt += (
        "\nDistribute the questions based on Bloom's Taxonomy:\n"
        f"- Create: {difficulty_distribution['Create']}% of questions should require creative problem-solving.\n"
        f"- Analyze: {difficulty_distribution['Analyze']}% should require analysis and critical thinking.\n"
        f"- Apply: {difficulty_distribution['Apply']}% should require application of knowledge.\n"
        f"- Understand: {difficulty_distribution['Understand']}% should assess basic understanding.\n"
        f"- Remember: {difficulty_distribution['Remember']}% should assess basic remembering.\n"
        f"- Evaluate: {difficulty_distribution['Evaluation']}% should assess basic evaluation.\n"
    )

    prompt += "\nEnsure the question paper has proper formatting and varied question types."

    try:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are an AI that generates structured question papers."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=4096,
            top_p=1,
        )

        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"
