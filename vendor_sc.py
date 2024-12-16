import streamlit as st
import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd
import os

st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

# st.sidebar.write("# Vendor Scorecard")
# option = st.selectbox("Select Vendor",("MUSP","ABCD","XTED"))

st.title("VirVentures FBM - Vendor Scorecard")

df = pd.read_csv("vendor_sc.csv")
print(df)

vendor_list = df["VENDOR CODE"]
month_list = df["Month"].unique()


col1,col2 = st.columns(2)
with col1:
    vendor_selected = st.selectbox("Select Vendor",vendor_list)
with col2:
    month_selected = st.selectbox("Select month",month_list)
    
df = df[(df['VENDOR CODE'] == vendor_selected) & (df['Month'] == month_selected)]
    
    # CSS for the custom table-like component
st.markdown(
        """
        <style>
        .custom-table {
            border: 1px solid black; /* Black border around the table */
            border-collapse: collapse; /* Remove gaps between table cells */
            width: 100%; /* Full-width table */
        }
        .custom-table th, .custom-table td {
            border: 1px solid black; /* Add borders to cells */
            padding: 10px; /* Padding inside cells */
            text-align: left; /* Align text to the left */
            vertical-align: middle; /* Center-align vertically */
        }
        .header-green {
            background-color: #e8f5e9; /* Light green background for header */
            font-weight: bold; /* Bold header text */
            font-size: 18px; /* Larger font size for description */
        }
        .description-row {
            text-align: left;
            font-size: 30px; /* Larger font size for description */
            font-weight: bold; /* Bold description text */
            height: 60px; /* Increase the height of the row */
            
        }
        .score-column {
            font-size: 30px; /* Larger font for the score */
            font-weight: bold; /* Bold score text */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # HTML for the custom table-like component
st.markdown(
        f"""
        <table class="custom-table">
            <tr>
                <td class="description-row" rowspan="2">{df["Vendor Name"].iloc[0]}</td>
                <th class="header-green">SCORE</th>
            </tr>
            <tr>
                <td class="score-column">{df['TOTAL SCORE'].iloc[0]}/100</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True,
    )


    # Basic Metrics
    # CSS for the custom card component
