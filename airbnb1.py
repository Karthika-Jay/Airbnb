import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import folium
from folium.plugins import MarkerCluster


# Streamlit part
st.set_page_config(layout= "wide")

st.image("C:/Users/lenovo/Desktop/try/airbnb/Airbnb_Logo.png", use_column_width=True)

st.write("")

def datafr():
    df= pd.read_csv("C:/Users/lenovo/Desktop/try/airbnb/Airbnb.csv")
    return df

df= datafr()
logo_path = "C:/Users/lenovo/Desktop/try/airbnb/Airbnb_Logo.png"

with st.sidebar:
    st.image(logo_path, use_column_width=True)
    # Add the CSS styles for the bouncing animation
    st.markdown(
        """
        <style>
        @keyframes bounce {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-10px);
            }
        }
        .bounce {
            animation: bounce 1s infinite;
            color: #800080;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add the "Hi!" text with the bouncing animation to the sidebar
    st.sidebar.markdown(
        "<div class='bounce'>Hello there 👋, choose something:</div>",
        unsafe_allow_html=True
    )
    select= st.radio("", ["Introduction Page📌","Airbnb Analysis 📈","Project summary📚"])

if select == "Introduction Page📌":
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-color: #FFC080;
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: local;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)



    st.markdown("<div style='background-color:#FF0000;padding:10px;'><h1 style='color:white;'>AIR BED AND BREAKFAST DATA ANALYSIS</h1></div>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    # Define the URLs for the buttons
    urls = {
        "⛪AIRBNB HOME": "https://www.airbnb.co.in/host/homes",
        "🏩AIRBNB STAYS": "https://www.airbnb.co.in/?category_tag=Tag%3A8851",
        "📱ONLINE EXPERIENCES": "https://www.airbnb.co.in/s/experiences/online",
        "🔍BROWSE ICONS": "https://www.airbnb.co.in/release",
        "📞HELP CENTRE": "https://www.airbnb.co.in/help",
        "☎ CONTACT": "https://news.airbnb.com/contact/"
    }


    # Create a button for each URL
    button_cols = st.columns(6)
    for i, (label, url) in enumerate(urls.items()):
        with button_cols[i]:
            if st.button(label):
                st.markdown(f"[{label}]({url})", unsafe_allow_html=True)
    st.image("C:/Users/lenovo/Desktop/try/airbnb/icon.jpg", use_column_width=True)
    st.header("**AIRBNB**")
    st.image("C:/Users/lenovo/Desktop/try/airbnb/head.jpg")
    st.write("")
    st.write('''Founding and Growth: Airbnb was founded in August 2008 by Brian Chesky, Joe Gebbia, and Nathan Blecharczyk in San Francisco, California. It started as a way for hosts to rent out their space to guests looking for short-term accommodations.

Global Reach: Airbnb operates in over 220 countries and regions worldwide, with millions of listings ranging from apartments and houses to unique properties like castles and houseboats.

Community and Trust: The platform emphasizes community and trust through its review system, where both hosts and guests can leave reviews based on their experiences. This helps build credibility and transparency within the Airbnb community.

Experiences and Activities: In addition to accommodations, Airbnb offers "Experiences" where locals can host activities, tours, and workshops for travelers, providing unique cultural experiences.

Impact on Hospitality: Airbnb has disrupted the traditional hospitality industry by offering a more personalized and often more affordable alternative to hotels. It has expanded accommodation options for travelers and enabled hosts to generate income from their properties.

Technology and Innovation: Airbnb has leveraged technology to create a user-friendly platform for both hosts and guests, facilitating easy booking, payment processing, and communication.

Regulation and Challenges: The rapid growth of Airbnb has posed challenges related to regulations in various cities and concerns about its impact on local housing markets and communities.

Financial Impact: Airbnb has experienced significant financial success, with a successful IPO in December 2020 that highlighted its valuation and market position.''')
    st.write("")
    
    st.header("Newsroom")
    st.image("C:/Users/lenovo/Desktop/try/airbnb/news.jpg", use_column_width=True)
    st.write("")
    st.write('Airbnb was born in 2007 when two hosts welcomed three guests to their San Francisco home, and has since grown to over 5 million hosts who have welcomed over 1.5 billion guest arrivals in almost every country across the globe. Every day, hosts offer unique stays and experiences that make it possible for guests to connect with communities in a more authentic way.')
    st.write("")
    st.write("")
    st.image("C:/Users/lenovo/Desktop/try/airbnb/facts.jpg", use_column_width=True)
    st.write("")
    st.write("")
    st.image("C:/Users/lenovo/Desktop/try/airbnb/founder.jpg", use_column_width=True)
    st.write("")
    st.write("")
    # Load the image
    st.image('C:/Users/lenovo/Desktop/try/airbnb/Visual.jpg', use_column_width=True)

if select == "Airbnb Analysis 📈":
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-color: #ADD8E6;
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: local;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    tab = st.selectbox("**📊Analysis tabs📈**", ["Select Tab for Analysis","💰 Price Analysis", "✅ Availability Analysis", "📍 Location Analysis", "🌎 Geospatial Visualization", "📈 Top Charts"])
    # Customize the appearance of the tabs using CSS
    if tab == "Select Tab for Analysis":
        st.image("C:/Users/lenovo/Desktop/try/airbnb/mr-bean-bean.gif")
    elif tab == "💰 Price Analysis":
        
        st.toast("Selected Tab: " + tab, icon="💰")

        
        col1,col2= st.columns(2)

        with col1:
            
            
            country= st.selectbox("Select the Country🏳‍🌈",df["country"].unique())

            df1= df[df["country"] == country]
            df1.reset_index(drop= True, inplace= True)

            room_ty= st.radio("choose the Room Type🏨",df1["room_type"].unique())
            
            df2= df1[df1["room_type"] == room_ty]
            df2.reset_index(drop= True, inplace= True)

            df_bar= pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
            df_bar.reset_index(inplace= True)

            # Pie chart for Price distribution across Property Types
            fig_bar= px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY_TYPES",hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
            st.plotly_chart(fig_bar)

        
        with col2:
            
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
     
            proper_ty= st.selectbox("choose the Property type⛪",df2["property_type"].unique())

            df4= df2[df2["property_type"] == proper_ty]
            df4.reset_index(drop= True, inplace= True)

            df_pie= pd.DataFrame(df4.groupby("host_response_time")[["price","bedrooms"]].sum())
            df_pie.reset_index(inplace= True)

            fig_bar = px.bar(df_pie, x="host_response_time", y="price",
                     hover_data=["bedrooms"],
                     title="Price Difference Based on Host Response Time",
                     color_discrete_sequence=px.colors.sequential.BuPu_r,
                     width=600, height=500)
            st.plotly_chart(fig_bar)

        col1,col2= st.columns(2)

        with col1:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            
            hostresponsetime= st.selectbox("choose the host response time",df4["host_response_time"].unique())

            df5= df4[df4["host_response_time"] == hostresponsetime]

            df_do_bar= pd.DataFrame(df5.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
            df_do_bar.reset_index(inplace= True)

            fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
            title='MINIMUM NIGHTS AND MAXIMUM NIGHTS',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow, width=600, height=500)
            

            st.plotly_chart(fig_do_bar)

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_do_bar_2= pd.DataFrame(df5.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
            df_do_bar_2.reset_index(inplace= True)

            fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
            title='BEDROOMS AND BEDS ACCOMMODATES',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r, width= 600, height= 500)
           
            st.plotly_chart(fig_do_bar_2)

    elif tab == "✅ Availability Analysis":
        st.toast("Selected Tab: " + tab, icon="✅")

        def datafr():
            df_a= pd.read_csv("C:/Users/lenovo/Desktop/try/airbnb/Airbnb.csv")
            return df_a

        df_a= datafr()

        col1,col2= st.columns(2)

        with col1:
            
            
            country_a= st.selectbox("Select the Country 🏳‍🌈 (availability)",df_a["country"].unique())

            df1_a= df[df["country"] == country_a]
            df1_a.reset_index(drop= True, inplace= True)

            property_ty_a= st.selectbox("Choose the Property Type⛪",df1_a["property_type"].unique())
            
            df2_a= df1_a[df1_a["property_type"] == property_ty_a]
            df2_a.reset_index(drop= True, inplace= True)

            df_a_sunb_30= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_30",width=600,height=500,title="AVAILABILITY_30",color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_a_sunb_30)
        
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            

            df_a_sunb_60= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_60",width=600,height=500,title="AVAILABILITY_60",color_discrete_sequence=px.colors.sequential.Blues_r)
            st.plotly_chart(df_a_sunb_60)

        col1,col2= st.columns(2)

        with col1:
            
            df_a_sunb_90= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_90",width=600,height=500,title="AVAILABILITY_90",color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
            st.plotly_chart(df_a_sunb_90)

        with col2:

            df_a_sunb_365= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_365",width=600,height=500,title="AVAILABILITY_365",color_discrete_sequence=px.colors.sequential.Greens_r)
            st.plotly_chart(df_a_sunb_365)
        
        roomtype_a= st.radio("Pick the Room Type availability🏨", df2_a["room_type"].unique())

        df3_a= df2_a[df2_a["room_type"] == roomtype_a]

        df_mul_bar_a= pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].sum())
        df_mul_bar_a.reset_index(inplace= True)

        fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
                         title='AVAILABILITY BASED ON HOST RESPONSE TIME', hover_data="price",
                         barmode='group', color_discrete_sequence=px.colors.sequential.PuBuGn_r, width=1000)

        st.plotly_chart(fig_df_mul_bar_a)


    elif tab == "📍 Location Analysis":
        st.toast("Selected Tab: " + tab, icon="📍")

        st.write("")

        def datafr():
            df= pd.read_csv("C:/Users/lenovo/Desktop/try/airbnb/Airbnb.csv")
            return df

        df_l= datafr()

        country_l= st.selectbox("Select the Country🏳‍🌈(location)",df_l["country"].unique())

        df1_l= df_l[df_l["country"] == country_l]
        df1_l.reset_index(drop= True, inplace= True)

        proper_ty_l= st.selectbox("choose the Property type(location)⛪",df1_l["property_type"].unique())

        df2_l= df1_l[df1_l["property_type"] == proper_ty_l]
        df2_l.reset_index(drop= True, inplace= True)

        st.write("")

        def select_the_df(sel_val):
            if sel_val == str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"):

                df_val_30= df2_l[df2_l["price"] <= differ_max_min*0.30 + df2_l['price'].min()]
                df_val_30.reset_index(drop= True, inplace= True)
                return df_val_30

            elif sel_val == str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"):
            
                df_val_60= df2_l[df2_l["price"] >= differ_max_min*0.30 + df2_l['price'].min()]
                df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df2_l['price'].min()]
                df_val_60_1.reset_index(drop= True, inplace= True)
                return df_val_60_1
            
            elif sel_val == str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)"):

                df_val_100= df2_l[df2_l["price"] >= differ_max_min*0.60 + df2_l['price'].min()]
                df_val_100.reset_index(drop= True, inplace= True)
                return df_val_100
            
        differ_max_min= df2_l['price'].max()-df2_l['price'].min()

        val_sel= st.selectbox("**Select the Price Range**",[str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"),
                                                    
                                                    str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"),

                                                    str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)")])
                                          
        df_val_sel= select_the_df(val_sel)

        st.dataframe(df_val_sel)

        # checking the correlation

        df_val_sel_corr= df_val_sel.drop(columns=["listing_url","name", "property_type",                 
                                            "room_type", "bed_type","cancellation_policy",
                                            "images","host_url","host_name", "host_location",                   
                                            "host_response_time", "host_thumbnail_url",            
                                            "host_response_rate","host_is_superhost","host_has_profile_pic" ,         
                                            "host_picture_url","host_neighbourhood",
                                            "host_identity_verified","host_verifications",
                                            "street", "suburb", "government_area", "market",                        
                                            "country", "country_code","location_type","is_location_exact",
                                            "amenities"]).corr()
        
        st.dataframe(df_val_sel_corr)

        df_val_sel_gr= pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
        df_val_sel_gr.reset_index(inplace= True)

        fig_1= px.bar(df_val_sel_gr, x="accommodates", y= ["cleaning_fee","bedrooms","beds"], title="ACCOMMODATES",
                    hover_data= "extra_people", barmode='group', color_discrete_sequence=px.colors.sequential.Inferno_r,width=1000)
        st.plotly_chart(fig_1)
        
        
        room_ty_l= st.radio("Select the Room_Type(location)🏨", df_val_sel["room_type"].unique())

        df_val_sel_rt= df_val_sel[df_val_sel["room_type"] == room_ty_l]

        fig_2= px.bar(df_val_sel_rt, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
             hover_data= ["name","host_name","market"], color_discrete_sequence=px.colors.sequential.Inferno_r,width=1000, error_y="market")
        st.plotly_chart(fig_2)


        
        fig_3= px.bar(df_val_sel_rt, x="government_area", y= ["host_is_superhost","host_neighbourhood","cancellation_policy"], title="GOVERNMENT_AREA",
                    hover_data= ["guests_included","location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Inferno_r,width=1000)
        st.plotly_chart(fig_3)


    elif tab == "🌎 Geospatial Visualization":
        st.toast("Selected Tab: " + tab, icon="🌎")
        
        st.write("")

        fig_4 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', size='accommodates',
                        color_continuous_scale="YlGnBu",hover_name='name',range_color=(0,49000), mapbox_style="open-street-map",
                        zoom=1)

        fig_4.update_layout(width=1150,height=800,title={'text': '🗺 GEOSPATIAL DISTRIBUTION FOR LISTINGS', 'font_color': 'blue'})
        st.plotly_chart(fig_4)


    elif tab == "📈 Top Charts":
        st.toast("Selected Tab: " + tab, icon="📈")

        country_t= st.selectbox("Select the Country_top_chart 🏳‍🌈",df["country"].unique())

        df1_t= df[df["country"] == country_t]

        property_ty_t= st.selectbox("Select the Property_type_top_chart⛪",df1_t["property_type"].unique())

        df2_t= df1_t[df1_t["property_type"] == property_ty_t]
        df2_t.reset_index(drop= True, inplace= True)

        df2_t_sorted= df2_t.sort_values(by="price")
        df2_t_sorted.reset_index(drop= True, inplace= True)


        df_price= pd.DataFrame(df2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        df_price.reset_index(inplace= True)
        df_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
        
        col1, col2= st.columns(2)

        with col1:
            
            fig_price = px.line(df_price, x="Total_price", y="host_neighbourhood", title="PRICE BASED ON HOST_NEIGHBOURHOOD", width=600, height=800)
            st.plotly_chart(fig_price)


        with col2:

            fig_price_2= px.line(df_price, x= "Avarage_price", y= "host_neighbourhood", title= "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",width= 600, height= 800)
            st.plotly_chart(fig_price_2)


        col1, col2= st.columns(2)

        with col1:

            df_price_1= pd.DataFrame(df2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
            df_price_1.reset_index(inplace= True)
            df_price_1.columns= ["host_location", "Total_price", "Avarage_price"]
            
            fig_price_3= px.line(df_price_1, x= "Total_price", y= "host_location", title= "PRICE BASED ON HOST_LOCATION",width= 600, height= 800, color_discrete_sequence=px.colors.sequential.Bluered_r)
            st.plotly_chart(fig_price_3)


        with col2:

            fig_price_4= px.line(df_price_1, x= "Avarage_price", y= "host_location", title= "AVERAGE PRICE BASED ON HOST_LOCATION",width= 600, height= 800, color_discrete_sequence=px.colors.sequential.Bluered_r)
            st.plotly_chart(fig_price_4)



        room_type_t= st.radio("Select the Room_Type_top_chart🏨",df2_t_sorted["room_type"].unique())

        df3_t= df2_t_sorted[df2_t_sorted["room_type"] == room_type_t]

        df3_t_sorted_price= df3_t.sort_values(by= "price")

        df3_t_sorted_price.reset_index(drop= True, inplace = True)

        df3_top_50_price= df3_t_sorted_price.head(100)

        fig_top_50_price_1= px.bar(df3_top_50_price, x= "name",  y= "price" ,color= "price",
                                 color_continuous_scale= "PuBuGn",
                                range_color=(0,df3_top_50_price["price"].max()),
                                title= "MINIMUM_NIGHTS MAXIMUM_NIGHTS AND ACCOMMODATES",
                                width=1200, height= 800,
                                hover_data= ["minimum_nights","maximum_nights","accommodates"])
        
        st.plotly_chart(fig_top_50_price_1)

        fig_top_50_price_2= px.bar(df3_top_50_price, x= "name",  y= "price",color= "price",
                                 color_continuous_scale= "OrRd",
                                 title= "BEDROOMS, BEDS, ACCOMMODATES AND BED_TYPE",
                                range_color=(0,df3_top_50_price["price"].max()),
                                width=1200, height= 800,
                                hover_data= ["accommodates","bedrooms","beds","bed_type"])

        st.plotly_chart(fig_top_50_price_2)
        st.balloons()
if select == "Project summary📚":
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-color: #C5C3C5;
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: local;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.header(":red[📝SUMMARY]")

    st.subheader(":blue[Airbnb Analysis]")

    st.write('''The "Airbnb Analysis" project focuses on leveraging MongoDB Atlas for data storage and retrieval to analyze Airbnb data. It involves Python scripting, data preprocessing, visualization, exploratory data analysis (EDA), Streamlit for web application development, and potentially Power BI or Tableau for dashboard creation. The domain of interest spans the travel industry, property management, and tourism.''')
    st.subheader(":orange[Project Summary:]")
    
    st.write('''
Objective: 
Analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.

**Key Components:**

MongoDB Setup: Establish a MongoDB Atlas account, set up a cluster, and import sample Airbnb data into the database.

Data Handling: Retrieve data from MongoDB, clean and preprocess it to address missing values, duplicates, and ensure data consistency.

**Visualization and Analysis:**

Geospatial Visualization: Develop a Streamlit web app with interactive maps to visualize Airbnb listing distributions, prices, ratings, and more.

Price Analysis: Explore price variations across locations, property types, and seasons using dynamic plots and charts.

Availability Patterns: Analyze occupancy rates and demand fluctuations throughout the year.

Location-Based Insights: Extract and visualize data for specific regions or neighborhoods to uncover local trends.
             
Interactive Tools: Implement interactive visualizations that allow users to filter and explore data dynamically based on their preferences.

Dashboard Creation: Build a comprehensive dashboard using Tableau or Power BI to consolidate key insights from the analysis, presenting findings in a clear and actionable format.''')
    
    st.snow()