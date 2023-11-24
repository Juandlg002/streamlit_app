import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt


st.title("David Lora")

#Elevator Pitch. Your Branding
st.subheader("One day there won't be any FEMALE LEADERS, just leaders")
col1, col2= st.columns([3,1])
with col1:
    st.subheader("About Me")
    st.text("Passionate about the power of data to drive insights and\ninnovation, I bring a wealth of experience in \nProject Management and Change Management to the world \nof Data Science.")
with col2:
    image = Image.open('asus.jpg')
    st.image(image,width = 250)

#Sidebar w/ Download
st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: juandlg002@gmail.com')
#rb means converting pdf file to raw binary format
pdf_file = open('Aquarium_Tickets.pdf', 'rb')
st.sidebar.download_button('Download Resume',pdf_file,file_name='Resume.pdf',mime='pdf')

tab_skills,tab_exp,tab_pro,tab_cont,tab_pic = st.tabs(['Skills','Experience','Projects','Content Me',"Take a picture"])

with tab_exp:

#Experience
    st.subheader("Relevant Experience")
    experience_table = pd.DataFrame({
            "Job Title":["Data Analyst","Project Specialist","Employer Relations Assistant"],
            "Company":["Sunlife","Sunlife","Laurier"],
            "Job Description":["Providing expertise in data storage structures, data mining, and data cleansing","Collaborated with cross-functional teams to identify areas for process improvement and recommended data-driven solutions, reducing operational costs by 30%.","Meticulously processed 150 job postings/day on the University’s job portal (Navigator)"],
    })
    experience_table = experience_table.set_index('Job Title')
    st.table(experience_table)

with tab_pro:
#Projects GRID
    st.subheader("Projects")
    titanic_data = pd.read_csv('titanic.csv')
    interval = alt.selection_interval()
    scatter = alt.Chart(titanic_data).mark_point().encode(
        x = 'Age',
        y = 'Fare',
        color=alt.condition(interval,'Sex', alt.value('lightgray'))
    ).add_selection(
        interval
        ).properties(
            width=300,height=200)

    bar = alt.Chart(titanic_data).mark_bar().encode(
        x='sum(Survived):Q',
        y='Pclass:N',
        color='Pclass:N',
        ).properties(
            width=300,
            height=200
        ).transform_filter(
            interval
        )
    st.altair_chart(scatter | bar)

with tab_skills:
#Skills Section - In the form of a bar chart

    skill_data = pd.DataFrame(
        {
            "Skills Level":[40,30,80,30],
            "Skills":["Python","Tableau","mySQL","Rstudio"]
        })
    skill_data = skill_data.set_index("Skills")
    with st.container():
        st.subheader("Skills")
        st.bar_chart(skill_data)
    with st.expander("See More Skills"):
        st.write("I have lots of more skills too such as ....")

with tab_cont:

    #Streamlit form
    form = st.form('my_form')
    fullname = form.text_input(label='Enter your full name', value='')
    age = st.slider("Select your age")
    gender = st.radio("Select your gender",('Male','Female','Other'))
    message = form.text_area(label="Your Message", value ='',height=100)
    terms = st.checkbox("Accept terms and conditions")
    submit = form.form_submit_button(label='Submit')
    #Handle form submission
    if submit:
        if terms:
            st.success('Form Completed: Thankyou for visiting')
        else:
            st.error('Please accept the terms and conditions')
    st.write("Name",fullname,"Age: ",age,"Gender: ",gender,"Message",message)

    #Add a map
    # # Create a DataFrame with latitude and longitude columns
    data = {
        'Location': ['Kitchener', 'Waterloo', 'Guelph', 'Cambridge'],
        'LAT': [43.451639, 43.464258, 43.5467, 43.3616],
        'LON': [-80.492533,-80.520410,-80.2482,-80.3144]
    }
    df = pd.DataFrame(data)
    st.map(df)

with tab_pic:

    picture = st.camera_input("Take a pcture with me")
    if picture:
        st.image(picture)