st.markdown(
        """
        <style>
        .custom-card {
            border: 1px solid black; /* Black border */
            # border-radius: 5px; /* Rounded corners */
            width: 162px; /* Fixed width */
            padding: 5px;
            text-align: center; /* Center text */
            margin: auto; /* Center the card horizontally */
        }
        .card-header {
            background-color: #e8f5e9; /* Light green background */
            padding: 10px;
            font-weight: bold; /* Bold text */
            color: black; /* Black text */
            border-bottom: 1px solid black; /* Optional: border below header */
        }
        .card-value {
            font-size: 27px; /* Larger font size for value */
            margin: 10px 0; /* Spacing around the value */
            font-weight: bold; /* Bold header text */
        }
        .card-footer {
            font-size: 14px; /* Smaller font size for footer */
            color: gray; /* Gray text */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

Period = "Jan - Jul, 2024"
YTD_Sales = df['YTD Sales'].iloc[0]
YTD_CM = df['YTD CM'].iloc[0]
YTD_CM_PCT = round(YTD_CM/YTD_Sales*100,2)
    # HTML for the custom card component

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="custom-card">
            <div class="card-header">YTD SALES</div>
            <div class="card-value">$ {df['YTD Sales'].iloc[0]}</div>
            <div class="card-footer">{Period}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        f"""
        <div class="custom-card">
            <div class="card-header">YTD CM</div>
            <div class="card-value">$ {df['YTD CM'].iloc[0]}</div>
            <div class="card-footer">{Period}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        f"""
        <div class="custom-card">
            <div class="card-header">Last Month Sales</div>
            <div class="card-value">$ {df['Sales'].iloc[0]}</div>
            <div class="card-footer">{Period}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col4:
    st.markdown(
        f"""
        <div class="custom-card">
            <div class="card-header">YTD CM %</div>
            <div class="card-value">{YTD_CM_PCT}%</div>
            <div class="card-footer">{Period}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Inject CSS for custom styling
st.markdown(
        """
        <style>
        .custom-table {
            border: 1px solid black;
            border-collapse: collapse;
            width: 100%;
            margin: auto;
        }
        .custom-table th, .custom-table td {
            border: 1px solid black;
            padding: 10px;
            text-align: center;
            vertical-align: middle;
        }
        .custom-table .header {
            font-size: 18px;
            font-weight: bold;
            text-align: left;
            padding-left: 10px;
            border-bottom: 3px solid black; /* Thick bottom border for first row */
            border-right: none; /* Remove internal borders */
        }
        .custom-table .time-range {
            font-size: 14px;
            font-weight: bold;
            color: gray;
            text-align: center;
            border-bottom: 3px solid black; /* Thick bottom border for last column */
            border-left: 1px solid black; /* Keep border between this and the previous column */
        }
        .custom-table .highlight {
            background-color: #fff4d6;
            font-size: 24px;
            font-weight: bold;
            color: #4a4a4a;
            border: 1px solid black; /* Keep border for the last column */
        }
        .custom-table .scoring-band {
            font-weight: bold;
            text-align: center;
            font-size: 14px;
            color: black;
            border: none; /* Remove borders for this column */
        }
        .custom-table .values {
            font-size: 14px;
            font-weight: bold;
            text-align: center;
            border: none; /* Remove borders for these columns */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    
profitability_score = int(round(df['Gross Margin Score'].iloc[0]/15*100,0))
competition_score = int(round(df['BuyBox Win Rate Score'].iloc[0]/15*100,0))
efficiency_score = int(round(df['Operational Performance Total'].iloc[0]/24*100,0))
perfomance_score = int(round(df['Contribution Margin Bridge Gap'].iloc[0]/26*100,0))
quality_score = int(round(df['Sales Return Rate Score'].iloc[0]/10*100,0))
diversification_score = int(round(df['Non-Amazon.com Sales Score'].iloc[0]/10*100,0))
    
data = {
    'x': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'y': [10, 20, 15, 25, 30],
    }

    # Create the Plotly chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['x'], y=data['y'], mode='lines+markers+text', text=data["y"],
textposition="top center", name='Trend'))
fig.update_layout(
        width=400,  # Match container width
        height=200,  # Match container height
        margin=dict(l=0, r=0, t=18, b=0),  # No margins
    )

    # Export the chart as HTML
chart_html = pio.to_html(fig, full_html=False)

html_scorecard = f"""
    <div style="
        border: 1px solid black; 
        border-radius: 0px; 
        padding: 5px; 
        min-width: 240px;
        min-height: 256px;
        max-height: 256px;
        margin: 0px;
    ">
        <div style="
            font-weight: bold; 
            font-size: 16px; 
            background-color: #EAF3E2; 
            padding: 10px; 
            text-align: left;
            border-bottom: 1px solid black;
        ">
            Scorecard
        </div>
        <div style="margin-top: 15px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px; margin-right:8px; margin-left:8px;">
                <div style="font-weight: bold;">1</div>
                <div style="width: 60%; text-align: left;">Profitability</div>
                <div style="background-color: #EAF3E2; font-size: 14px; color: black; padding: 3px 7px; border-radius: 15px; font-weight: bold;">
                    {profitability_score}%
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px; margin-right:8px; margin-left:8px;">
                <div style="font-weight: bold;">2</div>
                <div style="width: 60%; text-align: left;">Competition</div>
                <div style="background-color: #EAF3E2; font-size: 14px; color: black; padding: 3px 7px; border-radius: 15px; font-weight: bold;">
                    {competition_score}%
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px; margin-right:8px; margin-left:8px;">
                <div style="font-weight: bold;">3</div>
                <div style="width: 60%; text-align: left;">Efficiency</div>
                <div style="background-color: #EAF3E2; font-size: 14px; color: black; padding: 3px 7px; border-radius: 15px; font-weight: bold;">
                    {efficiency_score}%
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px; margin-right:8px; margin-left:8px;">
                <div style="font-weight: bold;">4</div>
                <div style="width: 60%; text-align: left;">Performance</div>
                <div style="background-color: #EAF3E2; font-size: 14px; color: black; padding: 3px 7px; border-radius: 15px; font-weight: bold;">
                    {perfomance_score}%
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px; margin-right:8px; margin-left:8px;">
                <div style="font-weight: bold;">5</div>
                <div style="width: 60%; text-align: left;">Quality</div>
                <div style="background-color: #EAF3E2; font-size: 14px; color: black; padding: 3px 7px;border-radius: 15px; font-weight: bold;">
                    {quality_score}%
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px; margin-right:8px; margin-left:8px;">
                <div style="font-weight: bold;">6</div>
                <div style="width: 60%; text-align: left;">Diversification</div>
                <div style="background-color: #EAF3E2; font-size: 14px; color: black; padding: 3px 7px; border-radius: 15px; font-weight: bold;">
                    {diversification_score}%
                </div>
            </div>
        </div>
    </div>
    """

    # Trend Chart HTML
html_trend = f"""
    <div style="
        border: 1px solid black; 
        border-radius: 0px; 
        padding: 5px; 
        max-width: 450px;
        min-width: 410px;
        min-height: 256px;
        max-height: 256px;
        margin: 0px;
    ">
        <div style="
            font-weight: bold; 
            font-size: 16px; 
            background-color: #EAF3E2; 
            padding: 10px; 
            text-align: left;
            border-bottom: 1px solid black;
        ">
            Trend
        </div>
        <div style="width: 100%; height: 100%;">
            {chart_html}
        </div>
    </div>
    """
final_html = f"""
    <div style="display: flex; gap: 20px; align-items: flex-start; justify-content: flex-start;">
        <div>{html_scorecard}</div>
        <div>{html_trend}</div>
    </div>
    """

    # Render the final layout in Streamlit
st.components.v1.html(final_html, height=290)
    
    # # HTML for the borderless table inside a bordered box
    # html = f"""
    # <div style="
    #     border: 1px solid black; 
    #     border-radius: 0px; 
    #     padding: 5px; 
    #     max-width: 270px;
    #     min-height: 306px;
    #     max-height: 306px;
    #     margin: auto;
    # ">
    #     <!-- Header -->
    #     <div style="
    #         font-weight: bold; 
    #         font-size: 18px; 
    #         background-color: #EAF3E2; 
    #         padding: 10px; 
    #         text-align: left;
    #         border-bottom: 1px solid black;
    #     ">
    #         Scorecard
    #     </div>
    #     <!-- Table -->
    #     <div style="margin-top: 15px;">
    #         <div style="display: flex; justify-content: space-between; margin-bottom: 10px; margin-right:8px; margin-left:8px;">
    #             <div style="font-weight: bold;">1</div>
    #             <div style="width: 60%; text-align: left;">Profitability</div>
    #             <div style="background-color: #EAF3E2; font-size: 14px; color: black; padding: 3px 7px; border-radius: 15px; font-weight: bold;">
    #                 {profitability_score}%
    #             </div>
    #         </div>
    #         <div style="display: flex; justify-content: space-between; margin-bottom: 10px; margin-right:8px; margin-left:8px;">
    #             <div style="font-weight: bold;">2</div>
    #             <div style="width: 60%; text-align: left;">Competition</div>
    #             <div style="background-color: #EAF3E2; font-size: 14px; color: black; padding: 3px 7px; border-radius: 15px; font-weight: bold;">
    #                 {competition_score}%
    #             </div>
    #         </div>
    #         <div style="display: flex; justify-content: space-between; margin-bottom: 10px; margin-right:8px; margin-left:8px;">
    #             <div style="font-weight: bold;">3</div>
    #             <div style="width: 60%; text-align: left;">Efficiency</div>
    #             <div style="background-color: #EAF3E2; font-size: 14px; color: black; padding: 3px 7px; border-radius: 15px; font-weight: bold;">
    #                 {efficiency_score}%
    #             </div>
    #         </div>
    #         <div style="display: flex; justify-content: space-between; margin-bottom: 10px; margin-right:8px; margin-left:8px;">
    #             <div style="font-weight: bold;">4</div>
    #             <div style="width: 60%; text-align: left;">Performance</div>
    #             <div style="background-color: #EAF3E2; font-size: 14px; color: black; padding: 3px 7px; border-radius: 15px; font-weight: bold;">
    #                 {perfomance_score}%
    #             </div>
    #         </div>
    #         <div style="display: flex; justify-content: space-between; margin-bottom: 10px; margin-right:8px; margin-left:8px;">
    #             <div style="font-weight: bold;">5</div>
    #             <div style="width: 60%; text-align: left;">Quality</div>
    #             <div style="background-color: #EAF3E2; font-size: 14px; color: black; padding: 3px 7px;border-radius: 15px; font-weight: bold;">
    #                 {quality_score}%
    #             </div>
    #         </div>
    #         <div style="display: flex; justify-content: space-between; margin-bottom: 10px; margin-right:8px; margin-left:8px;">
    #             <div style="font-weight: bold;">6</div>
    #             <div style="width: 60%; text-align: left;">Diversification</div>
    #             <div style="background-color: #EAF3E2; font-size: 14px; color: black; padding: 3px 7px; border-radius: 15px; font-weight: bold;">
    #                 {diversification_score}%
    #             </div>
    #         </div>
    #     </div>
    # </div>
    # """
    


    # html2 = f"""
    # <div style="
    #     border: 1px solid black; 
    #     border-radius: 0px; 
    #     padding: 5px; 
    #     max-width: 450px;
    #     min-height: 306px;
    #     max-height: 306px;
    #     margin: auto;
    # ">
    #     <!-- Header -->
    #     <div style="
    #         font-weight: bold; 
    #         font-size: 18px; 
    #         background-color: #EAF3E2; 
    #         padding: 10px; 
    #         text-align: left;
    #         border-bottom: 1px solid black;
    #     ">
    #         Trend
    #     </div>
    #     <! -- Chart -->
    #     <div style="width: 100%; height: 100%; overflow: hidden;">
    #         {chart_html}
    #     </div>
    # </div>
    # """

    # # Render the activity tracker in Streamlit

    # final_html = f"""
    # <div style="display: flex; gap: 20px; align-items: flex-start;">
    #     <div>{html}</div>
    #     <div>{html2}</div>
    # </div>
    # """

    # Render the borderless table inside a bordered box in Streamlit
    # col1,col2 = st.columns((2,3))
    # with col1:
    #     st.markdown(html, unsafe_allow_html=True)
    # with col2:
    #     st.components.v1.html(html2, height=330)
    # st.components.v1.html(final_html, height=330)
print(df)

YTD_Sales = float(df["YTD Sales"].iloc[0])
Gross_Margin_pct = df["Gross Margin %"].iloc[0]
Gross_Margin = round(YTD_Sales*(Gross_Margin_pct/100),0)
L30D_Txn = df['Txn Count'].iloc[0]
YTD_CM = df['YTD CM'].iloc[0]
Target_CM = df['YTD CM Target'].iloc[0]
Achieved_CM = round(YTD_CM/Target_CM*100,2)
    
    
    # Render the component
    # HTML structure for the table with no gray header background
st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)  # Adds 20px gap

    # Gross Margins
st.markdown(
        f"""
        <table class="custom-table">
            <!-- Header Row -->
            <tr>
                <td class="header" colspan="3">1.  Gross Margins</td>
                <td class="time-range">TIME RANGE: YTD</td>
                <td class="time-range">Out of 15</td>
            </tr>
            <!-- Labels and Values Row (merged) -->
            <tr class="data-row">
                <td class="values">YTD Sales<br><span style="font-weight: normal;">{YTD_Sales}</span></td>
                <td class="values">YTD Gross Margins<br><span style="font-weight: normal;">{Gross_Margin}</span></td>
                <td class="values">YTD Gross Margins %<br><span style="font-weight: normal;">{Gross_Margin_pct}%</span></td>
                <td class="scoring-band">Scoring Band<br>Between 35% to 55%</td>
                <td class="highlight">{df['Gross Margin Score'].iloc[0]}</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)  # Adds 20px gap
    # BuyBox Win
st.markdown(
        f"""
        <table class="custom-table">
            <!-- Header Row -->
            <tr>
                <td class="header" colspan="3">2.  BUY BOX WIN RATE</td>
                <td class="time-range">TIME RANGE: Last 30 days</td>
                <td class="time-range">Out of 15</td>
            </tr>
            <!-- Labels and Values Row (merged) -->
            <tr class="data-row">
                <td class="values">Active SKU<br><span style="font-weight: normal;">{df['Total Active SKU'].iloc[0]}</span></td>
                <td class="values">SKU with VV in Box<br><span style="font-weight: normal;">{df['SKU with VV in BuyBox'].iloc[0]}</span></td>
                <td class="values">Buy Box Win Rate %<br><span style="font-weight: normal;">{df['BuyBox Win Rate %'].iloc[0]}</span></td>
                <td class="scoring-band">Scoring Band<br>Between 5% to 25%</td>
                <td class="highlight">{df['BuyBox Win Rate Score'].iloc[0]}</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)  # Adds 20px gap
    # Handling Time
st.markdown(
        f"""
        <table class="custom-table">
            <!-- Header Row -->
            <tr>
                <td class="header" colspan="3">3.1.  HANDLING TIME</td>
                <td class="time-range">TIME RANGE: Last 30 days</td>
                <td class="time-range">Out of 3</td>
            </tr>
            <!-- Labels and Values Row (merged) -->
            <tr class="data-row">
                <td class="values">Last 30D Transactions<br><span style="font-weight: normal;">{L30D_Txn}</span></td>
                <td class="values">Avg. Handling time<br><span style="font-weight: normal;">{df['Avg Order Handling time'].iloc[0]}</span></td>
                <td class="values"><br><span style="font-weight: normal;"></span></td>
                <td class="scoring-band">Scoring Band<br>Between 1 day to 3 days</td>
                <td class="highlight">{df['Operational Performance - Handling Time'].iloc[0]}</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True,
    )


st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)  # Adds 20px gap
    # PRE-FULFILLMENT CANCELLATIONS
st.markdown(
        f"""
        <table class="custom-table">
            <!-- Header Row -->
            <tr>
                <td class="header" colspan="3">3.2.  PRE-FULFILLMENT CANCELLATIONS</td>
                <td class="time-range">TIME RANGE: Last 30 days</td>
                <td class="time-range">Out of 3</td>
            </tr>
            <!-- Labels and Values Row (merged) -->
            <tr class="data-row">
                <td class="values">Last 30D Transactions<br><span style="font-weight: normal;">{L30D_Txn}</span></td>
                <td class="values">Cancellations<br><span style="font-weight: normal;">{df['Pre-fulfillment Cancellation'].iloc[0]}</span></td>
                <td class="values">% of Cancellations<br><span style="font-weight: normal;">{df['Pre-fulfillment Cancellations %'].iloc[0]}</span></td>
                <td class="scoring-band">Scoring Band<br>Between 2% to 15%</td>
                <td class="highlight">{df["Operational Performance - Pre-fulfillment cancellations"].iloc[0]}</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True,
    )


st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)  # Adds 20px gap
    # CREDIT TERMS
