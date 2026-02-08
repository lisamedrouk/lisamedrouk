```python
"""
Setup configuration for EU AI Act Toolkit
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="eu-ai-act-toolkit",
    version="1.0.0",
    author="Lm",
    author_email="contact@example.com",
    description="Professional compliance toolkit for EU AI Act assessment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/eu-ai-act-toolkit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Legal Industry",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.31.0",
        "pandas>=2.1.4",
        "plotly>=5.18.0",
    ],
    entry_points={
        'console_scripts': [
            'euai-toolkit=app:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
```

