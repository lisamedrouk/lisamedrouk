"""
EU AI Act Toolkit - Complete Enhanced Streamlit Application
Professional compliance assessment with advanced features
Author: Lm - AI Governance Expert, Paris
Version: 1.0.0
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json
from typing import Dict, List

# Page Configuration
st.set_page_config(
    page_title="EU AI Act Toolkit",
    page_icon="🇪🇺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #003399 0%, #0066cc 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #003399;
    }
    
    .risk-unacceptable {
        background-color: #ffebee;
        border-left: 5px solid #d32f2f;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .risk-high {
        background-color: #fff3e0;
        border-left: 5px solid #f57c00;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .risk-limited {
        background-color: #fffde7;
        border-left: 5px solid #fbc02d;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .risk-minimal {
        background-color: #e8f5e9;
        border-left: 5px solid #388e3c;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .recommendation-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 3px solid #003399;
    }
</style>
""", unsafe_allow_html=True)

# EU AI Act Knowledge Base
EU_AI_ACT_RULES = {
    "prohibited_practices": [
        {
            "id": "P1",
            "article": "Article 5(1)(a)",
            "title": "Subliminal Manipulation",
            "description": "AI systems using subliminal techniques beyond consciousness",
            "keywords": ["subliminal", "subconscious", "manipulative"],
            "fine": "€35M or 7% global turnover"
        },
        {
            "id": "P2",
            "article": "Article 5(1)(b)",
            "title": "Exploitation of Vulnerabilities",
            "description": "Systems exploiting vulnerabilities of specific groups",
            "keywords": ["children", "vulnerable", "disability", "exploitation"],
            "fine": "€35M or 7% global turnover"
        },
        {
            "id": "P3",
            "article": "Article 5(1)(c)",
            "title": "Social Scoring",
            "description": "Social scoring by public authorities",
            "keywords": ["social scoring", "social credit", "citizen scoring"],
            "fine": "€35M or 7% global turnover"
        }
    ],
    "high_risk_systems": [
        {
            "id": "HR1",
            "annex": "Annex III(1)",
            "title": "Biometric Identification",
            "description": "Biometric identification and categorization",
            "keywords": ["biometric", "facial recognition", "fingerprint", "iris"],
            "sector": "Critical Infrastructure",
            "fine": "€15M or 3% global turnover"
        },
        {
            "id": "HR2",
            "annex": "Annex III(2)",
            "title": "Education Assessment",
            "description": "AI in education and vocational training",
            "keywords": ["education", "student assessment", "exam proctoring"],
            "sector": "Education",
            "fine": "€15M or 3% global turnover"
        },
        {
            "id": "HR3",
            "annex": "Annex III(3)",
            "title": "Employment & Recruitment",
            "description": "AI for recruitment and hiring decisions",
            "keywords": ["recruitment", "hiring", "cv screening", "employee"],
            "sector": "Employment",
            "fine": "€15M or 3% global turnover"
        },
        {
            "id": "HR4",
            "annex": "Annex III(4)",
            "title": "Essential Services",
            "description": "Access to essential services",
            "keywords": ["credit scoring", "insurance", "healthcare access"],
            "sector": "Essential Services",
            "fine": "€15M or 3% global turnover"
        },
        {
            "id": "HR5",
            "annex": "Annex III(5)",
            "title": "Law Enforcement",
            "description": "AI for law enforcement purposes",
            "keywords": ["predictive policing", "crime prediction"],
            "sector": "Law Enforcement",
            "fine": "€15M or 3% global turnover"
        }
    ],
    "limited_risk_systems": [
        {
            "id": "LR1",
            "article": "Article 52(1)",
            "title": "AI Interaction Transparency",
            "description": "Systems interacting with humans",
            "keywords": ["chatbot", "conversational ai", "virtual assistant"],
            "fine": "€7.5M or 1.5% global turnover"
        },
        {
            "id": "LR2",
            "article": "Article 52(3)",
            "title": "Deepfakes & Synthetic Media",
            "description": "AI-generated content",
            "keywords": ["deepfake", "synthetic media", "ai-generated"],
            "fine": "€7.5M or 1.5% global turnover"
        }
    ]
}

