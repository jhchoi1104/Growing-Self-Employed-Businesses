import requests
from dotenv import load_dotenv

import os

load_dotenv()
OPEN_DATA_API_KEY = os.environ.get('OPEN_DATA_API_KEY')

BRAND_FRCS_BZM_INTRRCTINFO_URL = "http://apis.data.go.kr/1130000/FftcBrandFrcsIntInfo2_Service/getbrandFrcsBzmnIntrrctinfo"

# 인테리어 비용
def find_interior_cost(brand, year):
    brand_frcs_bzm_intrrctinfo_params = {
        "serviceKey": OPEN_DATA_API_KEY,
        "pageNo": 1,
        "numOfRows": 1,
        "resultType": "json",
        "jngBizCrtraYr": year,
        "brandMnno": brand['brand_mnno']
    }

    response = requests.get(BRAND_FRCS_BZM_INTRRCTINFO_URL, params=brand_frcs_bzm_intrrctinfo_params)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")

    try:
        data = response.json()
        if not ('items' in data and data['items']):
            return
    
        item = data['items'][0]
        
        brand["unit_ar_intrr_amt_scope_val"] = item['unitArIntrrAmtScopeVal']  # 단위 면적 계약 금액 범위
        brand["stor_crtra_ar"] = item['storCrtraAr']                           # 매장 계약 면적
        brand["intrr_amt_scope_val"] = item['intrrAmtScopeVal']                # 인테리어 총 금액 범위
    except ValueError as e:
        print("JSONDecodeError:", e)
        print("Response Text:", response.text)