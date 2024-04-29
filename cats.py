def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info_list = []

            for line in file:
                cats_details = line.strip().split(',')
                if len(cats_details) != 3:
                    print(f'Wrong data format in line {line}')
                    return [0, 0]
                cat_id, cat_name, cat_age_str = cats_details
                cat_age = int(cat_age_str)

                cat_info = {
                     'id': cat_id,
                     'name': cat_name,
                     'age': cat_age
                }

                cats_info_list.append(cat_info)
    except ValueError:
         print('Data processsing error')
         return [0, 0]   
    except FileNotFoundError:
        print('File is not found')
        return [0, 0] 
    return cats_info_list 

if __name__ == '__main__':
     cats_info_list = get_cats_info('cats_info.txt')
     for d in cats_info_list:
         print(d)



    