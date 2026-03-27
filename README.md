# Global MSol EQS Executive Dashboard

## AI-Powered Strategic Measurement Health Tracking

**Author:** Kiran Chodavarapu
**Built With:** Claude AI (Anthropic)
**Source:** Global MSol EQS Target List 2026
**Date:** March 2026

---

## The Challenge

Managing Event Quality Score (EQS) health across Pinterest's entire measurement portfolio:
- 100+ advertisers across multiple pods, channels, and sectors
- Web and App EQS tracking with different status levels
- Complex blocker identification and resolution tracking
- Need for executive-level visibility with drill-down capability
- Strategic prioritization of improvement efforts

**Traditional approach: Hours of manual CSV analysis and pivot tables**

---

## The AI Solution

Leveraged Claude AI to build an executive dashboard that:
1. **Aggregates** portfolio health metrics automatically
2. **Identifies** critical problem areas requiring immediate attention
3. **Analyzes** common blockers and grey areas
4. **Enables** flexible filtering by pod, channel, sector, and service tier
5. **Provides** drill-down from executive summary to account-level details

**Result: Real-time strategic visibility replacing hours of manual analysis**

---

## Dashboard Features

### 1. Executive Summary
- Portfolio health score with color-coded status
- Web and App EQS distribution (pie charts)
- Key insights: critical accounts, grey areas, spend at risk
- Quick status of total accounts and measurement coverage

### 2. Performance Analysis
- Pod-level performance with stacked bar charts
- Channel health scores comparison
- Sector-level breakdown
- Service tier analysis

### 3. Problem Areas
- Critical accounts needing improvement (sorted by spend)
- Grey area accounts with N/A status
- Impact analysis: spend at risk
- Priority queue for immediate action

### 4. Common Challenges
- Top 10 blocker analysis with frequency counts
- Resolution timing distribution
- MSOT distribution for problem accounts
- Strategic insight into systemic issues

### 5. Detailed Drilldown
- Full data table with all columns
- Search by advertiser name
- Filter by EQS status (Web/App)
- CSV export capability

---

## Live Dashboard

**Local:** `streamlit run app.py`

**Streamlit Cloud:** Deploy at [share.streamlit.io](https://share.streamlit.io/)

---

## Key Metrics Tracked

### EQS Status Levels
- **EXCELLENT**: Optimal event quality
- **GOOD**: Healthy measurement setup
- **FAIR**: Acceptable with minor issues
- **NEEDS IMPROVEMENT**: Critical action required
- **N/A**: Grey area - no active measurement or pending setup

### Portfolio Health Score
Formula: `(Good + Excellent accounts) / Total measured accounts × 100`

### Critical Metrics
- Total accounts tracked
- Accounts with active measurement
- Spend at risk from critical accounts
- Grey area spend (N/A status)
- Top blockers by frequency

---

## How This Demonstrates AI Value

### 1. Speed
- **Manual:** Hours of CSV analysis + pivot tables
- **AI-Assisted:** Instant dashboard with real-time filtering
- **Result:** Day-to-day strategic companion

### 2. Strategic Clarity
- Executive summary with health score
- Automatic prioritization by spend
- Visual identification of problem areas
- Blocker pattern recognition

### 3. Flexibility
- Filter by pod, channel, sector, service tier
- Drill from portfolio view to account details
- Export filtered data for further analysis
- Adaptable to changing portfolio

### 4. Actionability
- Critical accounts sorted by impact (spend)
- Common challenges identified for systemic fixes
- Grey areas flagged for process improvement
- Clear priorities for measurement team

---

## Technical Stack

- **Streamlit**: Interactive dashboard framework
- **Pandas**: Data processing and filtering
- **Plotly**: Executive-level visualizations
- **Python 3.9+**: Core language

---

## Deployment Instructions

### Local Testing
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Streamlit Cloud Deployment
1. Push to GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Sign in with GitHub (Deekay507)
4. Click **New app**
5. Select repository and set main file to `app.py`
6. Click **Deploy**

---

## Files in This Project

```
app.py                                          # Main dashboard
requirements.txt                                # Python dependencies
Global MSol EQS target list 2026 - [...].csv   # Source data
README.md                                       # This file
```

---

## Usage for Leadership

### Tell the Story
1. **The Challenge**: Managing EQS health across 100+ advertisers
2. **The Solution**: AI-powered executive dashboard
3. **The Impact**: Instant strategic visibility, no manual analysis
4. **The Value**: Daily companion for measurement health tracking

### Key Talking Points
- "Real-time portfolio health score across all advertisers"
- "Instant identification of critical accounts by spend impact"
- "Common blocker analysis reveals systemic issues"
- "Grey area tracking for process improvements"
- "Flexible filtering for pod/channel-specific reviews"

### Metrics to Share
- Portfolio health score: X% (Good + Excellent)
- Critical accounts: X advertisers needing improvement
- Spend at risk: $X from critical accounts
- Top blockers: Top 3-5 most common issues
- Grey areas: X accounts with undefined measurement

---

## Future Enhancements

1. **Trend Analysis**: Historical EQS tracking over time
2. **Automated Alerts**: Notifications when accounts drop to NEEDS IMPROVEMENT
3. **Blocker Resolution Tracking**: Time-to-resolution metrics
4. **Predictive Analytics**: AI forecasts for EQS risk
5. **Integration**: Pull live data from measurement systems

---

## Contact

**Kiran Chodavarapu**
Tech & Telco Measurement Lead
*Demonstrating AI as a daily strategic companion*

---

**Built with Claude AI | March 2026**
