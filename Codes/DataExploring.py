import pandas as pd
import plotly
import plotly.graph_objs as go
plotly.offline.init_notebook_mode(connected=True)
import plotly.express as px


data_df = pd.read_csv("Data/CleanMovieData.csv")

# Year of Movie Release
fig = px.histogram(data_df, x="year" )
fig.update_layout(
    title_text='Year of Movie Release', # title of plot
    xaxis_title_text='Release Year', # xaxis label
    yaxis_title_text='Movie Count', # yaxis label
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
)


# Top 20 Movie Gross
gross_df = data_df.nlargest(20,'gross')
fig2 = px.scatter(data_df.nlargest(20,'gross'), x="budget", y='gross', text="name")
fig2.update_traces(textposition='top center')
fig2.update_layout(
    title_text='Top 20 Movie Gross', # title of plot
    xaxis_title_text='Movie Budget', # xaxis label
    yaxis_title_text='Movie Gross', # yaxis label

)


# Top 20 Movie Based on Return On Investment
tmp = []

for index, row in gross_df.iterrows():
    temp = (int(row['gross'])-int(row['budget']))/int(row['budget'])
    tmp.append(temp)
gross_df['ROI'] = tmp

fig3 = px.scatter(gross_df.nlargest(20,'ROI'), x="budget", y='ROI', text="name")
fig3.update_traces(textposition='top center')
fig3.update_layout(
    title_text='Top 20 Movie Based on ROI', # title of plot
    xaxis_title_text='Movie Budget', # xaxis label
    yaxis_title_text='Movie ROI', # yaxis label

)


# Public IMDb Score VS Gross Profit
fig4 = px.scatter(data_df.nlargest(20,'gross'), x="score", y='gross',text="name" ,color="rating")
fig4.update_traces(textposition='top center' )
fig4.update_layout(
    title_text='Public IMDb Score VS Gross Profit', # title of plot
    xaxis_title_text='Movie IMDb Score', # xaxis label
    yaxis_title_text='Movie Gross', # yaxis label

)



# Public IMDb Vote VS Gross Profit
fig5 = px.scatter(data_df, x="votes", y='gross' ,color="rating")
fig5.update_layout(
    title_text='Public IMDb Vote VS Gross Profit', # title of plot
    xaxis_title_text='Movie IMDb Vote', # xaxis label
    yaxis_title_text='Movie Gross', # yaxis label

)

#fig.show()
#fig2.show()
#fig3.show()
#fig4.show()
#fig5.show()

plotly.offline.plot(fig5)