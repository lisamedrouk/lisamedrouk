
```python
"""
Basic tests for EU AI Act Toolkit
"""

def test_imports():
    """Test that all required modules can be imported"""
    try:
        import streamlit
        import pandas
        import plotly
        assert True
    except ImportError as e:
        assert False, f"Import failed: {e}"

def test_risk_classifier():
    """Test risk classification logic"""
    from app import RiskClassifier
    
    classifier = RiskClassifier()
    
    # Test high-risk classification
    result = classifier.classify(
        "Automated hiring decisions",
        "HR department",
        ["Personal data"]
    )
    assert result['risk_level'] in ['high', 'unacceptable', 'limited', 'minimal']
    assert 0 <= result['risk_score'] <= 100
    assert isinstance(result['can_deploy'], bool)

def test_recommendations():
    """Test recommendation generation"""
    from app import RiskClassifier
    
    classifier = RiskClassifier()
    
    for level in ['unacceptable', 'high', 'limited', 'minimal']:
        recs = classifier.generate_recommendations(level)
        assert isinstance(recs, list)
        assert len(recs) > 0

if __name__ == "__main__":
    test_imports()
    test_risk_classifier()
    test_recommendations()
    print("✅ All tests passed!")
```