# Initialize session state
if 'assessments' not in st.session_state:
    st.session_state.assessments = [
        {
            "id": 1,
            "system_name": "CV Screening AI",
            "use_case": "Automated resume screening and candidate ranking",
            "context": "HR recruitment process",
            "data_types": ["Personal data", "Behavioral data"],
            "risk_level": "high",
            "risk_score": 85,
            "compliance_score": 67,
            "date": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
            "matched_rules": ["HR3"],
            "sector": "Employment"
        },
        {
            "id": 2,
            "system_name": "Customer Support Chatbot",
            "use_case": "Automated customer service responses",
            "context": "E-commerce website",
            "data_types": ["Text data"],
            "risk_level": "limited",
            "risk_score": 35,
            "compliance_score": 90,
            "date": (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d'),
            "matched_rules": ["LR1"],
            "sector": "Customer Service"
        }
    ]

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'dashboard'

# Risk Classification Engine
class RiskClassifier:
    def __init__(self):
        self.rules = EU_AI_ACT_RULES
    
    def classify(self, use_case: str, context: str, data_types: List[str]) -> Dict:
        text = f"{use_case} {context} {' '.join(data_types)}".lower()
        
        # Check prohibited practices
        for practice in self.rules['prohibited_practices']:
            if any(keyword in text for keyword in practice['keywords']):
                return {
                    'risk_level': 'unacceptable',
                    'risk_score': 100,
                    'matched_rules': [practice],
                    'can_deploy': False,
                    'fine_amount': practice['fine']
                }
        
        # Check high-risk systems
        high_risk_matches = []
        for system in self.rules['high_risk_systems']:
            matches = sum(1 for keyword in system['keywords'] if keyword in text)
            if matches >= 1:
                high_risk_matches.append(system)
        
        if high_risk_matches:
            base_score = 60
            bonus = min(len(high_risk_matches) * 10, 25)
            score = min(base_score + bonus, 95)
            
            return {
                'risk_level': 'high',
                'risk_score': score,
                'matched_rules': high_risk_matches,
                'can_deploy': True,
                'fine_amount': high_risk_matches[0]['fine']
            }
        
        # Check limited risk
        for system in self.rules['limited_risk_systems']:
            if any(keyword in text for keyword in system['keywords']):
                return {
                    'risk_level': 'limited',
                    'risk_score': 35,
                    'matched_rules': [system],
                    'can_deploy': True,
                    'fine_amount': system['fine']
                }
        
        return {
            'risk_level': 'minimal',
            'risk_score': 15,
            'matched_rules': [],
            'can_deploy': True,
            'fine_amount': 'N/A'
        }
    
    def generate_recommendations(self, risk_level: str) -> List[str]:
        if risk_level == 'unacceptable':
            return [
                "⛔ PROHIBITED - Cannot be deployed in EU",
                "Consider alternative approaches",
                "Consult legal experts immediately"
            ]
        elif risk_level == 'high':
            return [
                "📋 Establish risk management system (Article 9)",
                "📊 Implement data governance (Article 10)",
                "📄 Prepare technical documentation (Article 11)",
                "👤 Design human oversight mechanisms (Article 14)",
                "🛡️ Conduct conformity assessment"
            ]
        elif risk_level == 'limited':
            return [
                "ℹ️ Inform users of AI interaction (Article 52)",
                "🏷️ Label AI-generated content",
                "📝 Document transparency measures"
            ]
        else:
            return [
                "✅ No mandatory compliance",
                "💡 Consider voluntary guidelines",
                "📋 Document for internal governance"
            ]

# Visualization Functions
def create_risk_gauge(risk_score: int, risk_level: str):
    colors = {
        'unacceptable': '#d32f2f',
        'high': '#f57c00',
        'limited': '#fbc02d',
        'minimal': '#388e3c'
    }
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Risk Score", 'font': {'size': 20}},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': colors.get(risk_level, '#757575')},
            'steps': [
                {'range': [0, 25], 'color': '#e8f5e9'},
                {'range': [25, 50], 'color': '#fffde7'},
                {'range': [50, 75], 'color': '#fff3e0'},
                {'range': [75, 100], 'color': '#ffebee'}
            ],
        }
    ))
    
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
    return fig

def create_compliance_chart(compliance_score: int):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=compliance_score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Compliance", 'font': {'size': 20}},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "green" if compliance_score >= 80 else "orange"},
            'steps': [
                {'range': [0, 50], 'color': '#ffebee'},
                {'range': [50, 80], 'color': '#fff3e0'},
                {'range': [80, 100], 'color': '#e8f5e9'}
            ],
        }
    ))
    
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
    return fig

def create_risk_distribution():
    df = pd.DataFrame(st.session_state.assessments)
    risk_counts = df['risk_level'].value_counts()
    
    colors = {
        'unacceptable': '#d32f2f',
        'high': '#f57c00',
        'limited': '#fbc02d',
        'minimal': '#388e3c'
    }
    
    fig = go.Figure(data=[go.Pie(
        labels=risk_counts.index,
        values=risk_counts.values,
        marker=dict(colors=[colors.get(level, '#757575') for level in risk_counts.index]),
        hole=0.4
    )])
    
    fig.update_layout(title="Risk Distribution", height=400)
    return fig

def create_timeline():
    df = pd.DataFrame(st.session_state.assessments)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['date'],
        y=df['risk_score'],
        mode='lines+markers',
        name='Risk Score',
        marker=dict(size=10),
        line=dict(color='#003399', width=2)
    ))
    
    fig.update_layout(
        title="Assessment Timeline",
        xaxis_title="Date",
        yaxis_title="Risk Score",
        height=400
    )
    return fig

