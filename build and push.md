```
docker build -t qpdh1924/p1_commander .\Problem1\Commander\;
docker build -t qpdh1924/p1_general1 .\Problem1\General1\;
docker build -t qpdh1924/p1_general2 .\Problem1\General2\;
docker build -t qpdh1924/p1_general3 .\Problem1\General3\;

docker build -t qpdh1924/p2_commander .\Problem2\Commander\;
docker build -t qpdh1924/p2_general1 .\Problem2\General1\;
docker build -t qpdh1924/p2_general2 .\Problem2\General2\;
docker build -t qpdh1924/p2_general3 .\Problem2\General3\;
docker build -t qpdh1924/p2_general4 .\Problem2\General4\;

docker push qpdh1924/p1_commander;
docker push qpdh1924/p1_general1;
docker push qpdh1924/p1_general2;
docker push qpdh1924/p1_general3;

docker push qpdh1924/p2_commander;
docker push qpdh1924/p2_general1;
docker push qpdh1924/p2_general2;
docker push qpdh1924/p2_general3;
docker push qpdh1924/p2_general4;
```
