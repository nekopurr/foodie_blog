# foodie_blog
맛집 블로그

## 1. 목표 및 기능

### 1.1 목표
- django에 익숙해지기
- 맛집 정보와 직접 만든 음식을 공유하는 커뮤니티 사이트

### 1.2 기능
1. 메인페이지 구현 (완료)
2. 게시글 작성 (완료)
3. 게시글 상세보기 (완료)
4. 게시글 수정 (완료)
5. 게시글 삭제 (완료)
6. 게시글 작성일 (당일이면 시간, 당일이 아닐 시 날짜)
7. 게시글 검색
8. 회원가입
9. 로그인
10. 사진 업로드

## 2. 개발 환경
- Python - 3.9.10
- django - 4.2.3
- sqlite3 - 3.35.5

## 3. 구조
```
foodie_blog
├─ .gitignore
├─ app
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ views.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ blog
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_alter_post_title_alter_post_writer_comment.py
│  │  ├─ 0003_category_post_category.py
│  │  ├─ 0004_alter_category_name.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ templates
│  │  └─ blog
│  │     ├─ post_detail.html
│  │     ├─ post_edit.html
│  │     ├─ post_list.html
│  │     └─ post_write.html
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ manage.py
├─ README.md
├─ static
│  ├─ chat.css
│  ├─ common.css
│  ├─ css
│  ├─ img
│  │  ├─ first.png
│  │  ├─ icon-search.png
│  │  ├─ icon-x.png
│  │  ├─ last.png
│  │  ├─ next.png
│  │  └─ prev.png
│  ├─ list.css
│  ├─ login-join.css
│  ├─ table.css
│  ├─ view.css
│  └─ write.css
└─ templates
   ├─ base.html
   └─ index.html
```

## 4. DataBase 모델링
![image](https://github.com/nekopurr/foodie_blog/assets/85627591/0e9a829b-abac-4aa8-8a6e-93b7f9f18457)

## 5. 실행 화면
### 5.1 메인 입장
![01_main](https://github.com/nekopurr/foodie_blog/assets/85627591/b165af81-b7ff-43a0-8b44-f809f1d0dd3b)

### 5.2 글 쓰기
![02_write](https://github.com/nekopurr/foodie_blog/assets/85627591/0d49a0f2-5719-4a33-a393-3fee03fc3e43)

### 5.3 글 수정
![03_edit](https://github.com/nekopurr/foodie_blog/assets/85627591/91b506a8-1c2b-4618-b078-abef132be901)

### 5.4 글 삭제
![04_delete](https://github.com/nekopurr/foodie_blog/assets/85627591/41d4645e-25fd-4247-98df-23b18c9fddaf)
