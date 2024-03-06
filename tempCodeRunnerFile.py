    label1 = ttk.Label(frame, text="Name", padding=10)
    label1.grid(column=0, row=0, columnspan=2)
    habit_entry = ttk.Entry(frame, textvariable=habit_name)
    habit_entry.grid(column=0, row=1, columnspan=2)