st.markdown(
        f"""
        <table class="custom-table">
            <!-- Header Row -->
            <tr>
                <td class="header" colspan="3">3.3.  SETTLEMENT CREDIT TERMS</td>
                <td class="time-range">TIME RANGE: Last 30 days</td>
                <td class="time-range">Out of 3</td>
            </tr>
            <!-- Labels and Values Row (merged) -->
            <tr class="data-row">
                <td class="values">Credit Terms<br><span style="font-weight: normal;">{df['Credit Terms Final'].iloc[0]}</span></td>
                <td class="values"><br><span style="font-weight: normal;"></span></td>
                <td class="values"><br><span style="font-weight: normal;"></span></td>
                <td class="scoring-band">Scoring Band<br>Credit or No Credit</td>
                <td class="highlight">{df['Operational Performance - Credit Terms'].iloc[0]}</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)  # Adds 20px gap
    # PRICE UPDATION ERRORS
st.markdown(
        f"""
        <table class="custom-table">
            <!-- Header Row -->
            <tr>
                <td class="header" colspan="3">3.4.  PRICE UPDATION ERRORS</td>
                <td class="time-range">TIME RANGE: LATEST UPDATE</td>
                <td class="time-range">Out of 3</td>
            </tr>
            <!-- Labels and Values Row (merged) -->
            <tr class="data-row">
                <td class="values">Last 30D Transaction<br><span style="font-weight: normal;">{L30D_Txn}</span></td>
                <td class="values">Txn with Pricing Errors<br><span style="font-weight: normal;">{df['Pricing Mismatch'].iloc[0]}</span></td>
                <td class="values">% of Errors<br><span style="font-weight: normal;">{df['Pricing Mismatch %'].iloc[0]}</span></td>
                <td class="scoring-band">Scoring Band<br>Between 2% to 25%</td>
                <td class="highlight">{df['Operational Performance - Pricing Update Errors'].iloc[0]}</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True,
    )


