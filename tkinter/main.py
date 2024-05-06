import tkinter as tk
import random

class WordleWithKeyboard:
    def __init__(self, root, word_list):
        """
        The Constructor of the class. Has two variables 'root' and 'word_list'
        """
        self.root = root
        self.word_list = word_list
        self.initialize_game()

    def initialize_game(self):
        """
        Starts (initializes) the game
        """

        # check that the 'word_list' is not empty else return
        if not self.word_list:
            self.show_error("Word list is empty. Check the word file.")
            return

        # initialize instance variables for the wordle game and setup User interface
        self.secret_word = random.choice(list(self.word_list))
        self.attempts = 6
        self.current_attempt = 0
        self.current_guess = []
        self.best_key_color = {}
        self.setup_ui()

    def setup_ui(self):
        """
        Method to setup the user interface
        """

        # close the current Tkinter window(s)
        for widget in self.root.winfo_children():
            widget.destroy()

        # set window title to 'wordle game'
        self.root.title("Wordle Game")

        # create frame to handle guesses
        self.guess_frame = tk.Frame(self.root)
        self.guess_frame.grid(row=0, column=0, columnspan=10)

        # create labels for the guesses, 30 altogether - 6 guesses (rows) and 5 letters (columns) per word
        self.guess_labels = [
            [tk.Label(self.guess_frame, width=4, height=2, font=('Helvetica', 18), text='', borderwidth=2, relief='groove', bg='light grey')
             for _ in range(5)] for _ in range(6)]
        
        for i in range(6):
            for j in range(5):
                self.guess_labels[i][j].grid(row=i, column=j, padx=5, pady=5, sticky='nsew')

        
        # create label for messages
        self.message_label = tk.Label(self.root, text="", font=('Helvetica', 14), fg='red')
        self.message_label.grid(row=7, column=0, columnspan=10)

        # create keyboard frame
        self.keyboard_frame = tk.Frame(self.root)
        self.keyboard_frame.grid(row=8, column=0, columnspan=10)

        self.keys = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M', 'BACK']
        ]

        # create buttons on the keyboard frame for the letters of a keyboard
        self.buttons = {}
        for row_index, row in enumerate(self.keys):
            for col_index, key in enumerate(row):
                button = tk.Button(self.keyboard_frame, text=key, width=4, height=2, font=('Helvetica', 14),
                                   command=lambda k=key: self.key_press(k))
                button.grid(row=row_index, column=col_index, padx=5, pady=5)
                self.buttons[key] = button

        # create control frame for submit, restart and quit buttons and then create these buttons
        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.grid(row=9, column=0, columnspan=10, pady=(10, 0))

        submit_btn = tk.Button(self.controls_frame, text='Submit', width=10, height=1, font=('Helvetica', 14), command=self.submit_guess)
        submit_btn.pack(side=tk.LEFT, expand=True, padx=5)

        restart_btn = tk.Button(self.controls_frame, text='Restart', width=10, height=1, font=('Helvetica', 14), command=self.initialize_game)
        restart_btn.pack(side=tk.LEFT, expand=True, padx=5)

        quit_btn = tk.Button(self.controls_frame, text='Quit', width=10, height=1, font=('Helvetica', 14), command=self.quit_game)
        quit_btn.pack(side=tk.LEFT, expand=True, padx=5)


    def quit_game(self):
        """
        Method to end the game
        """
        self.root.destroy()


    def key_press(self, key):
        """
        Method to control what happens when a key is pressed on the keyboard
        """

        # if 'BACK' key is pressed as the most recent key, remove the most recent letter pressed
        if key == 'BACK' and self.current_guess:
            self.current_guess.pop()

        # if the guessed word is less than 5 and the 'BACK' key is not pressed, then add the current pressed letter to the guessed word
        elif len(self.current_guess) < 5 and key != 'BACK':
            self.current_guess.append(key)

        # when current guess has 5 letters in it - a 5 letter word, fill in the label for that attempt with the letters from the current guess
        for i, label in enumerate(self.guess_labels[self.current_attempt]):
            label.config(text=self.current_guess[i] if i < len(self.current_guess) else '')



    def submit_guess(self):
        """
        Method to control what happens when the submit button is pressed
        """

        # join the letters in the current guess to form a word, and make it lowercase
        guess = ''.join(self.current_guess).lower()

        # if the length of the word is not equal to 5 or is not in the word list, display a message that it is not a valid word
        if len(guess) != 5 or guess not in self.word_list:
            self.message_label.config(text="Not a valid 5-letter word!", fg='red')
            return

        # check the guessed word
        feedback = self.check_guess(self.secret_word, guess)

        # colour the keys according to the feedback and guess
        self.update_display(self.current_attempt, guess, feedback)
        self.color_keys(guess, feedback)

        if guess == self.secret_word:
            self.reveal_word(win=True)
        else:
            self.current_attempt += 1
            if self.current_attempt >= self.attempts:
                self.reveal_word(win=False)

        self.current_guess = []



    def update_display(self, attempt, guess, feedback):
        """
        Update the guess labels frame with the right color based on the feedback
        """
        for i in range(5):
            # set the color
            color = 'light grey' if feedback[i] == '_' else 'yellow' if feedback[i] == 'Y' else 'green'
            # apply the color
            self.guess_labels[attempt][i].config(text=guess[i].upper(), bg=color)


    def check_guess(self, secret, guess):
        """
        Check the guess and provide a response/feedback
        """
        response = ['_'] * 5
        secret_list = list(secret)
        guess_list = list(guess)

        # compare each character of the random secret word with each character in the guessed word
        # if the characters match, then mark the response for that index as G
        for i in range(5):
            if guess_list[i] == secret_list[i]:
                response[i] = 'G'
                secret_list[i] = None  # Mark this character as used to avoid duplication in further checks

        # if after doing the above, an index of the response variable still has '-' but one or more characters of the guessed word
        # exists in the random secret word, then mark the response index as Y.
        for i in range(5):
            if response[i] == '_' and guess_list[i] in secret_list:
                index = secret_list.index(guess_list[i]) # get index of secret_list element for where secret_list = guess_list[i]
                response[i] = 'Y'
                secret_list[index] = None  # Mark this character as used

        return response


    def color_keys(self, guess, feedback):
        for i, ch in enumerate(guess.upper()):
            new_color = 'red' if feedback[i] == '_' else 'yellow' if feedback[i] == 'Y' else 'green'
            if ch not in self.best_key_color or self.best_key_color[ch] == 'red' or (self.best_key_color[ch] == 'yellow' and new_color == 'green'):
                self.best_key_color[ch] = new_color
            self.buttons[ch].configure(bg=self.best_key_color[ch])

    def reveal_word(self, win):
      if win:
        final_message = "Congratulations! The word was: " + self.secret_word.upper()
        message_color = 'green'
      else:
        final_message = "Game Over! The word was: " + self.secret_word.upper()
        message_color = 'red'

      self.message_label.config(text=final_message, fg=message_color)

      # Disable all buttons to prevent further input
      for button in self.buttons.values():
        button.config(state='disabled')

    def show_error(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        tk.Label(error_window, text=message, font=('Helvetica', 14), fg='red').pack(pady=20, padx=20)
        tk.Button(error_window, text="OK", command=error_window.destroy, font=('Helvetica', 14)).pack(pady=10)


def load_words(file_path='5-letter-words.txt'):
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
        return {word.lower() for word in words if len(word) == 5}
    except FileNotFoundError:
        print("The word list file was not found.")
        return set()
    except Exception as e:
        print(f"An error occurred: {e}")
        return set()

def main():
    root = tk.Tk()
    root.geometry('800x600')  # Set the window size
    word_list = load_words()
    if not word_list:
        root.messagebox.showerror("Error", "Failed to load words. Exiting.")
        return
    app = WordleWithKeyboard(root, word_list)
    root.mainloop()

if __name__ == "__main__":
    main()
