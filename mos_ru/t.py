from get_token_from_curl import get_data_from_curl
from get_marks import get_marks

curl = '''curl "https://dnevnik.mos.ru/reports/api/progress/json?academic_year_id=10&student_profile_id=224645" ^
  -H "authority: dnevnik.mos.ru" ^
  -H "accept: application/json, text/plain, */*" ^
  -H "accept-language: ru-RU,ru;q=0.8" ^
  -H "auth-token: eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4MzQzIiwiYXVkIjoiMjoxIiwibmJmIjoxNjYzNzY2NDQ0LCJtc2giOiI3ZTA1YzM1Yi00MTBhLTQwZDItYTM1OS1kMmQyZjUyYTQ2OTYiLCJpc3MiOiJodHRwczpcL1wvc2Nob29sLm1vcy5ydSIsInJscyI6InsxOlsyMDoyOltdLDMwOjQ6W10sNDA6MTpbXSwxODM6MTY6W11dfSIsInptayI6ZmFsc2UsImV4cCI6MTY2NDYzMDQ0NCwiaWF0IjoxNjYzNzY2NDQ0LCJqdGkiOiI4MDRlYzIzYS1jNWQyLTQ5YTAtOGVjMi0zYWM1ZDIzOWEwYjUiLCJzc28iOiJhNjJlYmNiZS0zOTA3LTQ1YjgtOGQyYi00NWJiYmY4N2M3NzYifQ.XyQ4A9V17tlP5reypI_UHVivxRoR0OpudO3ATVbZyWwG4lcnXKstXKKJGab7W39bK1EnSf35XpWYvg9AB8q4Sb68PCVNMsPXwNfusSzB6rLJqS1vNBzBp547pPzYQK47AKkS7lIxRANwxv-eE3HHaf2styJ0X7eUG1IdsJqVL3_CQpbJu7VsTjl9JGZ49RvEXrvSdzkaVBy6Cp90z8mk-N6KYXtSvicuaYGfJjq_9YnZ4VgUdzdQmxgq-X1lCG-kwrXZDdsS-PKPjALs1XHcdtIvLBAo4MK_Ghgs8wWHEMyoAdnT5zoTaE8v3wVlztReMMPqQQ95CREUH27pDwH6Xg" ^
  -H "authorization: eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4MzQzIiwiYXVkIjoiMjoxIiwibmJmIjoxNjYzNzY2NDQ0LCJtc2giOiI3ZTA1YzM1Yi00MTBhLTQwZDItYTM1OS1kMmQyZjUyYTQ2OTYiLCJpc3MiOiJodHRwczpcL1wvc2Nob29sLm1vcy5ydSIsInJscyI6InsxOlsyMDoyOltdLDMwOjQ6W10sNDA6MTpbXSwxODM6MTY6W11dfSIsInptayI6ZmFsc2UsImV4cCI6MTY2NDYzMDQ0NCwiaWF0IjoxNjYzNzY2NDQ0LCJqdGkiOiI4MDRlYzIzYS1jNWQyLTQ5YTAtOGVjMi0zYWM1ZDIzOWEwYjUiLCJzc28iOiJhNjJlYmNiZS0zOTA3LTQ1YjgtOGQyYi00NWJiYmY4N2M3NzYifQ.XyQ4A9V17tlP5reypI_UHVivxRoR0OpudO3ATVbZyWwG4lcnXKstXKKJGab7W39bK1EnSf35XpWYvg9AB8q4Sb68PCVNMsPXwNfusSzB6rLJqS1vNBzBp547pPzYQK47AKkS7lIxRANwxv-eE3HHaf2styJ0X7eUG1IdsJqVL3_CQpbJu7VsTjl9JGZ49RvEXrvSdzkaVBy6Cp90z8mk-N6KYXtSvicuaYGfJjq_9YnZ4VgUdzdQmxgq-X1lCG-kwrXZDdsS-PKPjALs1XHcdtIvLBAo4MK_Ghgs8wWHEMyoAdnT5zoTaE8v3wVlztReMMPqQQ95CREUH27pDwH6Xg" ^
  -H "content-type: application/json;charset=UTF-8" ^
  -H "cookie: spa_id=0dea5746; at=1; disable_aupd_auth=; sbp_sid=000000000000000000000000000000000000; mos_id=rBEAAmJ/aksi7wke3//7AgA=; auth_flag=main; Ltpatoken2=h7ROOc1UE7szfF4N4VJVLaDJmdzzZkBp1xRc/VQMz2rqByZK7IJE5zBGtDTnBbz/aLQHodNC4BGMSL0I1giYWQxKBJguJ07QjJ1A3P71rQK+bgXWfNP/4xV9OsrRtXBcdk07wtw2cpHldSDNA548s2v1Y7ZTF6SITc190rViuNOZwQAuXfBmxvaY9cH8P9zEpEOuPE75UdcpLnGiU8pYR3B4dKJv+HPcJlVmy1KVXTCRfJkSht7Vj85Yu5ueUL/P1T3/9v7v+syF3mvW0rg8bNrhpW7bLQJ0hAYZsWy0I5YEIyROqC93jOWRqGfb2T9lumqsqMNsM1Vo8NeoKmsQ+A==; aupd_current_role=2:1; from_pgu=true; aid=10; auth_token=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4MzQzIiwiYXVkIjoiMjoxIiwibmJmIjoxNjYzNzY2NDQ0LCJtc2giOiI3ZTA1YzM1Yi00MTBhLTQwZDItYTM1OS1kMmQyZjUyYTQ2OTYiLCJpc3MiOiJodHRwczpcL1wvc2Nob29sLm1vcy5ydSIsInJscyI6InsxOlsyMDoyOltdLDMwOjQ6W10sNDA6MTpbXSwxODM6MTY6W11dfSIsInptayI6ZmFsc2UsImV4cCI6MTY2NDYzMDQ0NCwiaWF0IjoxNjYzNzY2NDQ0LCJqdGkiOiI4MDRlYzIzYS1jNWQyLTQ5YTAtOGVjMi0zYWM1ZDIzOWEwYjUiLCJzc28iOiJhNjJlYmNiZS0zOTA3LTQ1YjgtOGQyYi00NWJiYmY4N2M3NzYifQ.XyQ4A9V17tlP5reypI_UHVivxRoR0OpudO3ATVbZyWwG4lcnXKstXKKJGab7W39bK1EnSf35XpWYvg9AB8q4Sb68PCVNMsPXwNfusSzB6rLJqS1vNBzBp547pPzYQK47AKkS7lIxRANwxv-eE3HHaf2styJ0X7eUG1IdsJqVL3_CQpbJu7VsTjl9JGZ49RvEXrvSdzkaVBy6Cp90z8mk-N6KYXtSvicuaYGfJjq_9YnZ4VgUdzdQmxgq-X1lCG-kwrXZDdsS-PKPjALs1XHcdtIvLBAo4MK_Ghgs8wWHEMyoAdnT5zoTaE8v3wVlztReMMPqQQ95CREUH27pDwH6Xg; profile_id=224645; profile_roles=student; is_auth=true; user_id=208760; active_student=224645; cluster_id=1; JSESSIONID=node0vawn5ss03vc41drxtgyypenhm5653345.node0" ^
  -H "profile-id: 224645" ^
  -H "profile-type: student" ^
  -H "referer: https://dnevnik.mos.ru/diary/diary/marks" ^
  -H "sec-fetch-dest: empty" ^
  -H "sec-fetch-mode: cors" ^
  -H "sec-fetch-site: same-origin" ^
  -H "sec-gpc: 1" ^
  -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36" ^
  -H "x-mes-subsystem: familyweb" ^
  --compressed'''

token, st_id = get_data_from_curl(curl)
print(get_marks(token, st_id))
