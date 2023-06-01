def read_file(filename):
    """
    Reads content of a file and puts it into
    a list and returns that list.
    """
    with open(filename, 'r') as file:
        content = file.readlines()

    return content


def write_file(items, filename):
    """
    Writes the specified items into a file of
    your choice.
    """
    with open(filename, 'w') as file:
        file.writelines(items)


# var __name__ used to denote origin of script
# Commonly used to separate code from other modules


def load_ui(parent, child, list_name, var=None, singular='n'):
    """
    Loads a list of items into the specified UI. If singular = 'y'
    then it'll load first item from the list into the UI.
    """
    if singular == 'y':
        parent[child].update(value=var['todos'][0])
    else:
        parent[child].update(values=[todo.strip('\n') for todo in list_name])


def clear_ui(parent, child):
    parent[child].update(value='')


def add_newline_char(string):
    return string + '\n'


def display_popup(interface, msg, btn_msg):
    interface.popup(msg, title="Hold up!", custom_text=btn_msg, grab_anywhere=True,
                    keep_on_top=True, font=('Helvetica', 15))
