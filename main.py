import os
import subprocess

# Caminho do vídeo de entrada
input_video_path = r"C:\Users\aline\Desktop\videomaker\Les_ombres_du_passe.mp4"

# Caminho de destino para os vídeos cortados
output_directory = r"C:\Users\aline\Desktop\videomaker\Les_ombres_du_passe"

# Duração desejada para os vídeos de saída (em segundos)
duration = 180

# Função para converter segundos em formato de tempo HH:MM:SS
def seconds_to_time(seconds):
    minutes, seconds = divmod(seconds, 180)
    hours, minutes = divmod(minutes, 180)
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

# Comando ffmpeg para cortar o vídeo em clipes de 1 minuto
ffmpeg_command = f'ffmpeg -i "{input_video_path}" -c copy -f segment -segment_time {duration} -reset_timestamps 1 -map 0 "{output_directory}/Les_ombres_du_passe%03d.mp4"'

# Executa o comando ffmpeg
subprocess.run(ffmpeg_command, shell=True)

# Renomeia os arquivos de saída com base no tempo de início e fim do corte
for i, file_name in enumerate(os.listdir(output_directory)):
    if file_name.endswith(".mp4"):
        start_time = i * duration
        end_time = (i + 1) * duration
        new_file_name = f"Les_ombres_du_passe{seconds_to_time(start_time)}_{seconds_to_time(end_time)}.mp4"
        os.rename(os.path.join(output_directory, file_name), os.path.join(output_directory, new_file_name))

print("Vídeo cortado com sucesso!")
