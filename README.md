# Django를 이용한 Pinterest 서비스
Django모듈을 이용하여 Pinterest 웹페이지 서비스 만들기


## ⌨️ 프로젝트 소개
Django모듈을 이용하여 웹페이지 제작 및 운영하는 서비스를 제공합니다.


## 🕰️ 개발 기간 
- 23.07.11. ~ 23.09.10 


## ⚙️ 개발환경
- Python 3.9.0
- Django 4.2.3
- Django-bootstrap4 23.2
- django-environ 0.10.0
- gunicorn 21.2.0
- nginx 1.19.5
- mariadb 10.5


## 🔎 개발 과정
- 프로젝트 초기 설정
  - pragmatic: 메인 설정 폴더로, Django의 핵심 설정을 포함합니다.
     - settings: 기본 Django 설정 파일
     - deploy.py: 배포 환경에 대한 설정을 포함합니다.
     - local.py : 개발 환경에 대한 설정을 포합합니다.

- 계정 관련 기능
  - accountapp: 사용자의 계정 생성 및 삭제 관련 기능을 처리합니다.
     - 계정 생성, 로그인, 로그아웃 기능 구현
     - 계정 삭제 및 수정 기능 구현
 
 - 게시글 및 내용 관련 기능
   - articleapp: 사용자가 게시글을 게시, 수정, 삭제할 수 있게 합니다.
      - 게시글 생성, 수정, 삭제 기능 구현
      - 게시글 목록 및 상세 페이지 구현
   - commentapp: 게시글에 댓글을 달 수 있는 기능을 제공합니다.
      - 댓글 작성, 수정, 삭제 기능 구현
      - 댓글 표시 기능 구현  
   - likeapp: 사용자가 게시글에 좋아요를 표시할 수 있게 합니다.
      - 좋아요 추가 및 취소 기능 구현
      - 게시글별 좋아요 수 표시   
   - projectapp: 여러 게시글을 그룹화하여 표시합니다.
      - 게시글 그룹 생성 및 관리 기능 구현

 - 사용자 개인화 기능
   - profileapp: 사용자의 개인 정보 및 마이페이지 관련 기능을 제공합니다.
      - 사용자 프로필 표시 및 수정 기능
   - subscribeapp: 사용자가 다른 사용자를 구독하는 기능을 제공합니다.
      - 구독 추가 및 취소 기능
      - 댓글 표시 기능 구현
      - 구독 목록 표시
    
  - 프론트엔드 구성
    - static: 프로젝트에서 사용하는 정적 파일들을 저장합니다.
       - 폰트, 매직 그리드 등의 스타일 및 스크립트 파일 보관
    - templates: 기본적인 웹 페이지 구조를 정의하는 템플릿 파일들을 보관합니다.
       - base.html: 모든 웹 페이지의 기본 구조를 정의
       - footer.html: 웹 페이지의 바닥글 부분 템플릿
       - header.html: 웹 페이지의 헤더 부분 템플릿
       - head.html: 웹 페이지의 <head> 부분 템플릿

## 🔎 배포 방법
- AWS EC2 인스턴스 생성
 - 원하는 사양의 EC2 인스턴스를 생성
 - 필요한 경우, 보안 그룹 설정을 통해 특정 포트 (예: 80, 8000)을 열어줍니다.
- Docker 설치
    ```bash
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io
    ```
- Portainer 설치
  ```
  docker volume create portainer_data
  docker run -d -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
  ```
- Docker Swarm 초기화
  ```
  docker swarm init
  ```
- Django 프로젝트 Dockerize
  - Dockerfile을 이용해 이미지를 생성합니다.
- Docker Stack 배포
  - docker-compose.yml을 이용해 Docker Stack을 배포합니다.


## 📌 주요기능

#### 1. Article
- 원하는 게시물을 게시할 수 있습니다.
#### 2. Projects
- 올린 게시글을 묶어서 볼 수 있습니다.
#### 3. Subscription
- 구독한 사용자의 게시글을 따로 볼 수 있습니다.
#### 4. MyPage / login
- 로그인이 되어 있지 않다면 login 기능, 로그인이 되어있다면 프로필사진, 상태메시지 등을 수정할 수 있는 마이페이지가 있습니다.
#### 5. SignUp
- 계정을 생성할 수 있습니다.


## 📌 테스트 화면
![메인페이지](https://github.com/runacian0221/DjangoPJT/assets/123911214/cc34bb3b-5212-4882-8ca4-fe456b23bef1)



