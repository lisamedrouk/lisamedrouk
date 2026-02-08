
```markdown
# 🇪🇺 EU AI Act Compliance Toolkit

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Professional web application for assessing AI systems against EU Artificial Intelligence Act requirements. Built with Streamlit for ease of use and rapid deployment.

![Dashboard Screenshot](assets/screenshot.png)

## 🎯 Features

- **Automated Risk Classification** - Classifies AI systems into 4 risk levels based on EU AI Act Annex III
- **Interactive Assessment Forms** - User-friendly interface for system evaluation
- **Real-time Compliance Analysis** - Instant risk scoring and recommendations
- **Advanced Visualizations** - Interactive charts powered by Plotly
- **Export Capabilities** - Download assessments as JSON or CSV
- **Assessment History** - Track and compare multiple evaluations
- **Analytics Dashboard** - Visualize trends and distributions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/eu-ai-act-toolkit.git
cd eu-ai-act-toolkit

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The application will open automatically at `http://localhost:8501`

### Using pip

```bash
pip install -e .
euai-toolkit
```

## 📖 Usage

### Web Interface

1. **Start the application**: `streamlit run app.py`
2. **Navigate to "New Assessment"** in the sidebar
3. **Fill in the assessment form**:
   - System name
   - Sector (Employment, Healthcare, etc.)
   - Use case description
   - Deployment context
   - Data types processed
4. **Click "Analyze System"**
5. **View results** with risk classification, compliance score, and recommendations
6. **Export** your assessment as JSON

### Example Assessment

```
System Name: CV Screening Tool
Sector: Employment
Use Case: Automated screening and ranking of job applications
Context: Used by HR department for initial candidate filtering
Data Types: Personal data, Behavioral data
```

**Expected Result**: HIGH RISK (85/100) - Full EU AI Act compliance required

## 📊 Risk Levels

| Level | Description | Fine (Max) | Examples |
|-------|-------------|-----------|----------|
| 🔴 **Unacceptable** | Prohibited practices | €35M or 7% turnover | Social scoring, manipulation |
| 🟠 **High** | Significant risk to rights | €15M or 3% turnover | Hiring, biometrics, credit scoring |
| 🟡 **Limited** | Transparency required | €7.5M or 1.5% turnover | Chatbots, deepfakes |
| 🟢 **Minimal** | No specific obligations | N/A | Most other AI systems |

## 🛠️ Technology Stack

- **Framework**: [Streamlit](https://streamlit.io) 1.31.0
- **Data Processing**: [Pandas](https://pandas.pydata.org) 2.1.4
- **Visualizations**: [Plotly](https://plotly.com) 5.18.0
- **Language**: Python 3.8+

## 📚 Documentation

- [Installation Guide](docs/installation.md)
- [User Guide](docs/user_guide.md)
- [API Reference](docs/api_reference.md)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💼 Author

**Lm** - AI Governance Expert  
📍 Paris, France  
🎓 Specializing in EU AI Act compliance and regulatory strategy

## ⚖️ Disclaimer

This toolkit provides guidance based on EU AI Act requirements. **It does not constitute legal advice.** Organizations should consult qualified legal professionals for formal compliance verification.

## 🙏 Acknowledgments

- European Commission for EU AI Act framework
- Streamlit team for the excellent framework
- Open source community

## 📧 Contact

- **Issues**: [GitHub Issues](https://github.com/yourusername/eu-ai-act-toolkit/issues)
- **Email**: contact@example.com
- **Website**: [www.example.com](https://www.example.com)

## 🌟 Star History

If you find this project useful, please consider giving it a ⭐️ on GitHub!

---

**Made with ❤️ for AI compliance**
```

---