import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff 
import plotly.express as px
import numpy as np  
import datetime
import matplotlib

#Main Page config setup
st.set_page_config(layout='wide', initial_sidebar_state='auto')




#Sidebar header
st.markdown("<h1 style='text-align: left; color : darkblue; font-size : 40px '> BMTS SALES DASHBOARD</h1>",unsafe_allow_html= True)

#Main page subheader
st.markdown('### Statistics')






#Datas loading

data=pd.read_csv('/Users/anishmnair/Desktop/Streamlit/My_new_app/BMTS-APP/Sales/df_2024.csv')

month_targ = pd.read_csv(r'/Users/anishmnair/Desktop/Streamlit/My_new_app/BMTS-APP/Sales/mon_tar.csv')

fms_target= pd.read_csv(r'/Users/anishmnair/Desktop/Streamlit/My_new_app/BMTS-APP/Sales/FMS_target.csv')

actual_data= pd.read_csv(r'/Users/anishmnair/Desktop/Streamlit/My_new_app/BMTS-APP/Sales/actual_data.csv')

#Datas preparing

data_total= data[['Salesperson', 'Month_name', 'Year', 'LPO_Value', 'MaterialValue', 'Installation']].groupby(['Salesperson', 'Month_name', 'Year']).sum().reset_index()

data_total['Salesperson'].replace('SUSAI ANTONY JOHN BOSCO', 'SUSAI', inplace=True)
data_total['Salesperson'].replace('SURAJ RAJAN', 'SURAJ', inplace=True)
data_total['Salesperson'].replace('RAVIKUMAR', 'RAVI', inplace=True)

#Dropping nonrequired salespersons name

data_total.drop([data_total.index[24], data_total.index[61]], inplace=True)

year_total = data_total[['Salesperson', 'Year', 'LPO_Value', 'MaterialValue', 'Installation']].groupby(['Salesperson', 'Year']).sum().reset_index()

po_total= data[['Salesperson', 'Month_name', 'Year', 'LPO_Value']].groupby(['Salesperson', 'Month_name', 'Year']).sum().reset_index()

sales_table= data_total[['Salesperson', 'Month_name', 'LPO_Value']]

month_targ['SalesPerson'] = month_targ['SalesPerson'].str.upper()

month_targ_num= month_targ.select_dtypes(include='number')

month_targ['Total'] = month_targ_num.sum(axis=1)

targ_pivot= month_targ.drop('Total', axis=1).pivot_table(columns='SalesPerson')

data_sum= data_total[['Salesperson', 'Year', 'LPO_Value']].groupby(['Salesperson','Year']).sum()
data_sum.reset_index(inplace=True)


#Converting month names to numbers

month_nums= []
for month in targ_pivot.index:
    month_num= datetime.datetime.strptime(month, '%B').month
    month_nums.append(month_num)

targ_pivot['Month_num']= month_nums

targ_pivot= targ_pivot.sort_values('Month_num', axis= 0, ignore_index= True)

months= []
for month in data_total['Month_name']:
    month_num1= datetime.datetime.strptime(month, '%B').month
    months.append(month_num1)

data_total['Month_num']= months

data_total= data_total.sort_values('Month_num', axis= 0, ignore_index= True)

#Defining functions as required
def monthly_progress(option):
	mp= data_total[data_total['Month_name']== option]['LPO_Value'].sum(axis=0) - month_targ[option].sum(axis=0)
	return mp


def yearly_progress(option2):
	yp= data_total[data_total['Year'] == option2]['LPO_Value'].sum() - month_targ['Total'].sum()
	return yp 	

def sales_year(option2):
	if option3 == None:
		yp= data_total[data_total['Year'] == option2]
		return yp
	else:
		yp1= data_total[(data_total['Year'] == option2) & (data_total['Salesperson'] == option3)]
		return yp1

def sales_total(option2):
	yt= year_total[year_total['Year'] == option2]
	return yt  

def sales_month(option):
	if option2 != None:
		dm = data_total[(data_total['Month_name'] == option) & (data_total['Year'] == option2)]
		return dm
	else:
		dm1 = data_total[data_total['Month_name'] == option]
		return dm1

def sales_table(option):
	if option2 == None:
		st = data_total[data_total['Month_name'] == option]
		return st 
	else:
		st1 = data_total[(data_total['Month_name'] == option) & (data_total['Year']== option2)]
		return st1

def salesperson_mon_progress(option):
	sp= data_total[(data_total['Salesperson'] == option3) & (data_total['Month_name'] == option)]['LPO_Value'].sum()
	sm = month_targ[month_targ['SalesPerson'] == option3][option].sum()
	return sp - sm

