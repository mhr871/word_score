import tkinter as tk
from tkinter import messagebox
import random

def load_words(file_path):
    words = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  
            if line:  
                parts = line.split(';')
                if len(parts) == 2:  
                    word, meaning = parts
                    words.append((word.strip(), meaning.strip())) 
                else:
                    print(f"Skipped line with incorrect format: {line}")
    return words

def create_questions(words):
    questions = []
    for word, meaning in random.sample(words, min(30, len(words))):  
        wrong_answers = random.sample([w[1] for w in words if w[1] != meaning], 4)
        options = random.sample([meaning] + wrong_answers, 5)
        questions.append((word, meaning, options))
    return questions

class QuizApp:
    def __init__(self, master, words):
        self.master = master
        self.master.geometry("600x400")
        self.master.title("Word Quiz - English")
        self.master.configure(bg="#8F9B77")  
        self.words = words
        self.questions = create_questions(words)
        self.question_index = 0
        self.correct_count = 0
        self.answers = []

        self.question_label = tk.Label(master, text="", wraplength=400, bg="#8F9B77", font=("Arial", 20))
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()  
        self.option_buttons = []

        button_frame = tk.Frame(master, bg="#8F9B77")
        button_frame.pack(pady=10)

        for i in range(5):
            button = tk.Radiobutton(button_frame, text="", variable=self.var, value="", font=("Arial", 12), bg="#8F9B77",
                                    command=self.option_selected)  
            button.grid(row=i, column=0, sticky="w", padx=10, pady=5)
            self.option_buttons.append(button)

        self.next_button = tk.Button(master, text="Next", command=self.next_question, font=("Arial", 20), width=10, height=2,
                                       highlightbackground="lightgreen", activebackground="green", 
                                       fg="#8F9B77", bg="brown", state=tk.DISABLED) 
        self.next_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        if self.question_index < len(self.questions):
            word, meaning, options = self.questions[self.question_index]
            self.question_label.config(text=f"{self.question_index + 1}. What is the meaning of '{word}'?")
            self.var.set(None) 
            for i, button in enumerate(self.option_buttons):
                button.config(text=options[i], value=options[i])
            self.next_button.config(state=tk.DISABLED) 

        else:
            self.show_results()

    def option_selected(self):
        if self.var.get():
            self.next_button.config(state=tk.NORMAL)
        else:
            self.next_button.config(state=tk.DISABLED)

    def next_question(self):
        if not self.var.get(): 
            messagebox.showwarning("Warning", "Please select an option.")
            return

        selected = self.var.get()
        correct = self.questions[self.question_index][1]
        self.answers.append((self.question_index + 1, selected, correct))
        if selected == correct:
            self.correct_count += 1
        self.question_index += 1
        self.show_question()

    def show_results(self):
        total_questions = len(self.questions)
        wrong_count = total_questions - self.correct_count

        if total_questions == 0:
            messagebox.showinfo("Results", "No questions were asked.")
            return

        success_rate = (self.correct_count / total_questions) * 100

        result_message = f"Correct Answers: {self.correct_count}\nWrong Answers: {wrong_count}\nSuccess Rate: {success_rate:.2f}%"
        messagebox.showinfo("Results", result_message)

        for index, (question_index, given_answer, correct_answer) in enumerate(self.answers):
            if given_answer != correct_answer:
                message = f"Question {question_index}: '{self.questions[question_index - 1][0]}'\nWrong Answer: {given_answer}\nCorrect Answer: {correct_answer}"
                messagebox.showinfo("Wrong Answer", message)

def main():
    words = load_words("C:/python_studies/word_score/dictionary.txt")
    root = tk.Tk()
    app = QuizApp(root, words)
    root.mainloop()

if __name__ == "__main__":
    main()
