import streamlit as st
from scripts.extract_text import extract_text_from_resume

def main():
    st.set_page_config(page_title="ResMatch AI", page_icon="📄", layout="centered")
    st.title("ResMatch AI - Resume Analyzer & Job Match Scorer")

    st.markdown("""
    Upload your resume (PDF or DOCX) and paste the job description to get a match score and improvement suggestions.
    """)

    # Upload Resume File
    resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
    
    # Job Description input
    jd_text = st.text_area("Paste Job Description here", height=200)

    if resume_file and jd_text:
        with st.spinner("Extracting resume text..."):
            resume_text = extract_text_from_resume(resume_file)
        
        if resume_text:
            st.subheader("Extracted Resume Text (Preview):")
            st.write(resume_text[:1000] + "...")  # Preview first 1000 chars

            # TODO: Call skill extraction, matching & scoring here
            st.info("Next steps: skill extraction and match scoring will appear here.")
        else:
            st.error("Failed to extract text from resume. Please upload a valid PDF or DOCX file.")

if __name__ == "__main__":
    main()

