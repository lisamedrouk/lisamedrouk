

```markdown
# Installation Guide

## Prerequisites

- **Python 3.8 or higher** ([Download](https://www.python.org/downloads/))
- **pip** package manager (included with Python)
- **Git** ([Download](https://git-scm.com/downloads))

## Quick Install

### Option 1: Clone from GitHub

```bash
# Clone the repository
git clone https://github.com/yourusername/eu-ai-act-toolkit.git

# Navigate to directory
cd eu-ai-act-toolkit

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Option 2: Install as Package

```bash
pip install git+https://github.com/yourusername/eu-ai-act-toolkit.git
euai-toolkit
```

### Option 3: Download ZIP

1. Download ZIP from [Releases](https://github.com/yourusername/eu-ai-act-toolkit/releases)
2. Extract the archive
3. Open terminal in extracted folder
4. Run: `pip install -r requirements.txt`
5. Run: `streamlit run app.py`

## Verification

Test that everything works:

```bash
# Verify Python version (should be 3.8+)
python --version

# Verify Streamlit installation
streamlit version

# Test app import
python -c "import streamlit, pandas, plotly; print('✅ Success!')"
```

## First Run

```bash
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

## Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

## Troubleshooting

### Issue: `streamlit: command not found`

**Solution:**
```bash
python -m streamlit run app.py
```

### Issue: Module import errors

**Solution:**
```bash
pip install --upgrade -r requirements.txt
```

### Issue: Permission denied

**Solution (Windows):**
Run Command Prompt as Administrator

**Solution (macOS/Linux):**
```bash
pip install --user -r requirements.txt
```

## System Requirements

- **RAM**: 512 MB minimum (1 GB recommended)
- **Disk Space**: 100 MB
- **Internet**: Required for initial installation only
```
