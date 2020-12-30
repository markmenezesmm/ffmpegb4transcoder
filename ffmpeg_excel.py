import pandas
import subprocess

data = pandas.read_excel("filenames.xls", "Sheet1")
input_data  = data["Input File Name ffmpeg"].values.tolist()
output_data = data["Output File Name ffmpeg"].values.tolist()
output_folder = data["bento4 output folder"].values.tolist()

index = 0

while index < len(input_data):
	subprocess.run(f"ffmpeg -i \"{input_data[index]}\" -c:v libx264 -crf 23 -vf scale=1280:720 -preset veryfast -g 48 -keyint_min 48 -sc_threshold 0 -c:a aac -b:a 64K -ac 2 \"{output_data[index]}\"", shell=True)
	subprocess.run(f"mp4hls --segment-duration 5 --encryption-mode SAMPLE-AES --encryption-key 3777397A24432646294A404E63526655 --output-encryption-key -o \"{output_folder[index]}\" \"{output_data[index]}\"", shell=True)
	index += 1

print