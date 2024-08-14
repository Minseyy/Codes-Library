config_0 = \
    ["abcdefghijklm",
     "nopqrstuvwxyz"]

config_1 = \
    ["789",
     "456",
     "123",
     "0.-"]

config_2 = \
    ["chunk",
     "vibex",
     "gymps",
     "fjord",
     "waltz"]

config_3 = \
    ["bemix",
     "vozhd",
     "grypt",
     "clunk",
     "waqfs"]

keyboard = [config_0, config_1, config_2, config_3]  # Combine all configs into one variable
key = input("Enter a string to type: ")

shortest_len = 0
shortest_config = ""
shortest_operation = ""
failed_count = 0


    for current_config in keyboard:
        position_index = 0
        current_line_index = 0
        operations = ""
        failed_count = 0

        for char_key in key:
             if key.index(char_key) < len(key):
                for config_line in current_config:
                    if char_key in config_line:

                        char_index_in_line = config_line.index(char_key)
                        difference = char_index_in_line - position_index
                        line_index = current_config.index(config_line)

                        if difference > 0:
                            operations += "r" * difference

                        elif difference < 0:
                            operations += "l" * -difference

                        position_index = char_index_in_line

                        if line_index > current_line_index:
                            operations += "d" * (line_index - current_line_index)

                        elif line_index < current_line_index:
                            operations += "u" * (current_line_index - line_index)

                        current_line_index = line_index
                        if line_index == current_line_index:
                            operations += "p"

        if (len(operations) > 0) and (len(operations) < len(shortest_operation)):
            shortest_operation = operations
            shortest_config = current_config

    print(f"The robot must perform the following operations:\n{shortest_operation}")

else:
    failed_count += 1
    print("The string cannot be typed out.")










