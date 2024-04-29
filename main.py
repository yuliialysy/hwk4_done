def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_salary = 0
            devel_num = 0

            for line in file:
                developer_data = line.strip().split(',')
                if len(developer_data) != 2:
                    print(f'Wrong data format in line {line}')
                    return [0, 0]
                name, salary_str = developer_data
                salary = float(salary_str)
                total_salary += salary
                devel_num += 1
    
                average_salary = total_salary / devel_num 

            return total_salary, average_salary
    except FileNotFoundError:
        print('File is not found')
        return [0, 0]
    except ValueError:
        print('Data processsing error')
        return [0, 0]
    
if __name__ == '__main__':
    total, average = total_salary('salaries.txt')
    print(f'Total salary is: {total}. Average salary is: {average}')




        
           
        
            
                
 

                  