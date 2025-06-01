import streamlit as st
from scripts.extract_text import extract_text_from_resume
from scripts.skill_matcher import extract_skills

def main():
    st.set_page_config(page_title="ResMatch AI", page_icon="📄", layout="centered")
    st.title("📄 ResMatch AI - Resume Analyzer & Job Match Scorer")

    st.markdown("""
    Upload your resume (PDF/DOCX) and paste the job description to get a match score and suggestions.
    """)

    resume_file = st.file_uploader("📁 Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
    jd_text = st.text_area("📌 Paste Job Description here", height=200)

    if resume_file and jd_text:
        with st.spinner("🔍 Extracting text from resume..."):
            resume_text = extract_text_from_resume(resume_file)

        if resume_text:
            st.subheader("📝 Resume Text Preview:")
            st.write(resume_text[:500] + "..." if len(resume_text) > 500 else resume_text)

            # Extract skills
            resume_skills = extract_skills(resume_text)
            jd_skills = extract_skills(jd_text)

            matched_skills = resume_skills.intersection(jd_skills)
            missing_skills = jd_skills - resume_skills

            match_score = round((len(matched_skills) / len(jd_skills)) * 100, 2) if jd_skills else 0.0

            # Display results
            st.subheader("✅ Skill Match Results")
            st.markdown(f"**🎯 Match Score:** `{match_score}%`")
            st.markdown(f"**✅ Matched Skills ({len(matched_skills)}):** {', '.join(matched_skills) if matched_skills else 'None'}")
            st.markdown(f"**⚠️ Missing Skills ({len(missing_skills)}):** {', '.join(missing_skills) if missing_skills else 'None'}")

        else:
            st.error("❌ Could not extract text from resume.")

if __name__ == "__main__":
    main()
