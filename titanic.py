import streamlit
import pandas
import time


@streamlit.cache_data()
def load_data():
    with streamlit.spinner():
        time.sleep(10)
        url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
        return pandas.read_csv(url)

streamlit.write("# Titanic (lo de siempre)")

df = None

df = load_data()

streamlit.write(df.head())

sex = streamlit.selectbox("Sex", ["male", "female"])
pclass = streamlit.radio("Pclass", [1, 2, 3])
age_range = streamlit.slider(
    'Select a range of values',
    0,
    int(max(df['Age'].values)),
    value=(0, int(max(df['Age'].values))),
    step=1
)

sex_label = {
    "male": "Hombre",
    "female": "Mujer",
}
pclass_label = {
    1: "Primera",
    2: "Segunda",
    3: "Tercera",
}
min_age, max_age = age_range

mask = (
    (df.Pclass == pclass)
    & (df.Sex == sex)
    & (df.Age >= min_age)
    & (df.Age <= max_age)
)
survived_mask = mask & (df.Survived == 1)
probability = sum(survived_mask) / sum(mask) * 100

streamlit.write(
    f"Si yo hubiese sido sido **{sex_label[sex]}** en **{pclass_label[pclass]}** clase con una edad entre {min_age} y {max_age} años, la probabilidad de sobrevivir hubiese sido: {probability:.2f} %"
)
