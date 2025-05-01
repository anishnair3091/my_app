with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")
for i, j in zip(user_data.User_id, user_data.Password):    
    if (submit) and (user == i) and (password == j):
        placeholder.empty()
        st.success("Login successful")
        st.switch_page("pages/Monthly_sales.py")
    elif submit and user!=i and password!=j:
        st.rerun()
    else:
        pass



with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")
for i, j, k, l in zip(sales_data.User_id, sales_data.Password, customer_data.User_id, customer_data.Password):    
    if (submit) and (user == i) and (password == j):
        placeholder.empty()
        st.success("Login successful")
        st.switch_page("pages/Monthly_sales.py")
    elif (submit) and (user == k) and (password == l):
        placeholder.empty()
        st.success("Login successful")
        st.switch_page("pages/Tickets.py")
    elif submit and ((user!=i and password!=j) or (user != k and password != l)):
        st.error("Invalid username/password")
    else:
        pass



with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")
for i, j in zip(sales_data.User_id, sales_data.Password):    
    if (submit) and (user == i) and (password == j):
        placeholder.empty()
        st.success("Login successful")
        st.switch_page("pages/Monthly_sales.py")
    
    else:
        pass
for k, l in zip(customer_data.User_id, customer_data.Password):    
    if (submit) and (user == k) and (password == l):
        placeholder.empty()
        st.success("Login successful")
        st.switch_page("pages/Tickets.py")
   
    else:
        pass



with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")
   
if submit and (user in sales_data.User_id) and (password == (sales_data[sales_data['User_id']==user]['Password'])):
    placeholder.empty()
    st.success("Login successful")
    st.switch_page("pages/Monthly_sales.py")

elif submit and (user in customer_data.User_id) and (password == (customer_data[customer_data['User_id']==user]['Password'])):
    placeholder.empty()
    st.success("Login successful")
    st.switch_page("pages/Tickets.py")
elif submit and ((user not in sales_data.User_id) and (password != sales_data[sales_data['User_id']==user]['Password']) or (user not in customer_data.User_id) and (password != customer_data[customer_data['User_id']==user]['Password'])):
    st.error("Invalid username/password")
else:
    pass




    """

chosen_id = stx.tab_bar(data=[
    stx.TabBarItemData(id=1, title="ToDo", description="Tasks to take care of"),
    stx.TabBarItemData(id=2, title="Done", description="Tasks taken care of"),
    stx.TabBarItemData(id=3, title="Overdue", description="Tasks missed out"),
], default=1)







if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title= "Log in", icon=":material/login:")
logout_page= st.Page(logout, title= "Log out", icon=":material/logout:")


Home_sales= st.Page("BMTS_app.py", title= 'Main Page', icon= "🏠")
Tickets= st.Page("Service/Tickets.py", title= 'Service Section', icon= "🗝️")

PhaseWiseSales= st.Page("Sales/Monthly_sales.py", title="Phase Wise Sales", icon="📊")

Forecast= st.Page("Sales/Forecast.py", title="Forecast", icon="📈" )
Employees= st.Page("HR/Employees.py", title='Employees', icon="🧑🏻‍💻" )
Attendance= st.Page("HR/Attendance.py", title='Attendance', icon="🙋🏻‍♂️")
IT_forms= st.Page("IT/IT-forms.py", title= 'IT-forms', icon="🖥️")

if st.session_state.logged_in:
    pg = st.navigation(
        {
        "Service": [Tickets],
        "Sales": [PhaseWiseSales, Forecast],
        "HR": [Employees, Attendance],
        "IT": [IT_forms]
        }
        )



else:
    pg= st.navigation([login_page])


pg.run()


data=pd.read_csv('/Users/anishmnair/Desktop/Streamlit/My_new_app/BMTS-APP/Sales/df_2024.csv')




with col1:
    tab1, tab2 = st.tabs(["Contact", "Sign-in"])
    with tab1:
        st.text("support@bmts.ae\n800BMTS")
    with tab2:
        st.navigation(login_page)



"""