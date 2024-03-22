# Q3.
# 파일의 경로를 file_path로 설정

#file_path ="C:\\Users\\kimeh\\Downloads\\data-01-test-score.csv"
file_path ="./data-01-test-score.csv"

def read_file(file_path) :
    
    customer_list = [] #cutomer 개별 List를 저장하는 List

    with open (file_path) as customer_data: # "./date-01-test-score.csv"파일을 customer_data 객체에 저장
        while True:
            data = customer_data.readline().strip() #customer.csv에 한줄씩 data 변수에 저장, strip는 \n을 제거
            if  not  data: break	#데이터가 없을 때, Loop 종료
            customer_list.append(data.split(",")) #일반 데이터는 customer_list 객체에 저장, 데이터 저장시 “,”로 분리
    return str(customer_list).replace('], [','],\n [')
   
print(read_file(file_path))
