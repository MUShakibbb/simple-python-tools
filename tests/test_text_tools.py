from utils.text_tools import remove_extra_spaces, to_snake_case

def test_remove_extra_spaces():
    assert remove_extra_spaces("Hello   world") == "Hello world"

def test_to_snake_case():
    assert to_snake_case("Hello World.Example") == "hello_world_example"
