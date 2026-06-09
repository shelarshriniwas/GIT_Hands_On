
seconds = 3661

hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60

print(f"{hours:02}:{minutes:02}:{secs:02}")