st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)  # Adds 20px gap
    # HANDLING SALES RETURNS
st.markdown(
        f"""
        <table class="custom-table">
            <!-- Header Row -->
            <tr>
                <td class="header" colspan="3">3.5.  HANDLING SALES RETURNS</td>
                <td class="time-range">TIME RANGE: Last 30 days</td>
                <td class="time-range">Out of 3</td>
            </tr>
            <!-- Labels and Values Row (merged) -->
            <tr class="data-row">
                <td class="values">Accepts Returns<br><span style="font-weight: normal;">{df['Returns Terms Final'].iloc[0]}</span></td>
                <td class="values"><br><span style="font-weight: normal;"></span></td>
                <td class="values"><br><span style="font-weight: normal;"></span></td>
                <td class="scoring-band">Scoring Band<br>Yes or No</td>
                <td class="highlight">{df['Operational Performance - Accepts Returns'].iloc[0]}</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True,
    )



st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)  # Adds 20px gap
    # FULFILLMENT RESPONSIBILITY
st.markdown(
        f"""
        <table class="custom-table">
            <!-- Header Row -->
            <tr>
                <td class="header" colspan="3">3.6.  FULFILLMENT RESPONSIBILITY</td>
                <td class="time-range">TIME RANGE: Lastest Update</td>
                <td class="time-range">Out of 3</td>
            </tr>
            <!-- Labels and Values Row (merged) -->
            <tr class="data-row">
                <td class="values">Responsibility<br><span style="font-weight: normal;">{df['Shipping provided by Vendor (SPV) Final'].iloc[0]}</span></td>
                <td class="values"><br><span style="font-weight: normal;"></span></td>
                <td class="values"><br><span style="font-weight: normal;"></span></td>
                <td class="scoring-band">Scoring Band<br>SPV or VV</td>
                <td class="highlight">{df['Operational Performance - Vendor-account shipping'].iloc[0]}</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True,
    )


