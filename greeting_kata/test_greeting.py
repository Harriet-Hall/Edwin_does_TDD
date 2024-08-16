# create a function that takes a name as an argument and returns a greeting message Hello + name!
# eg if the function takes the name Edwin, it should return the greeting "Hello Edwin!"
# if the function is not given a name it should return the greeting ""Hello stranger!""
# if the function is given an argument that is not a string it returns the message "This is not a valid name!"


def generate_greeting(name):
    if name == "":
        return "Hello Stranger!"

def test_generate_greeting_should_handle_empty_string():
    result = generate_greeting("")
    assert(result) == "Hello Stranger!"