def salesperson_mon(option):
	sp= data_total[(data_total['Salesperson'] == option3) & (data_total['Month_name'] == option)]
	return sp  


def salesperson_year_progress(option3):
	sp= data_sum[(data_sum['Salesperson'] == option3) & (data_sum['Year'] == option2)]['LPO_Value'].sum()
	sm = month_targ[month_targ['SalesPerson'] == option3]['Total'].sum()
	c= sp - sm
	return c  

def LPO_month(option):
	if option2!=None:
		po = po_total[(po_total['Month_name'] == option) & (po_total['Year']==option2)]
		return po
	else:
		po1= po_total[po_total['Month_name'] == option]
		return po1

def sunburstchart(option):
	if option == None:
		if option3 == None:
			fig = px.sunburst(sales_total(option2), path=['Salesperson',  'LPO_Value', 'MaterialValue', 'Installation'], values= 'LPO_Value', color= 'LPO_Value', hover_data=['Salesperson'], color_continuous_scale='RdBu', maxdepth=2 )
			return fig  
		else:
			fig1 = px.sunburst(sales_year(option2), path=['Salesperson', 'Month_name', 'LPO_Value', 'MaterialValue', 'Installation'], values= 'LPO_Value', color= 'LPO_Value', hover_data=['Salesperson'], color_continuous_scale='RdBu', maxdepth=2 )
			return fig1
	elif option2 == None:
		if option3 == None:
			fig2 = px.sunburst(sales_month(option), path=['Salesperson', 'Month_name', 'LPO_Value', 'MaterialValue', 'Installation'], values= 'LPO_Value', color= 'LPO_Value', hover_data=['Salesperson'], color_continuous_scale='RdBu', maxdepth=3 )
			return fig2
		else:
			fig3 = px.sunburst(salesperson_mon(option), path=['Salesperson', 'Month_name', 'LPO_Value', 'MaterialValue', 'Installation'], values= 'LPO_Value',  hover_data=['Salesperson'], color_continuous_scale='RdBu', maxdepth=3 )
			return fig3
	else:
		if option3 == None:
			fig4 = px.sunburst(sales_month(option), path=['Salesperson', 'Month_name', 'LPO_Value', 'MaterialValue', 'Installation'], values= 'LPO_Value', color= 'LPO_Value', hover_data=['Salesperson'], color_continuous_scale='RdBu', maxdepth=3 )
			return fig4
		else:	
			fig5 = px.sunburst(salesperson_mon(option), path=['Salesperson', 'Month_name', 'LPO_Value', 'MaterialValue', 'Installation'], values= 'LPO_Value', hover_data=['Salesperson'], color_continuous_scale='RdBu', maxdepth=3 )
			return fig5


def line_figure(option3):
	if option3 != None:
	    data1= data_total[data_total['Salesperson'] == option3]
	    data1['Total_person']= np.cumsum(data1.LPO_Value)
	    data2= targ_pivot[[option3]]
	    data2['Total_person']= np.cumsum(data2[data2.columns[0]])
	    fig, ax= plt.subplots(figsize=(5, 5))
	    label= ['Actual Value', 'Target Value']
	    ax= plt.gca()
	    ax.plot(data1.Month_name, data1.Total_person, color= 'steelblue', label='Actual Value')
	    ax.plot(data2.index, data2.Total_person, color='yellowgreen', linestyle= '--', label='Target Value')
	    ax.set_xlabel('Month')
	    ax.set_ylabel('Sales Total (in Million)')
	    ax.set_xticklabels(labels= data1.Month_name, rotation= 45)
	    matplotlib.rcParams['axes.edgecolor'] = 'none'
	    ax.legend()
	    plt.show()
	    return fig
	else:
		fig, ax= plt.subplots(figsize=(5, 5))
		ax.plot(actual_data.Month_name, actual_data.cum_total, color= 'steelblue', label= 'Actual Value')
		ax.plot(fms_target.Month_name, fms_target.Cum_total, color= 'yellowgreen', linestyle= '--', label= 'Target Value')
		ax.set_xlabel('Month')
		ax.set_ylabel('Sales Total (in Million)')
		ax.set_xticklabels(labels= actual_data.Month_name, rotation= 45)
		matplotlib.rcParams['axes.edgecolor'] = 'none'
		ax.legend()
		plt.show()
		return fig  
    

col1, col2, col3= st.columns(3)
with col1:
	option= st.sidebar.selectbox('Month', options= data['Month_name'].unique(), index= None, placeholder= 'Select the prefered month', label_visibility= 'visible', disabled=False)