st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)  # Adds 20px gap
    # SHIPPING COST ESTIMATION
st.markdown(
        f"""
        <table class="custom-table">
            <!-- Header Row -->
            <tr>
                <td class="header" colspan="3">3.7.  SHIPPING COST ESTIMATION</td>
                <td class="time-range">TIME RANGE: Lastest 30 days</td>
                <td class="time-range">Out of 3</td>
            </tr>
            <!-- Labels and Values Row (merged) -->
            <tr class="data-row">
                <td class="values">Last 30D Sales<br><span style="font-weight: normal;">{df['Sales'].iloc[0]}</span></td>
                <td class="values">ABS Variance<br><span style="font-weight: normal;">{df['ABS Shipping Variance'].iloc[0]}</span></td>
                <td class="values">Variance as % of Sales<br><span style="font-weight: normal;">{df['Abs Shipping Variance / Sales %'].iloc[0]}</span></td>
                <td class="scoring-band">Scoring Band<br>Between 0.5% to 3%</td>
                <td class="highlight">{df['Operational Performance - Shipping cost variance'].iloc[0]}</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True,
    )



st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)  # Adds 20px gap
    # EXCLUSIVITY
st.markdown(
        f"""
        <table class="custom-table">
            <!-- Header Row -->
            <tr>
                <td class="header" colspan="3">3.8.  EXCLUSIVITY</td>
                <td class="time-range">TIME RANGE: YTD</td>
                <td class="time-range">Out of 3</td>
            </tr>
            <!-- Labels and Values Row (merged) -->
            <tr class="data-row">
                <td class="values">YTD Sales<br><span style="font-weight: normal;">{df['Sales'].iloc[0]}</span></td>
                <td class="values">YTD Exclusive Sales<br><span style="font-weight: normal;">{df['Exclusive Sales'].iloc[0]}</span></td>
                <td class="values">% of Exclusive Sales<br><span style="font-weight: normal;">{df['Exclusive SKU Sales / Total Sales %'].iloc[0]}</span></td>
                <td class="scoring-band">Scoring Band<br>Between 1% to 10%</td>
                <td class="highlight">{df['Operational Performance - Exclusivity'].iloc[0]}</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True,
    )




