# ppomppu
뽐뿌 크롤링

# k8s 기본 교육 사이트
https://www.youtube.com/playlist?list=PLF3s2WICJlqOiymMaTLjwwHz-MSVbtJPQ&app=desktop

참고자료 : k8s-excercize.zip

# Docker build 방법
폴더 안으로 들어가서 아래와 같이 실행 

> docker build -t ppomppu_monitor:latest .
> docker run -d -p 5003:5003 ppomppu_monitor:latest

> docker tag ppomppu_monitor:latest shclub/ppomppu_monitor:latest
> docker push shclub/ppomppu_monitor:latest
