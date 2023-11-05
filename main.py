from ui.python.Layout import Layout

path = "./data/layout 18x252.json"

layout = Layout(path)
print(layout.get_layout_name())
print(layout.get_layout())

test_check = ["test1", "test2", "test3", "test5", "test4", "test7"]

# test check
test_path = layout.get_check_optimal_path(test_check)

print(test_path)


# save layout to json file
with open("./data/layout 18x25_5.json", "w") as file:
    file.write(layout.get_layout_json())
layout.display_in_window()
