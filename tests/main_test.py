import sys
sys.path.insert(0, "../")
import main
import unittest
import json

class TestMain(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        """ Set up the json_data testing list."""
        super(TestMain, self).__init__(*args, **kwargs)

        self.test_json = "json_data/todolist.json"

        self.initial = {
            "0": ["zero"],
            "1": ["one"]
        }

        self.reset_json_file()

    def reset_json_file(self):
        
        with open(self.test_json, 'w') as fd:
            fd.write(json.dumps(self.initial))

    def test_add(self):
        """ This function will test the adding functionality."""

        end = {
            "0": ["zero"],
            "1": ["one"],
            "2": ["two"]
        }

        # Initalise to_do_list, used if the json file is empty
        to_do_list = {}

        # Read from the json file, and set to_do_list to the items if the file is not empty
        with open(self.test_json, 'r') as fd:
            lines = fd.read()
        if lines:
            to_do_list = json.loads(lines)

        # Make sure the initial list is correct
        self.assertEqual(cmp(to_do_list, self.initial), 0)

        main.add_item("two", self.test_json)

        # Read from the json file, and set to_do_list to the items if the file is not empty
        with open(self.test_json, 'r') as fd:
            lines = fd.read()
        if lines:
            to_do_list = json.loads(lines)

        # Make sure the resulting list is correct
        self.assertEqual(cmp(to_do_list, end), 0)

        self.reset_json_file()

    def initial_to_string(self):
        """ Convert self.initial to string representation."""

        return '\n'.join(str(item) + '\t' + str(self.initial[item][0]) for item in self.initial)

    def test_display(self):
        """ This function will test the display functionality."""

        initial_string = self.initial_to_string()

        output_items = main.display_items(self.test_json)

        self.assertEqual(output_items, initial_string)

    def test_delete(self):
        """ This function will test the deletion functionality."""

        end = {
            "0": ["zero"]
        }

        # Initalise to_do_list, used if the json file is empty
        to_do_list = {}

        # Read from the json file, and set to_do_list to the items if the file is not empty
        with open(self.test_json, 'r') as fd:
            lines = fd.read()
        if lines:
            to_do_list = json.loads(lines)

        # Make sure the initial list is correct
        self.assertEqual(cmp(to_do_list, self.initial), 0)

        main.delete_item("1", self.test_json)

        # Read from the json file, and set to_do_list to the items if the file is not empty
        with open(self.test_json, 'r') as fd:
            lines = fd.read()
        if lines:
            to_do_list = json.loads(lines)

        # Make sure the resulting list is correct
        self.assertEqual(cmp(to_do_list, end), 0)

        self.reset_json_file()

        

if __name__ == "__main__":
    unittest.main()