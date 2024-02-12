import json
import csv

# Read the JSON file
with open(r"C:\Users\pooja\Downloads\MaSaC_test_erc.json", 'r') as json_file:
    data = json.load(json_file)

# Extract utterance and emotion from each episode
utterances_emotions = []
for episode_data in data:
    utterances = episode_data['utterances']
    emotions = episode_data['labels']

    # Ensure utterances and emotions have the same length
    assert len(utterances) == len(emotions)

    for utterance, emotion in zip(utterances, emotions):
        utterances_emotions.append((utterance, emotion))

# Write the utterances and emotions to a CSV file
with open(r'C:\Users\pooja\Downloads\output_test.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['utterance', 'emotion'])  # Write header
    writer.writerows(utterances_emotions)
    print("done- yay!")
