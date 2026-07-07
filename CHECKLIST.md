# Getting Started Checklist

Follow this checklist to set up your Personal AI Chatbot.

## ☐ Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Expected output**: All packages installed successfully

**If errors occur**: 
- Ensure Python 3.8+ is installed
- Try: `pip install --upgrade pip`
- Use virtual environment: `python -m venv venv`

---

## ☐ Step 2: Get OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign up or log in to your account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)
5. Save it somewhere safe (you can't view it again)

**Cost**: ~$5 credit for new accounts, then pay-as-you-go

---

## ☐ Step 3: Configure Environment

Edit `.env` file:

```env
OPENAI_API_KEY=sk-your-actual-key-here
```

**Important**: 
- Remove the placeholder text
- Paste your actual API key
- No spaces or quotes around the key
- Save the file

---

## ☐ Step 4: Add Your Resume Information

Fill in these files with your actual information:

### ☐ `resume.txt`
- [ ] Name and contact information
- [ ] Professional summary
- [ ] Career objective

### ☐ `data/skills.txt`
- [ ] Programming languages
- [ ] Frameworks & libraries
- [ ] Tools & technologies
- [ ] Soft skills

### ☐ `data/experience.txt`
- [ ] Job titles and companies
- [ ] Dates and locations
- [ ] Responsibilities and achievements
- [ ] Technologies used

### ☐ `data/projects.txt`
- [ ] Project names
- [ ] Descriptions
- [ ] Technologies used
- [ ] Key features and impact

### ☐ `data/education.txt`
- [ ] Degrees and institutions
- [ ] Dates and GPAs
- [ ] Coursework
- [ ] Certifications

**Tip**: See `EXAMPLE_DATA.md` for formatting examples

---

## ☐ Step 5: Verify Setup

Run the test script:

```bash
python test_setup.py
```

**Expected output**:
```
✓ PASS - Package Installation
✓ PASS - Project Structure
✓ PASS - Environment Config
⚠️ PASS - Resume Data Files (may warn about placeholders)
✓ PASS - Custom Modules
```

**If any tests fail**: Check the error messages and fix the issues

---

## ☐ Step 6: Run the Application

```bash
streamlit run app.py
```

**Expected output**:
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
```

**If errors occur**:
- Check API key in `.env`
- Ensure all resume files have content
- Verify all dependencies installed

---

## ☐ Step 7: Test the Chatbot

Try these sample questions:

1. "What are your main technical skills?"
2. "Tell me about your work experience"
3. "What projects have you worked on?"
4. "What is your educational background?"
5. "Do you have experience with [specific technology]?"

**Expected behavior**:
- Quick responses (1-2 seconds)
- Relevant information from your resume
- Natural, conversational tone
- Source documents shown in expander

---

## ☐ Step 8: Customize (Optional)

### Change Model Quality
Edit `.env`:
```env
# Budget-friendly
LLM_MODEL=gpt-3.5-turbo

# High quality
LLM_MODEL=gpt-4-turbo-preview
```

### Adjust Response Style
Edit `.env`:
```env
# More factual (0.0-0.3)
LLM_TEMPERATURE=0.2

# Balanced (0.4-0.7)
LLM_TEMPERATURE=0.7

# More creative (0.8-1.0)
LLM_TEMPERATURE=0.9
```

### Modify Personality
Edit `src/rag.py` line ~50 to customize the system prompt

---

## Troubleshooting Checklist

### ☐ API Key Issues
- [ ] Key starts with `sk-`
- [ ] No spaces or quotes in `.env`
- [ ] Key is active on OpenAI platform
- [ ] Account has credits

### ☐ Import Errors
- [ ] Python 3.8+ installed
- [ ] All packages in `requirements.txt` installed
- [ ] No conflicting package versions

### ☐ Empty or Bad Responses
- [ ] Resume files have actual content (not placeholders)
- [ ] Multiple files filled in (not just one)
- [ ] At least 50-100 words per file
- [ ] Proper formatting (see `EXAMPLE_DATA.md`)

### ☐ Performance Issues
- [ ] First query takes longer (loads models)
- [ ] Subsequent queries faster
- [ ] Good internet connection
- [ ] Not hitting rate limits

---

## Quick Reference

### Start the App
```bash
streamlit run app.py
```

### Test Setup
```bash
python test_setup.py
```

### CLI Mode
```bash
python -m src.chatbot
```

### View Documentation
- `README.md` - Full documentation
- `QUICKSTART.md` - Quick setup guide
- `CONFIG_GUIDE.md` - Configuration options
- `EXAMPLE_DATA.md` - Resume examples
- `PROJECT_SUMMARY.md` - Technical overview

---

## Success Criteria

Your chatbot is ready when:

- [x] All files created
- [ ] Dependencies installed
- [ ] API key configured
- [ ] Resume data filled in
- [ ] Test script passes
- [ ] App runs without errors
- [ ] Chatbot answers questions accurately
- [ ] Source documents retrieved correctly

---

## Next Steps

### Immediate
- [ ] Share with friends/recruiters
- [ ] Test different questions
- [ ] Refine resume content
- [ ] Adjust configuration

### Future
- [ ] Deploy to Streamlit Cloud
- [ ] Add to personal website
- [ ] Integrate with LinkedIn
- [ ] Add more features

---

## Need Help?

### Documentation
- Start with `QUICKSTART.md`
- Check `CONFIG_GUIDE.md` for settings
- Read `EXAMPLE_DATA.md` for examples
- Review `PROJECT_SUMMARY.md` for details

### Common Issues
Most issues are due to:
1. Missing or invalid API key
2. Empty resume files
3. Missing dependencies

### Testing
Run `python test_setup.py` to identify issues

---

**Estimated Setup Time**: 15-30 minutes

**Ready?** Start with Step 1! ✨
