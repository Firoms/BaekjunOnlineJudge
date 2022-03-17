from datetime import datetime


date = datetime.strptime(input("날짜 입력하세요 (형식 : YYYYMMDD) : "), "%Y%m%d")
now  = datetime.now()


date_diff = date - now
print(date_diff)