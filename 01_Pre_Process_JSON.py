import json
import csv

def write_to_csv(json_data):
    # Write data to the CSV file
    header = ["id", "speaker", "utterance", "emotion"]
    csv_filename = "output_test.csv"

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)

        # Write data to the CSV file
        for idx, episode_data in enumerate(json_data):
            episode_id = idx + 1
            speakers = episode_data["speakers"]
            utterances = episode_data["utterances"]
            #emotions = episode_data["emotions"]

            # Ensure all lists have the same length
            #min_length = min(len(speakers), len(utterances), len(emotions))
            min_length = min(len(speakers), len(utterances))
            for i in range(min_length):
                row = [episode_id, speakers[i], utterances[i]] #emotions[i]
                csv_writer.writerow(row)

    print(f"CSV file '{csv_filename}' has been created successfully.")

def print_stats(data):
    print(f"Number of Episodes : {len(data)}")
    print(f"Contents of Json : {list(data[0].keys())}")

def display_episode(data,ep_number):
    print(f"Episode : {data[ep_number]['episode']}")
    speakers = data[ep_number]['speakers']
    utterances = data[ep_number]['utterances']
    emotions = data[ep_number]['emotions']
    
    for idx in range(len(utterances)):
        print(f"{speakers[idx]}\t{utterances[idx]}\t{emotions[idx]}")


with open('MaSac_test_erc.json') as f:
    data = json.load(f)
    #print_stats(data)
    #display_episode(data,0)
    write_to_csv(data)


    
