# Coding Conversations
# mat 14feb24
import os
import pandas as pd

def print_banner(banner):
    print(f'{banner}')


def read_csv_to_pd(file_name):
    file_path = os.path.join('assets', file_name)
    print(f'file_path: {file_path}')

    # read csv file into pandas dataframe
    df = pd.read_csv(file_path)

    #print(df.head(10))
    print(df.columns)

    return df

def run_test(df):
    import pandas as pd

    # Read the CSV file into a Pandas DataFrame
    # df = pd.read_csv("geothermalinvestments.csv")

    # Display the first 5 rows of the DataFrame
    #print(df.head())

    # Get information about the columns and their data types
    print(df.info())

    # Find Region containing the Country of Chile
    region_with_chile = df[df["Country"] == "Chile"]["Region"]
    region_code_with_chile = region_with_chile.values[0]

    # Print Region
    print(region_code_with_chile)

    # Find column most similar to Total Project Cost
    total_cost_column = df.filter(like="Total Project Cost")
    total_cost_column_name = total_cost_column.columns[0]
    # Print Total Project Cost column header
    print(total_cost_column_name)

    # Initialize total cost variable
    total_cost = 0
    df_lcr = df[df["Region"] == region_code_with_chile]
    print(df_lcr.size)

    # Loop through rows in Region containing the Country of Chile
    for index, row in df_lcr.iterrows():
        # ignore NaN in row
        if pd.isna(row[total_cost_column_name]):
            continue
        if row[total_cost_column_name] != "":
            # Add Total Project Cost to total_cost
            total_cost += int(row[total_cost_column_name])
            #print(f"cumulative Project Cost for Region containing Chile {region_code_with_chile}: US$ {total_cost:.2f} million")

    # Print the total cost
    print(f"Total Project Cost for Region {region_code_with_chile} containing Chile: US$ {total_cost:.2f} million")


if __name__ == '__main__':
    print_banner('Coding Conversations starts...')

    # set path to file under test
    under_test_file_name = "geothermalinvestments.csv"
    # read file under test
    df = read_csv_to_pd(under_test_file_name)
    print(f'read_csv_to_pd: {df.size}')

    run_test(df)

    print(f'Coding Conversations fini...')




