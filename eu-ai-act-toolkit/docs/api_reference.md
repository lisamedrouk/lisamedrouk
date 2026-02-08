
```markdown
# API Reference

## RiskClassifier

Main classification engine for EU AI Act compliance.

### Methods

#### `classify(use_case: str, context: str, data_types: List[str]) -> Dict`

Classifies an AI system based on inputs.

**Parameters:**
- `use_case` (str): Description of AI functionality
- `context` (str): Deployment environment
- `data_types` (List[str]): Types of data processed

**Returns:**
- Dictionary containing:
  - `risk_level` (str): unacceptable, high, limited, or minimal
  - `risk_score` (int): 0-100
  - `matched_rules` (List[Dict]): Matched regulatory rules
  - `can_deploy` (bool): Whether system can be deployed
  - `fine_amount` (str): Potential non-compliance fine

**Example:**
```python
classifier = RiskClassifier()
result = classifier.classify(
    use_case="CV screening",
    context="HR department",
    data_types=["Personal data"]
)
print(result['risk_level'])  # "high"
```

#### `generate_recommendations(risk_level: str) -> List[str]`

Generates compliance recommendations.

**Parameters:**
- `risk_level` (str): Risk classification level

**Returns:**
- List of actionable recommendations

## Visualization Functions

### `create_risk_gauge(risk_score: int, risk_level: str)`

Creates Plotly gauge chart for risk visualization.

### `create_compliance_chart(compliance_score: int)`

Creates compliance progress gauge.

### `create_risk_distribution()`

Creates pie chart of risk level distribution.

### `create_timeline()`

Creates line chart of assessment timeline.

## Data Structures

### Assessment Object

```python
{
    'id': int,
    'system_name': str,
    'use_case': str,
    'context': str,
    'data_types': List[str],
    'sector': str,
    'risk_level': str,
    'risk_score': int,
    'compliance_score': int,
    'matched_rules': List[str],
    'recommendations': List[str],
    'can_deploy': bool,
    'fine_amount': str,
    'date': str  # YYYY-MM-DD
}
```

## Constants

### EU_AI_ACT_RULES

Dictionary containing EU AI Act regulatory rules:

```python
{
    'prohibited_practices': List[Dict],
    'high_risk_systems': List[Dict],
    'limited_risk_systems': List[Dict]
}
```

Each rule contains:
- `id`: Unique identifier
- `title`: Rule name
- `description`: Detailed description
- `keywords`: Trigger keywords
- `fine`: Non-compliance penalty
```
