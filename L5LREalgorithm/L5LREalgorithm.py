def data_compression(original_file_name: str,new_file_name: str):
    f = open(original_file_name,'r')
    f2 = open(new_file_name,'w')
    original_text = f.read()
    if len(original_text) > 0:
        count = 1
        for i in range(1, len(original_text)):
            if i == len(original_text)-1:
                if original_text[i] == original_text[i-1]:
                    count += 1
                    f2.write(f'{count}{original_text[i]}')
                else:
                    f2.write(f'{count}{original_text[i-1]}')
                    f2.write(f'1{original_text[i]}')
            elif original_text[i] == original_text[i-1]: count += 1
            else:
                f2.write(f'{count}{original_text[i-1]}')
                count = 1
    f.close()
    f2.close()

def data_recovery(original_file_name: str,new_file_name: str):
    f = open(original_file_name,'r')
    f2 = open(new_file_name,'w')
    original_text = f.read()
    if len(original_text) > 1:
        for i in range(1, len(original_text), 2):
            f2.write(original_text[i]*int(original_text[i-1]))
    f.close()
    f2.close()

data_compression('original.txt','new.txt')
data_recovery('new.txt','new2.txt')