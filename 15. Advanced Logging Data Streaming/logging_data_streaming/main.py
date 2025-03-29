from data_stream import stream_log_data

if __name__=="__main__":
    file_path = 'sample_data.txt'

    print("Streaming log Data: ")
    for log_entry in stream_log_data(file_path):
        print(log_entry)

