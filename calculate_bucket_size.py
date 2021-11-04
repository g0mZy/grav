import csv
import boto3
import subprocess
import os

s3_client = boto3.client('s3', region_name='ap-southeast-2')
s3 = boto3.resource('s3')
input_csv = r"list-of-datasets.csv"
output_csv = r"output.csv"
output_csv_header = ['ts', 'dataset_id', 'dataset_name', 'dataset_path', 'gigapixels', 'gigabytes']

# Deleting the old output.csv file
subprocess.call(['rm', '-rf', '{0}'.format(output_csv)])

with open(output_csv, 'a') as csv_writer:
    # Adding the header in output file
    if os.stat(output_csv).st_size == 0:
        writer = csv.writer(csv_writer)
        writer.writerow(output_csv_header)

    print("====================================Processing Strated====================================")
    
    with open(input_csv,'rt') as f:
        data = csv.DictReader(f, delimiter=',')
        for row in data:
            row_dict = dict(row)
            row_list = list(row_dict.values())
            # print(str(row_list))
            s3_object_path = row['dataset_path']
            full_s3_path = 's3://' + s3_object_path
            
            try:
                # aws s3 ls --summarize --human-readable --recursive s3://path/to/dataset/ | grep Total
                full_size_details = subprocess.check_output("aws s3 ls --summarize --human-readable --recursive " + '{0}'.format(full_s3_path) + " | grep Total", shell=True).strip()
                size_in_gb = str(full_size_details).replace('\'','').split('Total Size:')[1]
                print('Size of path ' + full_s3_path + ' is: ' + size_in_gb)
                
                # Appending the result back to CSV
                row_list.append(size_in_gb)
                writer.writerow(row_list)
            except Exception as e:
                print(str(e))
        print("====================================Processing Completed====================================")