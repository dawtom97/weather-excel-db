import pandas as pd
import random
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_excel("pogoda_rozszerzona.xlsx")

# Konwersja timestamp na datetime
df["timestamp_dt"] = pd.to_datetime(
    df["timestamp"],
    format="%H:%M:%S %d-%m-%Y"
)

# Sortowanie po timnestamp
df = df.sort_values("timestamp_dt")


# fig = px.scatter(
#     df,
#     x="temp",
#     y="humidity",
#     title="Temp. vs wilgotność",
#     labels={"temp":"Temp. C", "humidity": "Wilgotność %"}
# )
#
# fig.show()

city = "Toronto"
sub = df[df["place"] == city].sort_values("timestamp_dt")

fig = px.line(
    sub,
    x="timestamp_dt",
    y="temp"
)
fig.show()





# PLOTLY

# Wykres kołowy

# fig = px.pie(
#     data_frame=df,
#     names="description",
#     title="Udział typów pogody"
# )
# fig.show()

# Wykres słupkowy

# fig = px.bar(
#     data_frame=df,
#     x="place",
#     title="Liczba obserwacji w miastach"
# )
#
# fig.update_layout(
#     xaxis_title="Miasto",
#     yaxis_title="Liczba rekordów",
# )
#
# fig.show()

# podstawowy wykres
# fig = px.bar(
#     data_frame=df,
#     x="place",
#     title="Liczba obserwacji w miastach",
#     color="place",  # różne kolory dla miast
#     color_discrete_sequence=["#FF6B6B", "#4ECDC4", "#1A535C", "#FFBE0B", "#8338EC"]
# )
#
# # styl słupków
# fig.update_traces(
#     marker=dict(
#         line=dict(width=2, color="black"),  # obramowanie
#         opacity=0.9
#     ),
#     texttemplate='%{y}',        # wyświetlanie wartości nad słupkami
#     textposition='outside'
# )
#
# # styl layoutu
# fig.update_layout(
#     xaxis_title="Miasto",
#     yaxis_title="Liczba rekordów",
#     template="simple_white",     # jasny elegancki motyw
#     font=dict(
#         family="Arial",
#         size=14,
#         color="black"
#     ),
#     plot_bgcolor="white",
#     paper_bgcolor="white",
#     margin=dict(l=40, r=40, t=60, b=40)
# )
#
# # styl osi
# fig.update_xaxes(
#     tickangle=45,
#     showgrid=True,
#     gridcolor="#E0E0E0"
# )
#
# fig.update_yaxes(
#     showgrid=True,
#     gridcolor="#E0E0E0",
#     rangemode="tozero"
# )
#
# fig.show()
#

# print(df["temp"])

# Wykres punktowy: temp. vs wilgotność
# plt.figure()
# plt.scatter(df["temp"], df["humidity"])
# plt.title("Temp. vs wilgotność")
# plt.xlabel("Temp. w C")
# plt.ylabel("Wilgotność w %")
#
# plt.xlim(-30,50)
# plt.ylim(0,100)
# plt.show()

# Histogram rozkładu temperatur
# plt.figure()
# # wyciąganie wartości y, x i informacji o słupkach
# y_values, x_values, patches = plt.hist(df['temp'])
# plt.xlabel("Temperatura")
# plt.ylabel("Liczba obserwacji")
# plt.title("Rozkład temperatur")
# plt.ylim(0,20)
#
# print(y_values, x_values, patches)
# for p in patches:
#     p.set_facecolor((random.random(), random.random(), random.random()))
#
# plt.show()


# Wykres pudełkowy - temperatury wg. miasta
# top_cities = df["place"].value_counts().head(5).index
#
# # wybór wierszy, które mają jedno z 5 miast w wartościach place
# subset = df[ df["place"].isin(top_cities) ]
# # wypis wszystkich wierszy (:) i tylko kolumny "place
# # print(subset.loc[:, ["place"]])
#
# data_for_box = [
#     subset[subset["place"] == city]["temp"]
#     for city in top_cities
# ]
#
# plt.figure()
# plt.boxplot(data_for_box, labels=top_cities)
# plt.show()


# Temperatura i temp. odczuwalna, w czasie dla jednego miasta
# city = "Lisbon"
# city_df = df[df["place"] == city]
#
# plt.figure()
# plt.plot(city_df["timestamp_dt"], city_df["temp"], label="Temperatura")
# plt.plot(city_df["timestamp_dt"], city_df["temp_feels_like"], label="Odczuwalna")
#
# plt.legend()
#
# plt.title(f"Temperatura w czasie - {city}")
#
# plt.show()

# Średnia temperatura w miastach - wykres słupkowy

# mean_temp = df.groupby("place")["temp"].mean().sort_values()
#
# plt.figure()
# plt.bar(mean_temp.index, mean_temp.values)
# plt.ylim(-20,50)
#
# plt.show()



# 1. Utwórz wykres słupkowy, gdzie pokażesz średnią wilgotność w miastach
# 2. Utwórz wykres liniowy, gdzie pokazujesz prędkość wiatru w Toronto na przestrzeni czasu
# 3. Opcjonalnie - spróbuj wprowadzić wyglądy do wykresów











