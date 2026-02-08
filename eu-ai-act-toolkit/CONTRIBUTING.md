
```markdown
# Contributing to EU AI Act Toolkit

Thank you for your interest in contributing! 🎉

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/yourusername/eu-ai-act-toolkit/issues)
2. If not, create a new issue using the bug report template
3. Include:
   - Python version (`python --version`)
   - Operating system
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable

### Suggesting Features

1. Open a new issue using the feature request template
2. Clearly describe:
   - The problem or use case
   - Your proposed solution
   - Why it would be valuable
   - Any alternatives you've considered

### Pull Requests

1. **Fork the repository**
2. **Create a branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes**
4. **Test thoroughly**:
   ```bash
   streamlit run app.py
   # Test all pages and features
   ```
5. **Commit with clear messages**: `git commit -m "Add feature: your description"`
6. **Push**: `git push origin feature/your-feature-name`
7. **Open a Pull Request** with detailed description

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/eu-ai-act-toolkit.git
cd eu-ai-act-toolkit

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Code Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Comment complex logic

## Testing

Before submitting a PR, ensure:
- [ ] App runs without errors
- [ ] All pages load correctly
- [ ] Forms validate properly
- [ ] Charts display correctly
- [ ] Export functions work

## Regulatory Updates

When updating EU AI Act compliance data:
1. Reference official sources
2. Document changes in CHANGELOG.md
3. Update README if user-facing
4. Test classification logic thoroughly

## Questions?

Open an issue or discussion! We're here to help.

---

**Thank you for contributing to AI compliance!** 🇪🇺
```
