from input_handler import get_string, get_number_input, yes_no



def add_instructions(selected_recipe):
    # TODO: Separate user input and data manipulation functions
    instructions = selected_recipe['instructions']
    while True:
        add_instruction = get_string('Enter the instruction and the preferred position of this instruction below:\n')
        print('Enter the number related to the instruction:\n')
        position_instruction = get_number_input(1, len(instructions) + 1)
        instructions.insert(position_instruction - 1, add_instruction)
        print('Instructions Added')
        instr_ans = yes_no("""Do you want to add another instruction?
                                \nPlease input Yes(y) or No(n): """)
        if not instr_ans:
            break
        else:
            for i, instruction in enumerate(instructions):
                print(f'{i + 1}. {instruction}\n')


def move_instruction(selected_recipe):
    instructions = selected_recipe['instructions']
    while True:
        print('Enter the number of the instruction you want to move/re-arrange:\n')
        move_instruction_num = get_number_input(1, len(instructions))
        print('Enter the preferred position (number) you want to move the instruction to:\n')
        position_instruction_num = get_number_input(1, len(instructions))
        instructions.insert(position_instruction_num - 1, instructions.pop(move_instruction_num - 1))
        print('Instruction Moved!')
        move_instr_ans = yes_no("""Do you want to move another instruction?
                                                    \nPlease input Yes(y) or No(n): """)
        if not move_instr_ans:
            break
        else:
            for i, instruction in enumerate(instructions):
                print(f'{i + 1}. {instruction}\n')
