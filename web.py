import streamlit as st
import functions as func

FILEPATH = 'todos.txt'

if 'new_todo' not in st.session_state:
    st.session_state['new_todo'] = ''

todos = func.read_file(FILEPATH)


def add_todo():
    new_todo = st.session_state['new_todo']
    todos.append(func.add_newline_char(new_todo))
    func.write_file(todos, FILEPATH)
    st.session_state['new_todo'] = ''


st.title("Py Do's!")
st.subheader("Your simplistic todo web-app.")

for index, todo in enumerate(todos):
    tamed_todo = todo.strip('\n')
    checkbox = st.checkbox(tamed_todo, key=todo)
    if checkbox:
        todos.remove(todo)
        func.write_file(todos, FILEPATH)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add todo", label_visibility='hidden', placeholder='Enter in your todo.',
              on_change=add_todo, key="new_todo")
