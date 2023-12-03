import streamlit as st
import pandas as pd
import pydeck as pdk
import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import seaborn as sns
from langchain.llms import Ollama

ollama = Ollama(base_url = 'http://localhost:11434', model = 'llama2')

cor = pd.read_csv('cor.csv')
# Load data
@st.cache_data
def load_data():
    data = pd.read_csv('ces_bay_cleaned.csv')  # replace with the path to your dataset
    data = data.rename(columns={'Latitude':'latitude', 'Longitude':'longitude'})
    return data


def create_heatmap(data, factor):
    # Initialize the map
    m = folium.Map(location=[37.8715, -122.2730], zoom_start=10)  # Adjust the default location and zoom as needed

    # Filter data for positive values in the selected factor
    filtered_data = data[data[factor] > 0][['latitude', 'longitude']]

    # Add heat map layer
    HeatMap(filtered_data).add_to(m)
    return m
def plot_bar_charts(data, factor):
    # for factor in factors:
        st.header(f"Average {factor} Levels by County")
        county_data = data.groupby('California County')[factor].mean().sort_values(ascending=False)
        palette = sns.color_palette("bright", len(county_data))
        plt.figure(figsize=(10, 6))
        sns.barplot(x=county_data.values, y=county_data.index, palette=palette)
        plt.xlabel('Average Level of ' + factor)
        plt.ylabel('California County')
        plt.title(f'Comparison of {factor}')
        st.pyplot(plt)


def create_heatmap_d(data, d):
    # Initialize the map
    m = folium.Map(location=[37.8715, -122.2730], zoom_start=10)  # Adjust the default location and zoom as needed

    # Filter data for positive values in the selected factor
    filtered_data = data[data[d] > 0][['latitude', 'longitude']]

    # Add heat map layer
    HeatMap(filtered_data).add_to(m)
    return m
def plot_bar_disease(data, factor):
    # for factor in factors:
        st.header(f"Average {factor} Levels by County")
        county_data = data.groupby('California County')[factor].mean().sort_values(ascending=False)
        palette = sns.color_palette("bright", len(county_data))
        plt.figure(figsize=(10, 6))
        sns.barplot(x=county_data.values, y=county_data.index, palette=palette)
        plt.xlabel('Average Level of ' + factor)
        plt.ylabel('California County')
        plt.title(f'Comparison of {factor}')
        st.pyplot(plt)
def create_heatmap_d(data, s):
    # Initialize the map
    m = folium.Map(location=[37.8715, -122.2730], zoom_start=10)  # Adjust the default location and zoom as needed

    # Filter data for positive values in the selected factor
    filtered_data = data[data[s] > 0][['latitude', 'longitude']]

    # Add heat map layer
    HeatMap(filtered_data).add_to(m)
    return m
def plot_bar_disease(data, factor):
    # for factor in factors:
        st.header(f"Average {factor} Levels by County")
        county_data = data.groupby('California County')[factor].mean().sort_values(ascending=False)
        palette = sns.color_palette("bright", len(county_data))
        plt.figure(figsize=(10, 6))
        sns.barplot(x=county_data.values, y=county_data.index, palette=palette)
        plt.xlabel('Average Level of ' + factor)
        plt.ylabel('California County')
        plt.title(f'Comparison of {factor}')
        st.pyplot(plt)
