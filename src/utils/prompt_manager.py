class PromptManager:
    """Manager of prompts that are shown to user"""
    @staticmethod
    def yes_no(msg: str) -> bool:
        """Simple yes/no prompt. Returns `True` if yes/y was entered,
        if no/n was entered returns False"""
        allowed_yes_inputs = ['y', 'yes']
        allowed_no_inputs = ['n', 'no']
        while True:
            print(msg, end=' ')
            users_input = input("(Y/n): ").strip().lower()
            if users_input in allowed_yes_inputs:
                return True
            elif users_input in allowed_no_inputs:
                return False

            print('Please enter (Y/n).')
