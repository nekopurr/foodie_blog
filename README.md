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
6. 게시글 검색
7. 회원가입
8. 로그인
9. 사진 업로드

## 2. 개발 환경
- Python - 3.9.10
- django - 4.2.3
- sqlite3 - 3.35.5

## 3. 구조



## 4. DataBase 모델링
![image](https://github.com/nekopurr/foodie_blog/assets/85627591/0e9a829b-abac-4aa8-8a6e-93b7f9f18457)


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