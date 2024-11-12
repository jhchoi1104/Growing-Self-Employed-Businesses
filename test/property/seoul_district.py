import requests
from dotenv import load_dotenv
import os
import pymysql

load_dotenv()

GU_REQUEST_URL = "https://www.serve.co.kr/info/v1/address/getLdongFilter"
DONG_REQUEST_URL = "https://www.serve.co.kr/info/v1/address/getLdongFilter"

# DB 정보
connection = pymysql.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'), 
    database="KB",
    charset='utf8'
)
cursor = connection.cursor()

def find_gu_code():
    gu_code_list = {}

    params = {
        'ldongRegDvsnCd': 2,
        'sidoCd': '1100000000' # 서울특별시
    }

    response = requests.get(GU_REQUEST_URL, params=params)

    if response.status_code == 200:
        try:
            data = response.json()['data']['resultList']
            for item in data:
                gu_code_list[item.get('sggNm')] = item.get('ldongCd')
        except ValueError as e:
            print("JSONDecodeError:", e)
            print("Response text:", response.text)
    else:
        print("Request failed with status code:", response.status_code)
    
    return gu_code_list


def create_dong_code(gu_name, ldong_cd):
    dong_code_list = {}

    params = {
        'sggCd': ldong_cd, # 법정동 코드
        'ldongRegDvsnCd': "3"
    }

    response = requests.get(DONG_REQUEST_URL, params=params)

    if response.status_code == 200:
        try:
            data = response.json()['data']['resultList']
            for item in data:
                sql = "INSERT INTO district_code (gu_name, gu_code, dong_name, dong_code) VALUES (%s, %s, %s, %s)"
                val = (gu_name, ldong_cd, item.get('emdNm'), item.get('ldongCd'))
                try:
                    cursor.execute(sql, val)
                except Exception as e:
                    print(f"Error occurred: {e}")
                dong_code_list[item.get('emdNm')] = item.get('ldongCd') # 동 명 : 코드
        except ValueError as e:
            print("JSONDecodeError:", e)
            print("Response text:", response.text)
    else:
        print("Request failed with status code:", response.status_code)
    print(dong_code_list)
    return dong_code_list


gu_code_list = find_gu_code()

for gu_name, ldong_cd in gu_code_list.items():
    print("[", gu_name, "-", ldong_cd, "]") # 구
    create_dong_code(gu_name, ldong_cd)
    print("=========================")

connection.commit()  # Save the changes
cursor.close()
connection.close()