allowlist = []
allowlist_num = '0123456789'
allowlist_giho = '자가하다아러타너차파버바나어서라사거카더커처마터저머허퍼'
allowlist_si = '택완아무읍연중탄속안횡풍금단홀귀수등두음마척계작기온인칠송북보하덕가태담함악종영선전군나서흥일철례산평사거실화월합옹청밀익의백김임로은추유항삼원포달주랑령초구창노과대운천승괴통상룡양논해춘충봉부울관미신시녕암목순리이도정고동오곡강광진파옥제장용남왕경증위성홍릉공래문명당예여'

allowlist.extend(allowlist_num)
allowlist.extend(allowlist_giho)
allowlist.extend(allowlist_si)

results = allowlist
results.sort() # 가나다 순으로 정렬
print(results)
print(len(results))

# text 작성: utf-8
with open(r'C:\Users\prude\PaddleOCR\custom_train\korean_number_plate_dict.txt', 'w', encoding='utf-8') as f:
    for row in results:
        f.write(row + '\n')

