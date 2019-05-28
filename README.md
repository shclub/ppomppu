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

# docker-compose.yaml
version: '3'

services:
  ppomppu_monitor:
    image: shclub/ppomppu_monitor:latest
    ports:
     - "8001:5003"
    depends_on:
     - ppomppu-monitoring-db
     - ppomppu-anal-service

  ppomppu-monitoring-db:
    image: mongo
    ports:
      - "8999:27017"
    volumes:
      - 'mongodb_data:/test'

  ppomppu-anal-service:
    image: naihil/ppomppu:v2
    ports:
     - "80:8000"

volumes:
  mongodb_data:
    driver: local

