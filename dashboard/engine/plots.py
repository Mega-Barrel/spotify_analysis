import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


data = pd.read_csv('../../dataset/csv_data/streaming_data_data.csv')


data['release_date'] =  pd.to_datetime(data['release_date'])
data['end_time'] =  pd.to_datetime(data['end_time'])
data['minutes_played'] = data[' ms_played'].divide(60000)
data.drop(' ms_played', axis=1, inplace=True)
data['days'] = [d.date() for d in data['end_time']]
data['time'] = [d.time() for d in data['end_time']]


def most_artist_played(df):
    most_played_artists_by_count = df.groupby(by='artist_name')['track_name'].count().sort_values(ascending=False)[:20]
    fig = go.Figure(
        data=[
            go.Bar(
                x = most_played_artists_by_count.index, 
                y = most_played_artists_by_count.values,
                marker = {
                    'color' : most_played_artists_by_count.values
                },
                text = most_played_artists_by_count.index,
            )
        ]
    )
    fig.update_layout(
        title_text= 'Popularity Of Artists By Number Of Times Their Song Was Played',
        barmode='group', 
        xaxis_tickangle=45,
        xaxis_title = "Name",
        yaxis_title = "Count",
        hovermode = 'x',
        height = 650,
        width = 1210,
    )
    return fig

def top_songs_listened(df):
    most_played_songs_count = df.groupby(by='track_name')['track_name'].count().sort_values(ascending=False)[:25]
    # plot for count of track listened
    fig = go.Figure(
        data=[
            go.Bar(
                x = most_played_songs_count.index, 
                y = most_played_songs_count.values,
                marker = {
                    'color' : most_played_songs_count.values
                },
                text = most_played_songs_count.index,
                textposition = 'inside'
            )
        ]
    )
    fig.update_layout(
        title_text='Count of tracks listened',
        barmode='group', 
        xaxis_tickangle=45,
        xaxis_title = "track_name",
        yaxis_title = "track_count",
        height = 800,
        width = 1210,
        hovermode = 'x',
    )
    return fig
    
def songs_listened_month(df):
    # plot for count of track listened
    month = df['month'].value_counts().sort_index(ascending=True)

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

    fig = go.Figure(
        data=[
            go.Bar(
                x = months, 
                y = month.values,
                marker = {
                    'color' : month.values
                },
                text = months,
                textposition = 'inside'
            )
        ]
    )
    fig.update_layout(
        title_text='Count of songs listened as per month',
        barmode='group', 
        xaxis_title = "month",
        yaxis_title = "count",
        height = 800,
        width = 1210,
        hovermode = 'x'
    )
    return fig


def popular_song_artist_by_minutes(df):
    amount_of_time = df.groupby(by='artist_name')['minutes_played'].sum().sort_values(ascending=False)[:15]
    # plot for count of track listened
    fig = go.Figure(
        data=[
            go.Bar(
                x = amount_of_time.index, 
                y = amount_of_time.values,
                marker = {
                    'color' : amount_of_time.values
                },
                text = amount_of_time.index,
                textposition = 'inside'
            )
        ]
    )
    fig.update_layout(
        title_text='Popularity of artists by amount of time spent listening to their song',
        barmode='group', 
        xaxis_tickangle=45,
        xaxis_title = "track_name",
        yaxis_title = "track_count",
        height = 800,
        width = 1210,
        hovermode = 'x',
    )
    return fig
    

def song_timeline(df):
    day = df.groupby(by=['days'], as_index=False).sum()
    fig = px.line(
        day, 
        x="days", 
        y="minutes_played",
        labels={
            "day": "Month",
            "minutes_played": "Minutes Played"
        },
        color_discrete_sequence = px.colors.sequential.Agsunset, 
        title = "Timeline Of My Streaming History"
    )

    fig.update_layout(
        hovermode = 'x'
    )
    return fig


def time_spend_all_days(df):
    df['week_day_name'] = pd.DatetimeIndex(df['days']).day_name()
    fig = px.pie(
        df, 
        names="week_day_name", 
        values="minutes_played", 
        color_discrete_sequence = px.colors.sequential.Agsunset
    )
    fig.update_layout(
        title = 'Time spend listening on each day of week'
    )
    return fig


def radial_plot():
    categories = ['danceability','energy',
                'loudness', 'speechiness', 'acousticness']
    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
                r = [0.375, 0.461, -6.202, 0.0279, 0.6270],
                theta=categories,
                fill='toself',
                name='Selfish'
        )
    )
    fig.add_trace(go.Scatterpolar(
                r=[0.281, 0.462, -6.638, 0.0674, 0.4980],
                theta=categories,
                fill='toself',
                name='Still Have Me'
        )
    )
    fig.add_trace(go.Scatterpolar(
                r=[0.836, 0.544, -5.975, 0.0943, 0.0403],
                theta=categories,
                fill='toself',
                name='IDGAF'
        )
    )
    fig.add_trace(
        go.Scatterpolar(
                r = [0.460, 0.800, -3.584, 0.0500, 0.2890],
                theta=categories,
                fill = 'toself',
                name = 'What I Like About You (feat. Theresa Rex)'
        )
    )
    fig.add_trace(
        go.Scatterpolar(
                r = [0.726, 0.554, -5.290, 0.0917, 0.0421],
                theta = categories,
                fill='toself',
                name='break up with your girlfriend, i\'m bored'
        )
    )
    fig.update_layout(
        title = "Diversity in audio features of top 5 songs",
        polar=dict(
        radialaxis = dict(
                visible=True,
                range=[-10, 1]
                )
        ),
        showlegend=True
    )
    return fig


    