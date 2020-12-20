import subprocess
p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print("Today is....:", output)
