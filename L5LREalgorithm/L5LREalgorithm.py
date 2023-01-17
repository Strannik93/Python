import io

def data_compression(original_file_name: str,new_file_name: str):
    f = open(original_file_name, 'r', encoding='utf-8')
    f2 = open(new_file_name, 'w', encoding='utf-8')
    original_text = f.readlines()
    original_text = [line.rstrip() for line in original_text]
    for k in range(len(original_text)):
        if k > 0: f2.write('\n')
        if len(original_text[k]) > 0:
            count = 1
            for i in range(1, len(original_text[k])):
                if i == len(original_text[k])-1:
                    if original_text[k][i] == original_text[k][i-1]:
                        count += 1
                        f2.write(f'{count}{original_text[k][i]}')
                    else:
                        f2.write(f'{count}{original_text[k][i-1]}')
                        f2.write(f'1{original_text[k][i]}')
                elif original_text[k][i] == original_text[k][i-1]: count += 1
                else:
                    f2.write(f'{count}{original_text[k][i-1]}')
                    count = 1
    f.close()
    f2.close()

def data_recovery(original_file_name: str,new_file_name: str):
    f = open(original_file_name,'r', encoding='utf-8')
    f2 = open(new_file_name,'w', encoding='utf-8')
    original_text = f.readlines()
    original_text = [line.rstrip() for line in original_text]
    for k in range(len(original_text)):
        if k > 0: f2.write('\n')
        new_text = ''
        i = 0
        while i < len(original_text[k]):
            if original_text[k][i].isdigit() and original_text[k][i+1].isdigit() == False:
                new_text += original_text[k][i] + ' ' + original_text[k][i+1] + ' '
                i += 2
            else:
                new_text += original_text[k][i]
                i += 1
        new_text = new_text.split()
        if len(new_text) > 1:
            for i in range(1, len(new_text), 2):
                f2.write(new_text[i]*int(new_text[i-1]))
    f.close()
    f2.close()

data_compression('original.txt','new.txt')
data_recovery('new.txt','new2.txt')