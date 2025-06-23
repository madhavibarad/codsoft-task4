import tkinter as tk
import random


player_score = 0
computer_score = 0

winning_rules = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}

random_win_mode = True

def play(user_choice):
    global player_score, computer_score

    options = list(winning_rules.keys())
    
    if random_win_mode and random.random() < 0.2:
    
        computer_choice = [k for k, v in winning_rules.items() if v == user_choice][0]
    else:
        computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif winning_rules[user_choice] == computer_choice:
        result = "You Win!"
        player_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

   
    user_label.config(text=f"Your Choice: {user_choice}")
    comp_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"Score - You: {player_score} | Computer: {computer_score}")

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    user_label.config(text="Your Choice: ")
    comp_label.config(text="Computer's Choice: ")
    result_label.config(text="Result: ")
    score_label.config(text="Score - You: 0 | Computer: 0")

root = tk.Tk()
root.title(" Rock Paper Scissors")
root.geometry("420x400")
root.configure(bg="#e3f6f5")  # Soft pastel background

tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 20, "bold"), bg="#e3f6f5").pack(pady=10)

btn_frame = tk.Frame(root, bg="#e3f6f5")
btn_frame.pack(pady=10)


colors = {
    "Rock": "#a8dadc",
    "Paper": "#457b9d",
    "Scissors": "#1d3557"
}

for idx, choice in enumerate(["Rock", "Paper", "Scissors"]):
    tk.Button(btn_frame, text=choice, width=12,
              command=lambda ch=choice: play(ch),
              bg=colors[choice], fg="white",
              font=("Helvetica", 12, "bold"),
              activebackground="#f1faee").grid(row=0, column=idx, padx=10)

user_label = tk.Label(root, text="Your Choice: ", font=("Helvetica", 12), bg="#e3f6f5")
user_label.pack(pady=5)

comp_label = tk.Label(root, text="Computer's Choice: ", font=("Helvetica", 12), bg="#e3f6f5")
comp_label.pack(pady=5)

result_label = tk.Label(root, text="Result: ", font=("Helvetica", 14, "bold"), bg="#e3f6f5")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Helvetica", 12), bg="#e3f6f5")
score_label.pack(pady=10)

tk.Button(root, text="Reset Game", command=reset_game, bg="#ffb703", fg="#023047", font=("Helvetica", 12, "bold")).pack(pady=10)

root.mainloop()