st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)  # Adds 20px gap
    # CONTRIBUTION BRIDE GAP
st.markdown(
        f"""
        <table class="custom-table">
            <!-- Header Row -->
            <tr>
                <td class="header" colspan="3">4.  CONTRIBUTION BRIDE GAP</td>
                <td class="time-range">TIME RANGE: YTD</td>
                <td class="time-range">Out of 26</td>
            </tr>
            <!-- Labels and Values Row (merged) -->
            <tr class="data-row">
                <td class="values">Target CM<br><span style="font-weight: normal;">{df['YTD CM Target'].iloc[0]}</span></td>
                <td class="values">Achieved CM<br><span style="font-weight: normal;">{df['YTD CM'].iloc[0]}</span></td>
                <td class="values">% of Target CM<br><span style="font-weight: normal;">{Achieved_CM}</span></td>
                <td class="scoring-band">Scoring Band<br>Between 50% to 100%</td>
                <td class="highlight">{df['Contribution Margin Bridge Gap'].iloc[0]}</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)  # Adds 20px gap
    # SALES RETURN RATE
st.markdown(
        f"""
        <table class="custom-table">
            <!-- Header Row -->
            <tr>
                <td class="header" colspan="3">5.  SALES RETURN RATE</td>
                <td class="time-range">TIME RANGE: YTD</td>
                <td class="time-range">Out of 10</td>
            </tr>
            <!-- Labels and Values Row (merged) -->
            <tr class="data-row">
                <td class="values">YTD Sales<br><span style="font-weight: normal;">{df['Sales'].iloc[0]}</span></td>
                <td class="values">YTD Returns<br><span style="font-weight: normal;">{df['YTD Sales Return'].iloc[0]}</span></td>
                <td class="values">Sales Returns %<br><span style="font-weight: normal;">{df['Sales Return Rate %'].iloc[0]}</span></td>
                <td class="scoring-band">Scoring Band<br>Between 2% to 10%</td>
                <td class="highlight">{df['Sales Return Rate Score'].iloc[0]}</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True,
    )


