# ppomppu
뽐뿌 크롤링

# Docker 기본 사용법
https://nicewoong.github.io/development/2017/10/09/basic-usage-for-docker/
https://www.slideshare.net/pyrasis/docker-fordummies-44424016

# k8s 기본 교육 사이트
https://www.youtube.com/playlist?list=PLF3s2WICJlqOiymMaTLjwwHz-MSVbtJPQ&app=desktop

참고자료 : k8s-exercise.zip

# Docker build 방법
폴더 안으로 들어가서 아래와 같이 실행 

- docker build -t ppomppu_monitor:latest .
- docker run -d -p 5003:5003 ppomppu_monitor:latest

- docker tag ppomppu_monitor:latest shclub/ppomppu_monitor:latest
- docker push shclub/ppomppu_monitor:latest

# AI Test
curl http://localhost:8888/postanal/\?post\=ilovekt


# K8S Dashboard
http://xxx.xxx.xxx.xxx:34000/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/#!/node?namespace=default

# k8s test
curl -X GET -H 'Content-Type:application/json'  http://10.110.66.17:8001/ppomppu_monitor -d  '{"param_list" : "ppomppu-anal-service,80,/postanal/?post=,0,Y,KT,Y,ppomppu-monitoring-db,8999,50026600,676003420:AAH7fq_HZzxbmWurz-IWdeUh6vZN1QTQxsE"}'

# docker-compose test
curl -X GET -H 'Content-Type:application/json' http://localhost:8001/ppomppu_monitor -d '{"param_list":"ppomppu-anal-service,8000,/postanal/?post=,0,Y,KT,Y,ppomppu-monitoring-db,27017,50026600,676003420:AAH7fq_HZzxbmWurz-IWdeUh6vZN1QTQxsE"}'

