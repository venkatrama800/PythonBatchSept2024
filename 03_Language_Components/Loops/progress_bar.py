#!/usr/bin/python3

data_set = range(11)
data_set_length = len(data_set) - 1  # We subtract 1 so that the loop correctly handles 100%
progress_bar_length = 10

for loop_index in data_set:
   
    percent_completed = loop_index * 10 if loop_index != 0 else 3  # Start at 3%, then 10, 20, ..., 100

    completed_bars = int((percent_completed / 100) * progress_bar_length)

    progress_bar = '[' + '*' * completed_bars + ' ' * (progress_bar_length - completed_bars) + ']'

    print(f"{progress_bar} {percent_completed}% completed")

print("Task complete!")