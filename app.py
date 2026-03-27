"""
Global MSol EQS Executive Dashboard
Pinterest Measurement - Strategic Performance Tracker

Executive-level view of EQS health across the portfolio:
- Performance snapshot
- Problem areas and opportunities
- Common challenges
- Pod/channel/sector analysis
- Drill-down capabilities

Author: Kiran Chodavarapu | Built with Claude AI
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page config
st.set_page_config(
    page_title="EQS Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .metric-good {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .metric-warning {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .metric-critical {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .insight-box {
        background: #f0fdf4;
        border-left: 4px solid #10b981;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    .warning-box {
        background: #fffbeb;
        border-left: 4px solid #f59e0b;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    .critical-box {
        background: #fef2f2;
        border-left: 4px solid #ef4444;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_eqs_data():
    """Load EQS tracker data"""
    file_path = '/Users/kchodavarapu/Global MSol EQS target list 2026 - [use this] EQS status - GCS Tier 1+2 Advertisers.csv'
    df = pd.read_csv(file_path)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert spend columns to numeric
    spend_cols = ['last_28d_spend', 'last_90d_spend', 'last_365d_spend']
    for col in spend_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Convert EQS scores to numeric
    eqs_score_cols = ['web_eqs_score', 'app_eqs_score', 'offline_eqs_score']
    for col in eqs_score_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df

# Header
st.markdown('<h1 class="main-header">📊 EQS Executive Dashboard</h1>', unsafe_allow_html=True)
st.markdown("**Global MSol EQS Target List 2026** | Strategic Performance Tracker")
st.caption("Real-time portfolio health | AI-powered insights")

# Load data
df = load_eqs_data()

# Sidebar filters
st.sidebar.header("🎯 Filters")

# Pod filter
all_pods = ['All'] + sorted([p for p in df['pod'].dropna().unique() if p != '#N/A'])
selected_pods = st.sidebar.multiselect(
    "Filter by Pod:",
    options=all_pods[1:],
    default=all_pods[1:] if len(all_pods) > 1 else []
)

# Pod channel filter
all_channels = ['All'] + sorted([c for c in df['pod_channel'].dropna().unique() if c != '#N/A'])
selected_channels = st.sidebar.multiselect(
    "Filter by Pod Channel:",
    options=all_channels[1:],
    default=all_channels[1:] if len(all_channels) > 1 else []
)

# Pod sector filter
all_sectors = ['All'] + sorted([s for s in df['pod_sector'].dropna().unique() if s != '#N/A'])
selected_sectors = st.sidebar.multiselect(
    "Filter by Pod Sector:",
    options=all_sectors[1:],
    default=all_sectors[1:] if len(all_sectors) > 1 else []
)

# Service tier filter
service_tiers = st.sidebar.multiselect(
    "Filter by Service Tier:",
    options=sorted(df['service_model_tier'].dropna().unique()),
    default=sorted(df['service_model_tier'].dropna().unique())
)

st.sidebar.divider()
st.sidebar.caption("💡 Filters apply to all tabs")

# Apply filters
filtered_df = df.copy()

if selected_pods:
    filtered_df = filtered_df[filtered_df['pod'].isin(selected_pods)]
if selected_channels:
    filtered_df = filtered_df[filtered_df['pod_channel'].isin(selected_channels)]
if selected_sectors:
    filtered_df = filtered_df[filtered_df['pod_sector'].isin(selected_sectors)]
if service_tiers:
    filtered_df = filtered_df[filtered_df['service_model_tier'].isin(service_tiers)]

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎯 Executive Summary",
    "📈 Performance Analysis",
    "⚠️ Problem Areas",
    "🔍 Common Challenges",
    "📊 Detailed Drilldown"
])

with tab1:
    st.header("Executive Summary")

    # Key metrics
    total_advertisers = len(filtered_df)

    # EQS status counts
    web_needs_improvement = len(filtered_df[filtered_df['web_eqs_status'] == 'NEEDS IMPROVEMENT'])
    app_needs_improvement = len(filtered_df[filtered_df['app_eqs_status'] == 'NEEDS IMPROVEMENT'])

    web_fair = len(filtered_df[filtered_df['web_eqs_status'] == 'FAIR'])
    app_fair = len(filtered_df[filtered_df['app_eqs_status'] == 'FAIR'])

    web_good = len(filtered_df[filtered_df['web_eqs_status'] == 'GOOD'])
    app_good = len(filtered_df[filtered_df['app_eqs_status'] == 'GOOD'])

    web_excellent = len(filtered_df[filtered_df['web_eqs_status'] == 'EXCELLENT'])
    app_excellent = len(filtered_df[filtered_df['app_eqs_status'] == 'EXCELLENT'])

    web_na = len(filtered_df[filtered_df['web_eqs_status'].isin(['N/A', '#N/A']) | filtered_df['web_eqs_status'].isna()])
    app_na = len(filtered_df[filtered_df['app_eqs_status'].isin(['N/A', '#N/A']) | filtered_df['app_eqs_status'].isna()])

    # Calculate health score
    total_measured = total_advertisers - web_na
    healthy_count = web_good + web_excellent
    health_score = (healthy_count / total_measured * 100) if total_measured > 0 else 0

    # Top metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Advertisers", f"{total_advertisers:,}")
    with col2:
        st.metric("Portfolio Health Score", f"{health_score:.0f}%",
                 delta=f"Good/Excellent" if health_score >= 70 else "Below Target")
    with col3:
        st.metric("Critical Issues", web_needs_improvement, delta_color="inverse")
    with col4:
        total_spend = filtered_df['last_90d_spend'].sum()
        st.metric("Total 90d Spend", f"${total_spend/1_000_000:.1f}M")

    st.divider()

    # Status breakdown
    st.subheader("📊 EQS Status Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Web EQS Distribution")
        web_status_data = pd.DataFrame({
            'Status': ['NEEDS IMPROVEMENT', 'FAIR', 'GOOD', 'EXCELLENT', 'N/A'],
            'Count': [web_needs_improvement, web_fair, web_good, web_excellent, web_na]
        })

        fig = px.pie(web_status_data, values='Count', names='Status',
                     color='Status',
                     color_discrete_map={
                         'NEEDS IMPROVEMENT': '#ef4444',
                         'FAIR': '#f59e0b',
                         'GOOD': '#10b981',
                         'EXCELLENT': '#059669',
                         'N/A': '#9ca3af'
                     })
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("### App EQS Distribution")
        app_status_data = pd.DataFrame({
            'Status': ['NEEDS IMPROVEMENT', 'FAIR', 'GOOD', 'EXCELLENT', 'N/A'],
            'Count': [app_needs_improvement, app_fair, app_good, app_excellent, app_na]
        })

        fig = px.pie(app_status_data, values='Count', names='Status',
                     color='Status',
                     color_discrete_map={
                         'NEEDS IMPROVEMENT': '#ef4444',
                         'FAIR': '#f59e0b',
                         'GOOD': '#10b981',
                         'EXCELLENT': '#059669',
                         'N/A': '#9ca3af'
                     })
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Key insights
    st.subheader("💡 Key Insights")

    if web_needs_improvement > total_advertisers * 0.5:
        st.markdown('<div class="critical-box">', unsafe_allow_html=True)
        st.markdown(f"**🚨 CRITICAL:** {web_needs_improvement} advertisers ({web_needs_improvement/total_advertisers*100:.0f}%) have NEEDS IMPROVEMENT web EQS status")
        st.markdown("**Action Required:** Immediate remediation needed for portfolio health")
        st.markdown('</div>', unsafe_allow_html=True)
    elif web_needs_improvement > total_advertisers * 0.25:
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown(f"**⚠️ ATTENTION:** {web_needs_improvement} advertisers need EQS improvement")
        st.markdown("**Recommended:** Prioritize high-spend accounts for remediation")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="insight-box">', unsafe_allow_html=True)
        st.markdown(f"**✅ HEALTHY:** Portfolio is in good shape with {web_needs_improvement} accounts needing attention")
        st.markdown('</div>', unsafe_allow_html=True)

    if web_na > total_advertisers * 0.3:
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown(f"**📊 GREY AREA:** {web_na} advertisers ({web_na/total_advertisers*100:.0f}%) have N/A EQS status")
        st.markdown("**Action:** Assess measurement capability and establish baselines")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.header("Performance Analysis by Segment")

    # Performance by pod
    st.subheader("📊 EQS Health by Pod")

    pod_analysis = filtered_df.groupby('pod').agg({
        'g_advertiser_id': 'count',
        'last_90d_spend': 'sum'
    }).reset_index()
    pod_analysis.columns = ['Pod', 'Advertiser Count', 'Total Spend']

    # Calculate status distribution by pod
    pod_status = []
    for pod in filtered_df['pod'].unique():
        pod_df = filtered_df[filtered_df['pod'] == pod]
        pod_status.append({
            'Pod': pod,
            'Needs Improvement': len(pod_df[pod_df['web_eqs_status'] == 'NEEDS IMPROVEMENT']),
            'Fair': len(pod_df[pod_df['web_eqs_status'] == 'FAIR']),
            'Good': len(pod_df[pod_df['web_eqs_status'] == 'GOOD']),
            'Excellent': len(pod_df[pod_df['web_eqs_status'] == 'EXCELLENT']),
            'N/A': len(pod_df[pod_df['web_eqs_status'].isin(['N/A', '#N/A']) | pod_df['web_eqs_status'].isna()])
        })

    df_pod_status = pd.DataFrame(pod_status)

    # Stacked bar chart
    fig = go.Figure()

    for status, color in [
        ('Excellent', '#059669'),
        ('Good', '#10b981'),
        ('Fair', '#f59e0b'),
        ('Needs Improvement', '#ef4444'),
        ('N/A', '#9ca3af')
    ]:
        fig.add_trace(go.Bar(
            name=status,
            x=df_pod_status['Pod'],
            y=df_pod_status[status],
            marker_color=color
        ))

    fig.update_layout(
        barmode='stack',
        title='EQS Status Distribution by Pod',
        xaxis_title='Pod',
        yaxis_title='Number of Advertisers',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Performance by channel
    st.subheader("📊 EQS Health by Channel")

    channel_status = []
    for channel in filtered_df['pod_channel'].dropna().unique():
        if channel != '#N/A':
            channel_df = filtered_df[filtered_df['pod_channel'] == channel]
            needs_imp = len(channel_df[channel_df['web_eqs_status'] == 'NEEDS IMPROVEMENT'])
            total = len(channel_df)
            health_pct = ((total - needs_imp) / total * 100) if total > 0 else 0

            channel_status.append({
                'Channel': channel,
                'Total Advertisers': total,
                'Needs Improvement': needs_imp,
                'Health %': health_pct,
                'Total Spend': channel_df['last_90d_spend'].sum()
            })

    df_channel_status = pd.DataFrame(channel_status).sort_values('Health %', ascending=True)

    fig = px.bar(df_channel_status, x='Health %', y='Channel', orientation='h',
                 color='Health %',
                 color_continuous_scale=['#ef4444', '#f59e0b', '#10b981'],
                 title='Channel Health Score (% of accounts NOT needing improvement)')

    st.plotly_chart(fig, use_container_width=True)

    # Show table
    df_channel_display = df_channel_status.copy()
    df_channel_display['Total Spend'] = df_channel_display['Total Spend'].apply(lambda x: f"${x/1_000_000:.1f}M")
    df_channel_display['Health %'] = df_channel_display['Health %'].apply(lambda x: f"{x:.0f}%")

    st.dataframe(df_channel_display, use_container_width=True, hide_index=True)

with tab3:
    st.header("⚠️ Problem Areas & Opportunities")

    # Critical accounts
    st.subheader("🚨 Critical Accounts (Needs Improvement)")

    critical = filtered_df[filtered_df['web_eqs_status'] == 'NEEDS IMPROVEMENT'].copy()
    critical = critical.sort_values('last_90d_spend', ascending=False)

    if len(critical) > 0:
        # Top 10 by spend
        top_critical = critical.head(10)

        st.markdown(f"**{len(critical)} total accounts need improvement** | Showing top 10 by spend:")

        critical_display = top_critical[[
            'ultimate_parent_name', 'advertiser_account_name', 'pod', 'pod_channel',
            'web_eqs_score', 'web_eqs_status', 'web blocker', 'web resolution timing',
            'last_90d_spend'
        ]].copy()

        critical_display['last_90d_spend'] = critical_display['last_90d_spend'].apply(
            lambda x: f"${x/1_000_000:.2f}M" if pd.notna(x) and x > 0 else '-'
        )

        critical_display.columns = ['Parent', 'Account', 'Pod', 'Channel', 'EQS Score',
                                   'Status', 'Blocker', 'Resolution Timing', '90d Spend']

        st.dataframe(critical_display, use_container_width=True, hide_index=True)

        # Impact analysis
        critical_spend = critical['last_90d_spend'].sum()
        total_spend = filtered_df['last_90d_spend'].sum()
        critical_pct = (critical_spend / total_spend * 100) if total_spend > 0 else 0

        col1, col2, col3 = st.columns(3)
        col1.metric("Accounts at Risk", len(critical))
        col2.metric("Spend at Risk", f"${critical_spend/1_000_000:.1f}M")
        col3.metric("% of Portfolio", f"{critical_pct:.1f}%")

    else:
        st.success("✅ No accounts with NEEDS IMPROVEMENT status!")

    st.divider()

    # Grey areas (N/A status)
    st.subheader("🌫️ Grey Areas (N/A Status)")

    grey = filtered_df[filtered_df['web_eqs_status'].isin(['N/A', '#N/A']) | filtered_df['web_eqs_status'].isna()].copy()
    grey = grey.sort_values('last_90d_spend', ascending=False)

    if len(grey) > 0:
        st.markdown(f"**{len(grey)} accounts with N/A status** | Assessment needed:")

        grey_display = grey.head(10)[[
            'ultimate_parent_name', 'advertiser_account_name', 'pod', 'service_model_tier',
            'primary_msot', 'last_90d_spend'
        ]].copy()

        grey_display['last_90d_spend'] = grey_display['last_90d_spend'].apply(
            lambda x: f"${x/1_000_000:.2f}M" if pd.notna(x) and x > 0 else '-'
        )

        grey_display.columns = ['Parent', 'Account', 'Pod', 'Service Tier', 'MSOT', '90d Spend']

        st.dataframe(grey_display, use_container_width=True, hide_index=True)

        grey_spend = grey['last_90d_spend'].sum()
        st.info(f"💡 **Action:** Assess measurement capability for these {len(grey)} accounts (${grey_spend/1_000_000:.1f}M in spend)")
    else:
        st.success("✅ All accounts have defined EQS status!")

with tab4:
    st.header("🔍 Common Challenges & Blockers")

    # Blocker analysis
    st.subheader("🚧 Top Blockers")

    # Web blockers
    web_blockers = filtered_df['web blocker'].dropna()
    web_blockers = web_blockers[web_blockers != '']

    if len(web_blockers) > 0:
        blocker_counts = web_blockers.value_counts().head(10)

        fig = px.bar(
            x=blocker_counts.values,
            y=blocker_counts.index,
            orientation='h',
            title='Top 10 Web EQS Blockers',
            labels={'x': 'Number of Accounts', 'y': 'Blocker'},
            color=blocker_counts.values,
            color_continuous_scale='Reds'
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### Blocker Details")

        for blocker in blocker_counts.head(5).index:
            affected = len(filtered_df[filtered_df['web blocker'] == blocker])
            with st.expander(f"**{blocker}** ({affected} accounts)"):
                affected_accounts = filtered_df[filtered_df['web blocker'] == blocker][[
                    'ultimate_parent_name', 'advertiser_account_name', 'pod',
                    'web_eqs_score', 'web resolution timing'
                ]].head(10)

                affected_accounts.columns = ['Parent', 'Account', 'Pod', 'EQS Score', 'Resolution Timing']
                st.dataframe(affected_accounts, use_container_width=True, hide_index=True)
    else:
        st.info("No blockers recorded in current selection")

    st.divider()

    # Resolution timing analysis
    st.subheader("⏱️ Resolution Timing Distribution")

    resolution_timing = filtered_df['web resolution timing'].dropna()
    resolution_timing = resolution_timing[resolution_timing != '']

    if len(resolution_timing) > 0:
        timing_counts = resolution_timing.value_counts()

        fig = px.pie(
            values=timing_counts.values,
            names=timing_counts.index,
            title='Resolution Timing Distribution',
            hole=0.4
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # MSOT analysis
    st.subheader("📊 MSOT Distribution (Problem Accounts)")

    problem_accounts = filtered_df[filtered_df['web_eqs_status'] == 'NEEDS IMPROVEMENT']

    if len(problem_accounts) > 0:
        msot_dist = problem_accounts['primary_msot'].value_counts().head(10)

        fig = px.bar(
            x=msot_dist.values,
            y=msot_dist.index,
            orientation='h',
            title='MSOT Distribution for Accounts Needing Improvement',
            labels={'x': 'Number of Accounts', 'y': 'Primary MSOT'}
        )

        st.plotly_chart(fig, use_container_width=True)

with tab5:
    st.header("📊 Detailed Drilldown")

    # Search and filter
    col1, col2 = st.columns([3, 1])

    with col1:
        search_term = st.text_input("🔍 Search by advertiser name:", "")

    with col2:
        status_filter = st.selectbox(
            "Filter by Status:",
            ['All', 'NEEDS IMPROVEMENT', 'FAIR', 'GOOD', 'EXCELLENT', 'N/A']
        )

    # Apply search
    detail_df = filtered_df.copy()

    if search_term:
        detail_df = detail_df[
            detail_df['ultimate_parent_name'].str.contains(search_term, case=False, na=False) |
            detail_df['advertiser_account_name'].str.contains(search_term, case=False, na=False)
        ]

    if status_filter != 'All':
        detail_df = detail_df[detail_df['web_eqs_status'] == status_filter]

    # Show results
    st.subheader(f"Found {len(detail_df)} accounts")

    if len(detail_df) > 0:
        # Key columns for display
        display_cols = [
            'ultimate_parent_name', 'advertiser_account_name', 'pod', 'pod_channel', 'pod_sector',
            'service_model_tier', 'primary_msot',
            'web_eqs_score', 'web_eqs_status', 'app_eqs_score', 'app_eqs_status',
            'web blocker', 'web resolution timing',
            'last_28d_spend', 'last_90d_spend', 'last_365d_spend'
        ]

        detail_display = detail_df[display_cols].copy()

        # Format spend
        for col in ['last_28d_spend', 'last_90d_spend', 'last_365d_spend']:
            detail_display[col] = detail_display[col].apply(
                lambda x: f"${x/1_000_000:.2f}M" if pd.notna(x) and x > 0 else '-'
            )

        detail_display.columns = [
            'Parent', 'Account', 'Pod', 'Channel', 'Sector', 'Service Tier', 'MSOT',
            'Web Score', 'Web Status', 'App Score', 'App Status',
            'Blocker', 'Resolution', '28d Spend', '90d Spend', '365d Spend'
        ]

        st.dataframe(detail_display, use_container_width=True, hide_index=True, height=600)

        # Export option
        csv = detail_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Full Data (CSV)",
            data=csv,
            file_name=f"eqs_detailed_export_{pd.Timestamp.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

# Footer
st.divider()
st.caption("Built with AI | Data refreshes automatically | Last updated: March 2026")
st.caption("💡 **AI-Powered Insights:** This dashboard demonstrates how AI saves time by instantly surfacing critical issues, trends, and opportunities from complex data.")
