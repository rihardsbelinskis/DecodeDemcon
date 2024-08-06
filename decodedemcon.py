# Using the heapq library
import heapq

def assign_stages(shows):
    # Sort shows by their start time
    shows.sort(key=lambda show: show[1])

    # Keeping track of the end time of each stage (priority queue)
    stages = []

    # Store the sequence of shows for each stage
    stage_show_sequence = {}

    # Iterating through all shows
    for show in shows:
        show_name, start, end = show

        # Check if any stage is free (i.e., the earliest end time is <= current start time)
        if stages and stages[0][0] <= start:
            # Reuse the stage
            end_time, stage_id = heapq.heappop(stages)
        else:
            # No free stages, so another is needed
            stage_id = len(stages) + 1
            stage_show_sequence[stage_id] = []

        # Assign this show to the stage
        stage_show_sequence[stage_id].append(show_name)

        # Push the new end time for this stage
        heapq.heappush(stages, (end, stage_id))

    # Calculate the number of stages required
    num_stages = len(stage_show_sequence)

    # Return the number of stages required and the sequence of each stage
    return num_stages, stage_show_sequence

# Sample input - feel free to add / remove / adjust
shows = [
    ("show_1", 29, 33),
    ("show_2", 2, 9),
    ("show_3", 44, 47),
    ("show_4", 26, 30),
    ("show_5", 15, 20),
    ("show_6", 8, 15),
    ("show_7", 2, 9),
    ("show_8", 30, 34),
    ("show_9", 1, 9),
    ("show_10", 20, 28),
    ("show_11", 1, 4),
    ("show_12", 2, 11),
    ("show_13", 26, 29),
    ("show_14", 5, 10),
    ("show_15", 37, 44),
    ("show_16", 27, 35),
    ("show_17", 36, 39),
    ("show_18", 4, 10),
    ("show_19", 35, 44),
    ("show_20", 22, 30),
    ("show_21", 15, 20),
    ("show_22", 42, 46),
    ("show_23", 6, 9),
    ("show_24", 19, 23),
    ("show_25", 31, 38),
    ("show_26", 37, 41),
    ("show_27", 30, 36),
    ("show_28", 14, 21),
    ("show_29", 5, 13),
    ("show_30", 33, 36)
]

# Assign a stage to each show
num_stages, stage_show_sequence = assign_stages(shows)

# Print outputs
print(f"The minimum number of stages required is: {num_stages}")
print("Show sequence per stage:")
for stage, shows in stage_show_sequence.items():
    print(f"Stage {stage}: {', '.join(shows)}")