# Main Application
def main():
    # Sidebar
    with st.sidebar:
        st.markdown("## 🇪🇺 Navigation")
        
        if st.button("🏠 Dashboard", use_container_width=True):
            st.session_state.current_page = 'dashboard'
        if st.button("➕ New Assessment", use_container_width=True):
            st.session_state.current_page = 'assessment'
        if st.button("📊 Analytics", use_container_width=True):
            st.session_state.current_page = 'analytics'
        if st.button("📚 History", use_container_width=True):
            st.session_state.current_page = 'history'
        if st.button("ℹ️ About", use_container_width=True):
            st.session_state.current_page = 'about'
        
        st.markdown("---")
        st.markdown("### 📈 Quick Stats")
        st.metric("Total", len(st.session_state.assessments))
        high_risk = sum(1 for a in st.session_state.assessments if a['risk_level'] in ['high', 'unacceptable'])
        st.metric("High Risk", high_risk)
        
        st.markdown("---")
        st.markdown("**Developed by:**  \nLm - AI Governance Expert  \nParis, France")
    
    # Route to pages
    if st.session_state.current_page == 'dashboard':
        show_dashboard()
    elif st.session_state.current_page == 'assessment':
        show_assessment_form()
    elif st.session_state.current_page == 'analytics':
        show_analytics()
    elif st.session_state.current_page == 'history':
        show_history()
    elif st.session_state.current_page == 'about':
        show_about()

