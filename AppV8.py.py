#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df_reduced = pd.read_csv('reduced_dataset.csv')

# Define the vibrant color palette
vibrant_palette = {
    'positive': '#00CC96',
    'neutral': '#636EFA',
    'negative': '#EF553B'
}

# Title of the dashboard
st.title("Music Data Dashboard")

# Sidebar filters
selected_genres = st.sidebar.multiselect(
    "Choose your Vibe (Genre)",
    options=df_reduced['track_genre'].unique(),
    default=[]
)

mood_metric = st.sidebar.selectbox(
    "Select Your Mood Metric",
    options=[
        'danceability', 
        'energy', 
        'valence', 
        'acousticness', 
        'liveness', 
        'speechiness'
    ],
    index=0
)

# Filter data based on selection
if selected_genres:
    filtered_df = df_reduced[df_reduced['track_genre'].isin(selected_genres)]
else:
    filtered_df = df_reduced

# Generate plots
fig_genre_sentiment = px.bar(
    filtered_df.groupby(['track_genre', 'sentiment']).size().reset_index(name='count'),
    x='track_genre', y='count', color='sentiment', barmode='stack',
    color_discrete_map=vibrant_palette, 
    title='Sentiment Distribution by Genre'
)
fig_genre_sentiment.update_layout(
    title_font_size=24, title_font_color='#2E86C1', title_x=0.5,
    xaxis_title='Genre', yaxis_title='Count',
    legend_title=dict(text='Sentiment', font=dict(color='black')), 
    xaxis_tickangle=-45,
    plot_bgcolor='white', paper_bgcolor='white',
    font=dict(size=16, color='black'),
    xaxis=dict(tickfont=dict(color='black'), titlefont=dict(color='black')),
    yaxis=dict(tickfont=dict(color='black'), titlefont=dict(color='black')),
    legend=dict(font=dict(color='black')),
    margin=dict(l=80, r=20, t=60, b=40)
)

fig_sentiment_popularity = px.box(
    filtered_df, x='sentiment', y='popularity', color='sentiment', 
    color_discrete_map=vibrant_palette,
    title='Sentiment vs. Popularity'
)
fig_sentiment_popularity.update_layout(
    title_font_size=24, title_font_color='#2E86C1', title_x=0.5,
    xaxis_title='Sentiment', yaxis_title='Popularity',
    plot_bgcolor='white', paper_bgcolor='white',
    font=dict(size=16, color='black'),
    xaxis=dict(tickfont=dict(color='black'), titlefont=dict(color='black')),
    yaxis=dict(tickfont=dict(color='black'), titlefont=dict(color='black')),
    legend=dict(font=dict(color='black')),
    margin=dict(l=80, r=20, t=60, b=40)
)

fig_sentiment_danceability = px.box(
    filtered_df, x='sentiment', y='danceability', color='sentiment', 
    color_discrete_map=vibrant_palette,
    title='Sentiment vs. Danceability'
)
fig_sentiment_danceability.update_layout(
    title_font_size=24, title_font_color='#2E86C1', title_x=0.5,
    xaxis_title='Sentiment', yaxis_title='Danceability',
    plot_bgcolor='white', paper_bgcolor='white',
    font=dict(size=16, color='black'),
    xaxis=dict(tickfont=dict(color='black'), titlefont=dict(color='black')),
    yaxis=dict(tickfont=dict(color='black'), titlefont=dict(color='black')),
    legend=dict(font=dict(color='black')),
    margin=dict(l=80, r=20, t=60, b=40)
)

fig_sentiment_energy = px.box(
    filtered_df, x='sentiment', y='energy', color='sentiment', 
    color_discrete_map=vibrant_palette,
    title='Sentiment vs. Energy'
)
fig_sentiment_energy.update_layout(
    title_font_size=24, title_font_color='#2E86C1', title_x=0.5,
    xaxis_title='Sentiment', yaxis_title='Energy',
    plot_bgcolor='white', paper_bgcolor='white',
    font=dict(size=16, color='black'),
    xaxis=dict(tickfont=dict(color='black'), titlefont=dict(color='black')),
    yaxis=dict(tickfont=dict(color='black'), titlefont=dict(color='black')),
    legend=dict(font=dict(color='black')),
    margin=dict(l=80, r=20, t=60, b=40)
)

fig_mood_navigator = px.scatter(
    filtered_df, x=mood_metric, y='energy', color='sentiment', size='popularity', 
    hover_data=['track_name', 'artists'], color_discrete_map=vibrant_palette,
    title=f'Find Your Track Based on {mood_metric} and Energy'
)
fig_mood_navigator.update_layout(
    title_font_size=24, title_font_color='#2E86C1', title_x=0.05,
    xaxis_title=mood_metric.capitalize(), yaxis_title='Energy',
    plot_bgcolor='white', paper_bgcolor='white',
    font=dict(size=16, color='black'),
    xaxis=dict(tickfont=dict(color='black'), titlefont=dict(color='black')),
    yaxis=dict(tickfont=dict(color='black'), titlefont=dict(color='black')),
    legend=dict(font=dict(color='black')),
    margin=dict(l=80, r=20, t=60, b=40)
)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Mood Navigator", "Sentiment Distribution by Genre", "Sentiment vs. Popularity", 
     "Sentiment vs. Danceability", "Sentiment vs. Energy"]
)

with tab1:
    st.plotly_chart(fig_mood_navigator)

with tab2:
    st.plotly_chart(fig_genre_sentiment)

with tab3:
    st.plotly_chart(fig_sentiment_popularity)

with tab4:
    st.plotly_chart(fig_sentiment_danceability)

with tab5:
    st.plotly_chart(fig_sentiment_energy)


# In[ ]:




