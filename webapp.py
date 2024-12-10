import streamlit as st
import functions

st.title("My Todo App")
#st.subheader("Example of Subheader")
#st.write("Example of text")

todos=functions.get_date()

def add_todo():
    todo=st.session_state["new_todo"] +'\n'
    todos.append(todo)
    functions.write_data(todos)

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_data(todos)
        st.rerun()


st.text_input(label="Todo",placeholder="add new todo",on_change=add_todo,key='new_todo')