# Q5.
# 파일의 경로를 file_path로 설정

#file_path ="C:\\Users\\kimeh\\Downloads\\data-01-test-score.csv"
file_path ="./data-01-test-score.csv"

class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path
        self.customer_list = [] #cutomer 개별 List를 저장하는 List
        self.merged_list = [] #cutomer 개별 List의 sum을 저장하는 List

    def read_file(self):
        with open (self.file_path) as customer_data: # "./date-01-test-score.csv"파일을 customer_data 객체에 저장
            while True:
                data = customer_data.readline().strip() #customer.csv에 한줄씩 data 변수에 저장, strip는 \n을 제거
                if  not  data: break	#데이터가 없을 때, Loop 종료
                self.customer_list.append(list(map(int,data.split(",")))) #“,”로 분리하고 int형으로 변환후 custom_list에 추가
        return self.customer_list

    def merge_list(self):
        self.read_file()
        for i in self.customer_list:
            self.merged_list.append(sum(i)/len(i))
        self.merged_list.sort()
        return self.merged_list

read_csv = ReadCSV(file_path)
print(read_csv.merge_list())