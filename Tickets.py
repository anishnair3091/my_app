import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from st_on_hover_tabs import on_hover_tabs 
import time
from rembg import remove
import extra_streamlit_components as stx  


data=pd.read_csv('/Users/anishmnair/Desktop/Streamlit/My_new_app/BMTS-APP/Service.data_edtd.csv')

st.set_page_config(layout='wide', initial_sidebar_state='auto')

st.markdown('<style>' + open('/Users/anishmnair/Desktop/Streamlit/My_new_app/style.css').read() + '</style>', unsafe_allow_html=True)

i = 244 

troubles= pd.read_csv(r'/Users/anishmnair/Desktop/Streamlit/My_new_app/BMTS-APP/Service/troubles.csv')

troubles = troubles.iloc[:, 1:]

pics= pd.read_csv(r'/Users/anishmnair/Desktop/Streamlit/My_new_app/BMTS-APP/Service/Salesperson_pics.csv', skiprows=1)

pics.dropna(axis=1, inplace=True)

history_data= pd.read_csv(r'/Users/anishmnair/Desktop/Streamlit/My_new_app/BMTS-APP/Service/History.csv')



def project_name(option1):

	data1= data[data['Customer'] == option1]
	project_name= data1['Project'].unique()
	return project_name
	
def systems_name(option2):
	data1 = data[data['Project'] == option2]
	systems_name= data1['Systems'].unique()
	return systems_name

def troubles_name(option3):
	troubles_type = []
	data1= troubles[troubles['Systems'] == option3]
	Troubles= data1['troubles'].unique()
	for trouble in Troubles:
		trouble_type = trouble.split(", ")
		return trouble_type

def team_assign(option2):
	data1 = data[data['Project'] == option2]
	for team in data1.Salesperson:
		person = team 
		return person  	



def team_image(option2):
    data1 = data[data['Project'] == option2]
    teams = data1.Salesperson
    for team in teams.unique():
        data2= pics[pics['Salesperson'] == team]
        pic_link = data2['IMAGE'].values
        for link in pic_link:
            image= Image.open(link)
            output = remove(image)
            return output

def team_desig(option2):
    data1 = data[data['Project'] == option2]
    teams = data1.Salesperson
    for team in teams.unique():
        data2 = pics[pics['Salesperson']==team]
        for des in data2['Designation']:            
            designation= des
        return designation

def team_contact(option2):
    data1 = data[data['Project'] == option2]
    teams = data1.Salesperson
    for team in teams.unique():
        data2 = pics[pics['Salesperson']==team]
        for con in data2['Contact']:
            contact= con
        return contact

def team_email(option2):
    data1 = data[data['Project'] == option2]
    teams = data1.Salesperson
    for team in teams.unique():
        data2 = pics[pics['Salesperson']==team]
        for em in data2['Email id']:
            email= em
        return email

def input_features():

	data = {'Organization': option1, 'Project': option2, 'System': option3, 'Troubles_Name': option4, 'Service_Person': team_assign(option2), 'Ticket ref': f'BMTS/Ser/Tic/{i}'

	} 
	history = pd.DataFrame(data, index=[0])
	return history 



with st.sidebar:
    tabs = on_hover_tabs(tabName=['Create Tickets', 'View tickets'], 
                         iconName=['create', 'economy'], default_choice=0)

if tabs =='Create Tickets':
	st.title("Create Tickets")
	
	with st.form('Service tickets'):
	    col1, col2 = st.columns(2, border=False, gap= 'large')
	    with col1:
	        option1= st.selectbox('Organization name:', options= data.Customer.unique(), index= None, placeholder= 'Select the Organization name and press submit')
	        option2= st.selectbox('Project name:', options= project_name(option1), index=None, placeholder= 'Select the project name')
	        option3= st.selectbox('System type:', options= systems_name(option2), index=None, placeholder= 'Select the system name')
	        option4 =st.selectbox('Troubles name:', options= troubles_name(option3), index= None, placeholder= 'Select the trouble name')
	        submitted= st.form_submit_button('Submit')
	        if submitted:
	        	if (option4!=None):
	        		progress_text = "Ticket creation in progress. Please wait."
	        		my_bar = st.progress(0, text=progress_text)
	        		for percent_complete in range(100):
	        			time.sleep(0.01)
	        			my_bar.progress(percent_complete + 1, text=progress_text)
	        		time.sleep(1)
	        		my_bar.empty()
	        		
	        		st.success('The ticket is created. You can view the status on right shortly', icon="✅")
	        		i = i + 1 
	        		time.sleep(2)
	        		with col2:
	        			row1= st.columns(1)
	        			for col in row1:
	        				container= col.container(height= 50, border=False)
		        			container.write(f'The ticket is assigned to Mr. {team_assign(option2)}')
	        			col1, col2= st.columns([.25, .75])
        				with col1:
        					container= st.container(height= 150, border=False)
		        			container.image(team_image(option2), output_format= 'auto', use_container_width=True)
		        		with col2:
		        			container= st.container(height= 100, border=False)
		        			container.text(f'{team_desig(option2)}\n{team_contact(option2)}\n{team_email(option2)}')


	        			
	        		

elif tabs == 'View tickets':
	st.title("View Tickets")
	st.write('Name of option is {}'.format(tabs))

input_data= input_features()

history_data = pd.concat([history_data, input_data], axis= 0)

history_data.to_csv('/Users/anishmnair/Desktop/Streamlit/My_new_app/BMTS-APP/Service/History.csv', index= False)