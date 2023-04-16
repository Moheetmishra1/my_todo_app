import streamlit as st
import functionforpyproject

##streamlit -

todos = functionforpyproject.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+'\n')
    functionforpyproject.write_todos(todos)


st.title("MY Todo APP")
st.subheader("This is my todo APP.")
st.write("This app is to increase your prductivity.")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functionforpyproject.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a todo", placeholder="Add new todo..",
              on_change=add_todo, key='new_todo')


print("Hello") ##very neccessary for security check entry  IP check
