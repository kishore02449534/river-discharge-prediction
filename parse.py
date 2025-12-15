import os
import pandas as pd
import re

def parse_file(file_path):
    """
    Parse a single file to extract the information into a structured format.
    """
    data = []
    current_model = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Match the section header
            header_match = re.match(r"Model (\d+) \| days behind (\d+) \| days ahead (\d+)", line)
            if header_match:
                # Save the current model data and start a new section
                if current_model:
                    data.append(current_model)
                current_model = {
                    "Model": int(header_match.group(1)),
                    "Days_Behind": int(header_match.group(2)),
                    "Days_Ahead": int(header_match.group(3)),
                    "Metrics": []
                }
                continue

            # Match train/test metrics
            metric_match = re.match(
                r"(\w+)\s+(train|test)\s+RMSE:\s+([\d.]+),\s+R\^2:\s+([\d.]+)",
                line.strip()
            )
            if metric_match:
                metric = {
                    "Type": metric_match.group(1),
                    "Dataset": metric_match.group(2),
                    "RMSE": float(metric_match.group(3)),
                    "R^2": float(metric_match.group(4))
                }
                current_model["Metrics"].append(metric)

        # Add the last model's data if present
        if current_model:
            data.append(current_model)
    
    return data

def flatten_data(parsed_data, relative_path):
    """
    Flatten the parsed data into a list of dictionaries suitable for DataFrame conversion.
    """
    rows = []
    for model in parsed_data:
        base_info = {
            "Model": model["Model"],
            "Days_Behind": model["Days_Behind"],
            "Days_Ahead": model["Days_Ahead"],
            "File_Path": relative_path
        }
        for metric in model["Metrics"]:
            row = base_info.copy()
            row["Type"] = metric["Type"]
            row["Dataset"] = metric["Dataset"]
            row["RMSE"] = metric["RMSE"]
            row["R^2"] = metric["R^2"]
            rows.append(row)
    return rows

def recursive_search_and_parse(root_dir):
    """
    Recursively search for .txt files in a directory, parse their content,
    and store the results in a DataFrame.
    """
    all_data = []

    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith('.txt'):
                file_path = os.path.join(dirpath, file)
                relative_path = os.path.relpath(file_path, root_dir)
                parsed_data = parse_file(file_path)
                flat_data = flatten_data(parsed_data, relative_path)
                all_data.extend(flat_data)

    return pd.DataFrame(all_data)

# Example usage:
root_directory = "./results"  # Replace with your root directory
df = recursive_search_and_parse(root_directory)
print(df)

# parse path in each row to cols ex: results/Single_Var_Prediction_WLD_h:25_l:3/10000

#name of experiment

df['experiment'] = df['File_Path'].apply(lambda x: x.split('/')[0].split('_h:')[0])

# number of epochs
df['epochs'] = df['File_Path'].apply(lambda x: x.split('/')[1]).astype(int)

# hidden size
df['hidden_size'] = df['File_Path'].apply(lambda x: x.split('h:')[1].split('_')[0]).astype(int)

# layer size
df['num_layers'] = df['File_Path'].apply(lambda x: x.split('l:')[1].split('/')[0]).astype(int)

#drop the file path
df.drop(columns=['File_Path'], inplace=True)

# only use test data
df = df[df['Dataset'] == 'test']

# drop epopchs less than 1000
df = df[df['epochs'] >= 1000]

print(df)

# for each experiment scatter plot RMSE and R^2 for hidden and layer size and find the correlation

import matplotlib.pyplot as plt
import seaborn as sns

# Scatter plot of RMSE and R^2 for each experiment



for experiment in df['experiment'].unique():
    
    # plot RMSE and hidden size

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.scatterplot(data=df[df['experiment'] == experiment], x='hidden_size', y='RMSE', hue='Days_Ahead')
    plt.title(f'{experiment} RMSE vs Hidden Size')
    plt.xlabel('Hidden Size')
    plt.ylabel('RMSE')

    # plot R^2 and hidden size

    plt.subplot(1, 2, 2)
    sns.scatterplot(data=df[df['experiment'] == experiment], x='hidden_size', y='R^2',  hue='Days_Ahead')
    plt.title(f'{experiment} R^2 vs Hidden Size')
    plt.xlabel('Hidden Size')
    plt.ylabel('R^2')

    
    # plot RMSE and layer size

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.scatterplot(data=df[df['experiment'] == experiment], x='num_layers', y='RMSE',  hue='Days_Ahead')
    plt.title(f'{experiment} RMSE vs Layer Size')
    plt.xlabel('Layer Size')
    plt.ylabel('RMSE')

    # plot R^2 and layer size

    plt.subplot(1, 2, 2)
    sns.scatterplot(data=df[df['experiment'] == experiment], x='num_layers', y='R^2',  hue='Days_Ahead')
    plt.title(f'{experiment} R^2 vs Layer Size')
    plt.xlabel('Layer Size')
    plt.ylabel('R^2')

    plt.show()



