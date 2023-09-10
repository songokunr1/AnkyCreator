def read_srt_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            index = []
            start_time = []
            end_time = []
            text = []
            for line in lines:
                try:
                    index.append(int(line))
                    continue
                except ValueError as e:
                    pass
                if "-->" in  line:
                    times = line.split(' --> ')
                    start_time.append(times[0])
                    end_time.append(times[1])
                    continue
                text.append(line)


    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    # print(index)
    # print(start_time)
    # print(end_time)
    # print(text)
    text = ' '.join(text)
    return text


# Example usage
srt_file_path = r'C:\Users\Administrator\Downloads\The.srt'
subtitles = read_srt_file(srt_file_path)

# Print the extracted subtitles