st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)  # Adds 20px gap
    # VENUE DIVERSIFICATION
st.markdown(
        f"""
        <table class="custom-table">
            <!-- Header Row -->
            <tr>
                <td class="header" colspan="3">6.  VENUE DIVERSIFICATION</td>
                <td class="time-range">TIME RANGE: Last 30 days</td>
                <td class="time-range">Out of 10</td>
            </tr>
            <!-- Labels and Values Row (merged) -->
            <tr class="data-row">
                <td class="values">Last 30 days<br><span style="font-weight: normal;">{df['Sales'].iloc[0]}</span></td>
                <td class="values">Non Amazon.com Sales<br><span style="font-weight: normal;">{df['Non-AMZ.com Sales'].iloc[0]}</span></td>
                <td class="values">% of Diversification<br><span style="font-weight: normal;">{df['% of Non Amazon.com Sales'].iloc[0]}</span></td>
                <td class="scoring-band">Scoring Band<br>Between 5% to 25%</td>
                <td class="highlight">{df['Non-Amazon.com Sales Score'].iloc[0]}</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True,
    )

# # File to store activities
# CSV_FILE = "activities.csv"

#     # Function to load activities from CSV
# def load_activities():
#         if os.path.exists(CSV_FILE):
#             return pd.read_csv(CSV_FILE).to_dict('records')  # Convert to list of dicts
#         return []

#     # Function to save activities to CSV
# def save_activities(activities):
#         df = pd.DataFrame(activities)
#         df.to_csv(CSV_FILE, index=False)

#     # Initialize session state
# if 'activities' not in st.session_state:
#     st.session_state['activities'] = load_activities()

# if 'show_form' not in st.session_state:
#     st.session_state['show_form'] = False

# if 'edit_index' not in st.session_state:
#     st.session_state['edit_index'] = None

# # UI for activity tracking
# st.title("Activity Tracker")

# # Button to toggle "Add Activity" form
# if st.button("Add Activity"):
#     st.session_state['show_form'] = True
#     st.session_state['edit_index'] = None  # Reset editing state

#     # Display activities
# if st.session_state['activities']:
#     st.write("### List of Activities")
#     for i, activity in enumerate(st.session_state['activities']):
#             with st.expander(f"{activity['Activity Title']} ({activity['Status']})"):
#                 st.write(f"**Activity Description:** {activity['Activity Description']}")
#                 st.write(f"**Metric Category:** {activity['Metric Category']}")
#                 st.write(f"**Status:** {activity['Status']}")
#                 st.write(f"**Planned From:** {activity['Planned From']}")
#                 st.write(f"**Activity Stopped On:** {activity['Activity Stopped On']}")
#                 st.write(f"**Implemented By:** {activity['Implemented By']}")

#                 # Edit button for each activity
#                 if st.button(f"Edit", key=f"edit_{i}"):
#                     st.session_state['show_form'] = True
#                     st.session_state['edit_index'] = i
#     else:
#         st.info("No activities added yet.")

#     # Show form only if "Add Activity" or "Edit" is clicked
# if st.session_state['show_form']:
#     with st.form("activity_form", clear_on_submit=True):
#             # Determine whether the form is for adding or editing
#             if st.session_state['edit_index'] is not None:
#                 st.subheader("Edit Activity")
#                 activity = st.session_state['activities'][st.session_state['edit_index']]
#                 activity_title = st.text_input("Activity Title (short text)", activity["Activity Title"])
#                 activity_description = st.text_area("Activity Description (long text)", activity["Activity Description"])
#                 metric_category = st.selectbox(
#                     "Metric Category",
#                     [
#                         "Gross Margin",
#                         "BuyBox Win Rate",
#                         "Operational Performance - Handling Time",
#                         "Operational Performance - Pre-fulfillment cancellations",
#                         "Operational Performance - Credit Terms",
#                         "Operational Performance - Pricing Update Errors",
#                         "Operational Performance - Accepts Returns",
#                         "Operational Performance - Vendor-account shipping",
#                         "Operational Performance - Shipping cost variance",
#                         "Operational Performance - Exclusivity",
#                         "Contribution Margin Bridge Gap",
#                         "Sales Return Rate",
#                         "Non-Amazon.com Sales",
#                     ],
#                     index=[
#                         "Gross Margin",
#                         "BuyBox Win Rate",
#                         "Operational Performance - Handling Time",
#                         "Operational Performance - Pre-fulfillment cancellations",
#                         "Operational Performance - Credit Terms",
#                         "Operational Performance - Pricing Update Errors",
#                         "Operational Performance - Accepts Returns",
#                         "Operational Performance - Vendor-account shipping",
#                         "Operational Performance - Shipping cost variance",
#                         "Operational Performance - Exclusivity",
#                         "Contribution Margin Bridge Gap",
#                         "Sales Return Rate",
#                         "Non-Amazon.com Sales",
#                     ].index(activity["Metric Category"]),
#                 )
#                 status = st.selectbox("Status", ["Active", "On Hold", "Completed"], index=["Active", "On Hold", "Completed"].index(activity["Status"]))
#                 planned_from = st.date_input("Planned from (date)", pd.to_datetime(activity["Planned From"]))
#                 activity_stopped_on = st.date_input("Activity Stopped on (date)", pd.to_datetime(activity["Activity Stopped On"]))
#                 implemented_by = st.text_input("Implemented by", activity["Implemented By"])
#             else:
#                 st.subheader("Add New Activity")
#                 # Empty fields for new activity
#                 activity_title = st.text_input("Activity Title (short text)")
#                 activity_description = st.text_area("Activity Description (long text)")
#                 metric_category = st.selectbox(
#                     "Metric Category",
#                     [
#                         "Gross Margin",
#                         "BuyBox Win Rate",
#                         "Operational Performance - Handling Time",
#                         "Operational Performance - Pre-fulfillment cancellations",
#                         "Operational Performance - Credit Terms",
#                         "Operational Performance - Pricing Update Errors",
#                         "Operational Performance - Accepts Returns",
#                         "Operational Performance - Vendor-account shipping",
#                         "Operational Performance - Shipping cost variance",
#                         "Operational Performance – Exclusivity",
#                         "Contribution Margin Bridge Gap",
#                         "Sales Return Rate",
#                         "Non-Amazon.com Sales",
#                     ],
#                 )
#                 status = st.selectbox("Status", ["Active", "On Hold", "Completed"])
#                 planned_from = st.date_input("Planned from (date)")
#                 activity_stopped_on = st.date_input("Activity Stopped on (date)")
#                 implemented_by = st.text_input("Implemented by")

#             # Submit button
#             submitted = st.form_submit_button("Save Activity")

#             # Handle form submission
#             if submitted:
#                 if activity_title and implemented_by:
#                     new_activity = {
#                         "Activity Title": activity_title,
#                         "Activity Description": activity_description,
#                         "Metric Category": metric_category,
#                         "Status": status,
#                         "Planned From": planned_from,
#                         "Activity Stopped On": activity_stopped_on,
#                         "Implemented By": implemented_by,
#                     }

#                     if st.session_state['edit_index'] is not None:
#                         # Update existing activity
#                         st.session_state['activities'][st.session_state['edit_index']] = new_activity
#                         st.success("Activity updated successfully!")
#                     else:
#                         # Add new activity
#                         st.session_state['activities'].append(new_activity)
#                         st.success("Activity added successfully!")

#                     # Save to CSV and hide the form
#                     save_activities(st.session_state['activities'])
#                     st.session_state['show_form'] = False
#                     st.session_state['edit_index'] = None
#                 else:
#                     st.error("Please fill in the required fields.")
