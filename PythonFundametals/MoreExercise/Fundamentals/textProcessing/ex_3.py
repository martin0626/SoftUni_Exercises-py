file_directory = input().split('\\')

result = file_directory[-1].split('.')

print (f'File name: {result[0]}\nFile extension: {result[1]}')