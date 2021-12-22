# Byzantine-Fault-Tolerance

케이스 1, 2 모두 비잔틴 노드가 General3 입니다.

 

이미지는 제가 push한 토커 허브에 있는 이미지를 가져오는 방식을 택했습니다.

 

이미지, 컨테이너 이름, 포트 번호의 쌍은 다음과 같습니다.

 |이미지 명|컨테이너 명|포트번호|
|------|---|---|
|p1_commander|p1_commander_con|5000|
|p1_general1|p1_general1|5001|
|p1_general2|p1_general2|5002|
|p1_general3|p1_general3|5003|


 |이미지 명|컨테이너 명|포트번호|
|------|---|---|
|p2_commander|p2_commander_con|5000|
|p2_general1|p2_general1|5001|
|p2_general2|p2_general2|5002|
|p2_general3|p2_general3|5003|
|p2_general3|p2_general4|5004|

 
결과 값은 

curl http://localhost:5000/ping

을 통해 확인하였습니다.
![케이스 1번](https://user-images.githubusercontent.com/74190329/146796470-e7e490dd-1a75-4c38-af36-08f00698b503.png)

![케이스 2번](https://user-images.githubusercontent.com/74190329/146796527-14abbcfa-22b4-4488-a55a-9e01eed2f166.png)