def main():
    st.title("Environmental Factors Heatmap")

    # Load data
    data = load_data()

    # Dropdown to select environmental factor
    factor = st.selectbox("Select Environmental Factor", ['Ozone', 'PM2.5', 'Diesel PM', 'Drinking Water', 'Pesticides', 'Tox. Release', 'Traffic', 'Cleanup Sites', 'Groundwater Threats', 'Haz. Waste', 'Imp. Water Bodies', 'Solid Waste'])  
    # Create and display the heatmap
    heatmap = create_heatmap(data, factor)
    folium_static(heatmap)
    st.header("Comparison of " + factor + " Across Counties")
    plot_bar_charts(data, factor)
    st.title("Health factors heatmap")
    d = st.selectbox("Select the disease",['Asthma', 'Low Birth Weight', 'Cardiovascular Disease'])
    heatmap = create_heatmap(data, d)
    folium_static(heatmap)
    st.header("Comparison of " + d + " Across Counties")
    plot_bar_charts(data, d)
    st.title("Social factors heatmap")
    s = st.selectbox("Select the disease",['Education', 'Linguistic Isolation', 'Poverty', 'Unemployment'])
    heatmap = create_heatmap(data, s)
    folium_static(heatmap)
    st.header("Comparison of " + s + " Across Counties")
    plot_bar_charts(data, s)

    image_info = {
        'Asthma_regression_plot.png': 'Asthma Model: With an R-squared of 0.3077, the model suggests that approximately 30.77% of the variability in asthma rates can be explained by the environmental indicators used in the model. However, an MSE of 1203.21 indicates that the models predictions are, on average, 1203.21 units squared away from the actual asthma rates, which suggests that there could be other factors affecting asthma rates that are not captured by this model.',
        'Cardiovascular Disease_regression_plot.png': 'Low Birth Weight Model: The low R-squared of 0.0346 indicates a weak fit; the model explains only 3.46% of the variability in low birth weight rates. This low percentage suggests that other variables not included in the model or non-linear relationships might be more influential in predicting low birth weight.',
        'Low Birth Weight_regression_plot.png': 'Cardiovascular Disease Model: An R-squared of 0.3257 indicates a moderate fit, where about 32.57% of the variability in cardiovascular disease rates can be explained by the environmental indicators. The MSE of 10.51 is the average squared prediction error, which, while not perfect, indicates that the model has some predictive power.',
        # Add more images and their descriptions here
    }

    # Dropdown to select an image
    selected_image = st.selectbox("Choose an image", list(image_info.keys()))

    # Display the selected image and its description
    st.title('Regression Analysis')
    image_path = f'{selected_image}'  # Replace with your image directory path
    st.image(image_path, use_column_width=True)
    st.write(image_info[selected_image])  # Display the description
    st.header("Correlation between environmental factors and health outcomes")
    st.image('E-H.png',use_column_width=True )
    st.write(cor)
    st.write('''
The categorized results from the correlation analysis tell us the strength of the linear relationship between each environmental variable and the health outcomes of interest.

##### Asthma:
PM2.5 and Drinking Water have a strong correlation with asthma rates. This suggests that areas with higher particulate matter (PM2.5) or poor drinking water quality might see higher rates of asthma.
Diesel PM, Tox. Release, Groundwater Threats, and Imp. Water Bodies have a moderate correlation with asthma. This implies that these environmental factors could have a noticeable but less intense impact on asthma rates compared to PM2.5 and drinking water quality.
Ozone and other variables have a weak correlation with asthma, indicating a less clear or more negligible relationship.

##### Low Birth Weight:
All environmental variables have been categorized as having a weak correlation with low birth weight rates. This means that there isn't a strong linear relationship between these specific environmental factors and low birth weight according to the data provided. Other factors not included in the analysis might be more influential.

##### Cardiovascular Disease:
Ozone has a strong correlation with cardiovascular disease rates, suggesting a significant relationship where areas with higher levels of ozone might have higher rates of cardiovascular disease.
Toxic Release shows a moderate correlation, indicating a potential moderate impact on cardiovascular disease rates.
The rest of the environmental variables have a weak correlation with cardiovascular disease, indicating less influence based on the linear correlation coefficient alone.


Furthermore, the impact of an environmental variable on health can be complex and influenced by many other factors, such as genetics, lifestyle, access to healthcare, and socioeconomic status, but the results above point to direct correlation between severe health coditions and environmental variables
''')
    grouped_data = data.groupby('California County').agg({
        'Total Population': 'sum',
        'Poverty': 'mean',
        'Unemployment': 'mean',
        'Ozone': 'mean',
        'PM2.5': 'mean',
        'Diesel PM': 'mean',
        'Drinking Water': 'mean',
        'Lead': 'mean',
        'Pesticides': 'mean',
        'Tox. Release': 'mean',
        'Traffic': 'mean',
        'Cleanup Sites': 'mean',
        'Groundwater Threats': 'mean',
        'Haz. Waste': 'mean',
        'Imp. Water Bodies': 'mean',
        'Solid Waste': 'mean',
        'Pollution Burden': 'mean',
        'Asthma': 'mean',
        'Low Birth Weight': 'mean',
        'Cardiovascular Disease': 'mean',
        'Education': 'mean',
        'Linguistic Isolation': 'mean',
        'Poverty': 'mean',
        'Unemployment': 'mean',
        'Housing Burden': 'mean',
    })

    grouped_data.reset_index(inplace=True)
    grouped_data_string = grouped_data.to_string(header=False, index=False, index_names=False).replace('\n', ' ')

    st.title('Query bot:')
    prompt = st.text_input('Enter your about')
    st.write(ollama(prompt + grouped_data_string) + 'based only on this data')

if __name__ == "__main__":
    main()