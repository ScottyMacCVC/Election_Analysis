counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

message_to_candidate = (
    f"You received {counties_dict:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {counties_dict / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)