def show_dashboard():
    st.markdown("""
    <div class="main-header">
        <h1 style="margin:0;">🇪🇺 EU AI Act Toolkit</h1>
        <p style="margin:0.5rem 0 0 0;">Professional Compliance Assessment</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #003399; margin: 0;">Total</h3>
            <p style="font-size: 2.5rem; margin: 0; font-weight: bold;">{len(st.session_state.assessments)}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        high = sum(1 for a in st.session_state.assessments if a['risk_level'] == 'high')
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #f57c00; margin: 0;">High Risk</h3>
            <p style="font-size: 2.5rem; margin: 0; font-weight: bold;">{high}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        limited = sum(1 for a in st.session_state.assessments if a['risk_level'] == 'limited')
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #fbc02d; margin: 0;">Limited</h3>
            <p style="font-size: 2.5rem; margin: 0; font-weight: bold;">{limited}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        avg = sum(a['risk_score'] for a in st.session_state.assessments) / len(st.session_state.assessments)
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #388e3c; margin: 0;">Avg Score</h3>
            <p style="font-size: 2.5rem; margin: 0; font-weight: bold;">{avg:.0f}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_risk_distribution(), use_container_width=True)
    with col2:
        st.plotly_chart(create_timeline(), use_container_width=True)
    
    # Recent assessments
    st.markdown("### 📋 Recent Assessments")
    recent = sorted(st.session_state.assessments, key=lambda x: x['date'], reverse=True)[:3]
    
    for a in recent:
        with st.expander(f"**{a['system_name']}** - {a['date']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Risk Level", a['risk_level'].upper())
            with col2:
                st.metric("Score", f"{a['risk_score']}/100")
            with col3:
                st.metric("Sector", a['sector'])

def show_assessment_form():
    st.title("➕ New AI System Assessment")
    
    with st.form("assessment"):
        st.markdown("### System Information")
        
        system_name = st.text_input("System Name *", placeholder="e.g., Recruitment AI")
        
        col1, col2 = st.columns(2)
        with col1:
            sector = st.selectbox("Sector *", 
                ["Employment", "Healthcare", "Education", "Financial Services", 
                 "Law Enforcement", "Customer Service", "Other"])
        with col2:
            stage = st.selectbox("Stage", 
                ["Planning", "Development", "Testing", "Production"])
        
        use_case = st.text_area("Use Case *", height=100,
            placeholder="Describe what the AI does...")
        
        context = st.text_area("Context *", height=100,
            placeholder="Where and how is it deployed?")
        
        data_types = st.multiselect("Data Types *",
            ["Personal data", "Biometric data", "Sensitive data",
             "Financial data", "Behavioral data", "Text data"])
        
        col1, col2 = st.columns(2)
        with col1:
            automated = st.checkbox("Fully Automated Decisions")
        with col2:
            realtime = st.checkbox("Real-time Processing")
        
        submitted = st.form_submit_button("🔍 Analyze System", type="primary")
        
        if submitted:
            if not all([system_name, use_case, context, data_types]):
                st.error("Please fill all required fields")
            else:
                classifier = RiskClassifier()
                result = classifier.classify(use_case, context, data_types)
                recommendations = classifier.generate_recommendations(result['risk_level'])
                
                compliance_score = 50 + len(data_types) * 5 if result['risk_level'] == 'high' else 85
                
                new_assessment = {
                    'id': max([a['id'] for a in st.session_state.assessments]) + 1,
                    'system_name': system_name,
                    'use_case': use_case,
                    'context': context,
                    'data_types': data_types,
                    'sector': sector,
                    'risk_level': result['risk_level'],
                    'risk_score': result['risk_score'],
                    'compliance_score': compliance_score,
                    'matched_rules': [r.get('id', 'N/A') for r in result['matched_rules']],
                    'recommendations': recommendations,
                    'can_deploy': result['can_deploy'],
                    'fine_amount': result['fine_amount'],
                    'date': datetime.now().strftime('%Y-%m-%d')
                }
                
                st.session_state.assessments.append(new_assessment)
                st.success("✅ Assessment Complete!")
                st.balloons()
                
                # Show results
                st.markdown("---")
                show_results(new_assessment)

def show_results(assessment):
    risk_class = f"risk-{assessment['risk_level']}"
    
    st.markdown(f"""
    <div class="{risk_class}">
        <h2>{assessment['risk_level'].upper()} RISK</h2>
        <h3>{assessment['system_name']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Risk Score", f"{assessment['risk_score']}/100")
    with col2:
        st.metric("Risk Level", assessment['risk_level'].upper())
    with col3:
        st.metric("Compliance", f"{assessment['compliance_score']}%")
    with col4:
        deploy = "✅ Yes" if assessment['can_deploy'] else "❌ No"
        st.metric("Can Deploy?", deploy)
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_risk_gauge(assessment['risk_score'], 
                       assessment['risk_level']), use_container_width=True)
    with col2:
        st.plotly_chart(create_compliance_chart(assessment['compliance_score']), 
                       use_container_width=True)
    
    st.markdown("### 💡 Recommendations")
    for i, rec in enumerate(assessment['recommendations'], 1):
        st.markdown(f"""
        <div class="recommendation-card">
            <strong>{i}.</strong> {rec}
        </div>
        """, unsafe_allow_html=True)
    
    if assessment['risk_level'] in ['high', 'unacceptable']:
        st.error(f"**⚠️ Potential Fine:** {assessment['fine_amount']}")
    
    # Export
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        json_data = json.dumps(assessment, indent=2)
        st.download_button("📄 Download JSON", json_data,
                          f"assessment_{assessment['id']}.json")
    with col2:
        if st.button("🏠 Back to Dashboard"):
            st.session_state.current_page = 'dashboard'
            st.rerun()

def show_analytics():
    st.title("📊 Analytics")
    
    if not st.session_state.assessments:
        st.info("No data yet. Create assessments first!")
        return
    
    tab1, tab2 = st.tabs(["📈 Overview", "🎯 Details"])
    
    with tab1:
        st.plotly_chart(create_timeline(), use_container_width=True)
        st.plotly_chart(create_risk_distribution(), use_container_width=True)
    
    with tab2:
        df = pd.DataFrame(st.session_state.assessments)
        st.dataframe(df[['system_name', 'date', 'sector', 'risk_level', 
                        'risk_score']], use_container_width=True)
        
        csv = df.to_csv(index=False)
        st.download_button("📊 Export CSV", csv, "assessments.csv")

def show_history():
    st.title("📚 Assessment History")
    
    if not st.session_state.assessments:
        st.info("No assessments yet")
        return
    
    for a in sorted(st.session_state.assessments, key=lambda x: x['date'], reverse=True):
        badges = {'unacceptable': '🔴', 'high': '🟠', 'limited': '🟡', 'minimal': '🟢'}
        
        with st.expander(f"{badges[a['risk_level']]} {a['system_name']} - {a['date']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Risk", a['risk_level'].upper())
            with col2:
                st.metric("Score", f"{a['risk_score']}/100")
            with col3:
                st.metric("Sector", a['sector'])
            
            st.markdown(f"**Use Case:** {a['use_case'][:200]}...")

def show_about():
    st.title("ℹ️ About")
    
    st.markdown("""
    ### 🇪🇺 EU AI Act Toolkit
    
    Professional compliance assessment platform for EU AI Act.
    
    ### Risk Levels
    
    - 🔴 **Unacceptable**: Prohibited (€35M fine)
    - 🟠 **High**: Full compliance required (€15M fine)
    - 🟡 **Limited**: Transparency obligations (€7.5M fine)
    - 🟢 **Minimal**: No obligations
    
    ### Developer
    
    **Lm** - AI Governance Expert  
    📍 Paris, France
    
    ### Disclaimer
    
    This tool provides guidance only. Consult legal professionals for 
    formal compliance verification.
    
    **Version:** 1.0.0  
    **Updated:** February 2025
    """)

if __name__ == "__main__":
    main()