with col2:
	option2 = st.sidebar.selectbox('Year', options= data['Year'].unique(), index= None, placeholder= 'Choose the year')
with col3:
	option3= st.sidebar.selectbox('Salesperson', options = data['Salesperson'].unique(), index= None, placeholder='Select the Salesperson')


col1, col2 = st.columns(2, gap='small')


if st.sidebar.button('Submit'):
	if option == None:
		if (option3 == None) & (option2!=None):
			st.write(f'### Total Sales per Salesperson for the year {option2}')
			st.table(sales_total(option2)[['Salesperson', 'LPO_Value']])
			col1.metric('Monthly Progress', value= "None", border= True )
			col2.metric('Yearly Statistics', value= f'{np.around((data_total[data_total['Year'] == option2]['LPO_Value'].sum()/10**6), decimals= 3)} M', delta= f'{np.around((yearly_progress(option2)/10**6), decimals= 3)} M', border=True)
			col4, col5 = st.columns(2, gap= 'large', border=True)
			col4.write(f"#### Bar chart representation of total sales per Salesperson for the year {option2}")
			col4.bar_chart(sales_total(option2), x = 'Salesperson', y= 'LPO_Value', use_container_width=True)
			col5.write(f'#### Sunburst chart representation of total sales per Salesperson for the year {option2}')
			col5.plotly_chart(sunburstchart(option), use_container_width=True)
			st.write(f'#### Achieved value Vs Target Value of year {option2}')
			st.plotly_chart(line_figure(option3))
		elif option2 == None:
			st.sidebar.markdown("<h1 style='text-align: center; color : red; font-size: 15px; '> PLEASE CHOOSE THE MONTH/YEAR OPTIONS 👆🏻 TO PROCEED</h1>", unsafe_allow_html= True)
		else: 
			if (option2 == None) and (option3 ==None):
				st.sidebar.markdown("<h1 style='text-align: center; color : red; font-size: 15px; '> PLEASE CHOOSE THE MONTH/YEAR OPTIONS 👆🏻 TO PROCEED </h1>", unsafe_allow_html= True)
			else:
				st.write(f'### Total Sales per Salesperson {option3} for the year {option2}')
				st.table(sales_year(option2))
				col1.metric('Monthly Progress', value= "None", border= True )
				col2.metric('Yearly Statistics', value= f'{np.around((data_sum[(data_sum['Salesperson'] == option3) & (data_sum['Year'] == option2)]['LPO_Value'].sum()/10**6), decimals= 3)} M', delta= f'{np.around((salesperson_year_progress(option3)/10**6), decimals= 3)} M', border=True)
				col4, col5 = st.columns(2, gap= 'large', border=True)
				col4.write(f"#### Bar chart representation of total sales of sale person Mr. {option3} for the year {option2}")
				col4.bar_chart(sales_year(option2), x = 'Month_name', y= 'LPO_Value', use_container_width= True)
				col5.write(f'#### Sunburst chart representation of total sales of sale person Mr. {option3} for the year {option2}')
				col5.plotly_chart(sunburstchart(option), use_container_width= True)
				st.write(f'#### Achieved value Vs Target Value of {option3}')
				st.plotly_chart(line_figure(option3))

	elif option3 == None:
		if option == None:	
			st.write(f'### Total Sales per Salesperson for the year {option2}')
			st.table(sales_total(option2)[['Salesperson', 'LPO_Value']])
			col1.metric('Monthly Progress', value= "None", border= True )
			col2.metric('Yearly Statistics', value= f'{np.around((data_total[data_total['Year'] == option2]['LPO_Value'].sum()/10**6), decimals= 3)} M', delta= f'{np.around((yearly_progress(option2)/10**6), decimals= 3)} M', border=True)
			col4, col5 = st.columns(2, gap= 'large', border=True)
			col4.write(f"#### Bar chart representation of total sales per Salesperson for the year {option2}")
			col4.bar_chart(sales_total(option2), x = 'Salesperson', y= 'LPO_Value', use_container_width=True)
			col5.write(f'#### Sunburst chart representation of total sales per Salesperson for the year {option2}')
			col5.plotly_chart(sunburstchart(option), use_container_width=True)
			st.write(f'#### Achieved value Vs Target Value of year {option2}')
			st.plotly_chart(line_figure(option3))
		elif option2 == None:
			st.write(f'### Total Sales per Salesperson for the month {option}')
			st.table(sales_table(option).drop('Year', axis=1))
			col1.metric('Monthly Progress', value= f'{np.around(((data_total[data_total['Month_name']== option]['LPO_Value'].sum(axis=0))/10**6), decimals= 3)} M', delta= f'{np.around((monthly_progress(option)/10**6), decimals= 3)} M', border= True )
			col2.metric('Yearly Statistics', value= "None", border=True)
			col4, col5 = st.columns(2, gap= 'large', border=True)
			col4.write(f'#### Bar chart representation of total sales per Salesperson for the month {option}')
			col4.bar_chart(LPO_month(option), x = 'Salesperson', y = 'LPO_Value', use_container_width=True)
			col5.write(f'#### Sunburst chart representation of total sales per Salesperson for the year {option2}')
			col5.plotly_chart(sunburstchart(option), use_container_width=True)
		else:
			if (option == None) & (option2== None):
				st.write('`PLEASE CHOOSE THE OPTIONS ON 👈🏻 TO PROCEED`')
			else:
				st.write(f'### Total Sales per Salesperson for the month {option}')
				st.table(sales_table(option))
				col1.metric('Monthly Progress', value= f'{np.around(((data_total[data_total['Month_name']== option]['LPO_Value'].sum(axis=0))/10**6), decimals= 3)} M', delta= f'{np.around((monthly_progress(option)/10**6), decimals= 3)} M', border= True )
				col2.metric('Yearly Statistics', value= f'{np.around((data_total[data_total['Year'] == option2]['LPO_Value'].sum()/10**6), decimals= 3)} M', delta= f'{np.around((yearly_progress(option2)/10**6), decimals= 3)} M', border=True)
				col4, col5 = st.columns(2, gap= 'large', border=True)
				col4.write(f"#### Bar chart representation of total sales per Salesperson for the month {option}")
				col4.bar_chart(LPO_month(option), x = 'Salesperson', y = 'LPO_Value', use_container_width=True)
				col5.write(f'#### Sunburst chart representation of total sales per Salesperson for the year {option2}')
				col5.plotly_chart(sunburstchart(option), use_container_width= True)
	else: 
		if option2 == None:
			st.write(f'### Total Sales of {option3} for the month {option}')
			st.table(sales_table(option)[sales_table(option)['Salesperson'] == option3])
			col1.metric('Monthly Progress', value= f'{np.around(((data_total[(data_total['Salesperson'] == option3) & (data_total['Month_name'] == option)]['LPO_Value'].sum(axis=0))/10**6), decimals= 3)} M', delta= f'{np.around((salesperson_mon_progress(option)/10**6), decimals= 3)} M', border= True )
			col2.metric('Yearly Statistics', value= "None", border=True)
			col4, col5 = st.columns(2, gap= 'large', border=True)
			col4.write(f'#### Bar chart representation of total sales of  Salesperson Mr. {option3} for the month {option}')
			col4.bar_chart(salesperson_mon(option), x = 'Salesperson', y = ['LPO_Value', 'MaterialValue', 'Installation'], use_container_width=True)
			col5.write(f'#### Sunburst chart representation of total sales of Salesperson Mr. {option3} for the month {option}')
			col5.plotly_chart(sunburstchart(option), use_container_width= True)

		else: 
			st.write(f'### Total Sales of {option3} for the month {option}')
			st.table(sales_table(option)[sales_table(option)['Salesperson'] == option3] )
			col1.metric('Monthly Progress', value= f'{np.around(((data_total[(data_total['Salesperson'] == option3) & (data_total['Month_name'] == option)]['LPO_Value'].sum(axis=0))/10**6), decimals= 3)} M', delta= f'{np.around((salesperson_mon_progress(option)/10**6), decimals= 3)} M', border= True )
			col2.metric('Yearly Statistics', value= f'{np.around((data_sum[(data_sum['Salesperson'] == option3) & (data_sum['Year'] == option2)]['LPO_Value'].sum()/10**6), decimals= 3)} M', delta= f'{np.around((salesperson_year_progress(option3)/10**6), decimals= 3)} M', border=True)
			col4, col5 = st.columns(2, gap= 'large', border=True)
			col4.write(f'#### Bar chart representation of total sales of  Salesperson Mr. {option3} for the month {option}')
			col4.bar_chart(salesperson_mon(option), x = 'Salesperson', y = ['LPO_Value', 'MaterialValue', 'Installation'], use_container_width=True)
			col5.write(f'#### Sunburst chart representation of total sales of  Salesperson Mr. {option3} for the month {option}')
			col5.plotly_chart(sunburstchart(option), use_container_width=True)
	
	
else:
	st.sidebar.write('Please submit')


st.sidebar.markdown('''
	---
	`Created by Anish- Data Scientist`''')
