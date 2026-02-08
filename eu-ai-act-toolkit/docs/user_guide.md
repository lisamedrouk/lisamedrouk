
```markdown
# User Guide

## Getting Started

### Launching the Application

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your browser.

## Main Features

### 1. Dashboard 🏠

The dashboard provides an overview of all assessments:

- **Total Assessments**: Count of all evaluations
- **High Risk Systems**: Number of high-risk classifications
- **Limited Risk**: Count of limited-risk systems
- **Average Risk Score**: Mean score across all assessments

**Charts:**
- Risk Distribution (Pie Chart)
- Assessment Timeline (Line Chart)

### 2. New Assessment ➕

Create a new AI system evaluation:

**Required Fields:**
- **System Name**: Descriptive name for your AI
- **Sector**: Choose from dropdown (Employment, Healthcare, Finance, Retail,  etc.)
- **Use Case**: Detailed description of what the AI does
- **Context**: Where and how it's deployed
- **Data Types**: Select all applicable types

**Optional Fields:**
- **Deployment Stage**: Current stage (Planning to Production)
- **Automated Decisions**: Check if fully automated
- **Real-time Processing**: Check if processes data in real-time

**Click "Analyze System"** to get instant classification.

### 3. Results Page

After analysis, you'll see:

**Risk Classification:**
- Risk Level (Unacceptable, High, Limited, Minimal)
- Risk Score (0-100)
- Compliance Score
- Can Deploy? (Yes/No)

**Visualizations:**
- Risk Score Gauge
- Compliance Progress Chart

**Recommendations:**
- Specific actions based on risk level
- EU AI Act article references
- Compliance requirements

**Export Options:**
- Download as JSON
- View full details

### 4. Analytics 📊

View trends and patterns:

**Overview Tab:**
- Timeline of assessments
- Risk distribution over time

**Details Tab:**
- Complete data table
- Export to CSV

### 5. History 📚

Browse past assessments:

- Filter by sector and risk level
- Sort by date or score
- Click to view full details
- Expandable cards for each assessment

## Examples

### Example 1: High-Risk Recruitment AI

```
System Name: AI Recruitment Assistant
Sector: Employment
Use Case: Automated CV screening and candidate ranking using NLP
Context: Used by HR for initial filtering of job applications
Data Types: Personal data, Behavioral data
Automated Decisions: ✓
```

**Expected Result**: HIGH RISK (80-90)

### Example 2: Limited-Risk Chatbot

```
System Name: Customer Service Bot
Sector: Customer Service
Use Case: Answers product questions and handles basic support
Context: E-commerce website, 24/7 availability
Data Types: Text data
```

**Expected Result**: LIMITED RISK (30-40)

## Tips & Best Practices

1. **Be Specific**: Provide detailed use case descriptions
2. **Select All Data Types**: Include all types your system processes
3. **Export Regularly**: Save assessments as JSON for records
4. **Review History**: Compare similar systems
5. **Update Assessments**: Re-evaluate when systems change

## Keyboard Shortcuts

- **Ctrl+R**: Reload page
- **Ctrl+S**: Save (in browser)
- **Tab**: Navigate form fields

## Support

- 📧 Email: contact@example.com
- 🐛 Report bugs: [GitHub Issues](https://github.com/yourusername/eu-ai-act-toolkit/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/eu-ai-act-toolkit/discussions)
```
