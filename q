[33mcommit 4f6581f62701b83b27ecd76d145942016d6bc71f[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mSorfina[m[33m, [m[1;31morigin/Sorfina[m[33m)[m
Author: Nur sorfina <sorfinafaisal@gmail.com>
Date:   Wed Sep 4 10:59:52 2024 +0800

    change background color
    This reverts commit 9c496c2fc7e206fed96191921ef7b7c0de7f5b7f.

[1mdiff --git a/MMU-pic.jpg b/MMU-pic.jpg[m
[1mnew file mode 100644[m
[1mindex 0000000..cb71d25[m
Binary files /dev/null and b/MMU-pic.jpg differ
[1mdiff --git a/Sorfina/create_account.py b/Sorfina/create_account.py[m
[1mdeleted file mode 100644[m
[1mindex e6e991f..0000000[m
[1m--- a/Sorfina/create_account.py[m
[1m+++ /dev/null[m
[36m@@ -1,11 +0,0 @@[m
[31m-from flask import Flask, render_template[m
[31m-[m
[31m-app = Flask(__name__)[m
[31m- [m
[31m-[m
[31m-@app.route('/')[m
[31m-def home():[m
[31m-    return render_template('index.html')[m
[31m-[m
[31m-if __name__== '__main__':[m
[31m-    app.run(debug=True)[m
\ No newline at end of file[m
[1mdiff --git a/Sorfina/index.html b/Sorfina/index.html[m
[1mdeleted file mode 100644[m
[1mindex 6956d5d..0000000[m
[1m--- a/Sorfina/index.html[m
[1m+++ /dev/null[m
[36m@@ -1,83 +0,0 @@[m
[31m-<!DOCTYPE html>[m
[31m-<html lang="en">[m
[31m-<head>[m
[31m-    <meta charset="UTF-8">[m
[31m-    <meta name="viewport" content="width=device-width, initial-scale=1.0">[m
[31m-    <title>MMU CLUB MANAGEMENT</title>[m
[31m-    <style>[m
[31m-        body {[m
[31m-            margin: 0;[m
[31m-            font-family: 'Times New Roman', Times, serif;[m
[31m-            height: 100vh;[m
[31m-            display: flex;[m
[31m-            flex-direction: column;[m
[31m-        }[m
[31m-[m
[31m-        .header {[m
[31m-            background-color: #f5f5f5;[m
[31m-            padding: 10px;[m
[31m-            text-align: center;[m
[31m-            font-size: 24px;[m
[31m-            font-weight: bold;[m
[31m-            border-bottom: 1px solid #ccc;[m
[31m-        }[m
[31m-[m
[31m-        .container {[m
[31m-            display: flex;[m
[31m-            flex: 1;[m
[31m-            width: 100%;[m
[31m-            height: calc(100vh - 60px); /* Adjusted for header height */[m
[31m-            position: relative;[m
[31m-        }[m
[31m-[m
[31m-        .sidebar {[m
[31m-            position: fixed;[m
[31m-            top: 0;[m
[31m-            left: 0;[m
[31m-            width: 60px;[m
[31m-            background-color: #f5f5f5;[m
[31m-            display: flex;[m
[31m-            flex-direction: column;[m
[31m-            align-items: center;[m
[31m-            padding-top: 20px;[m
[31m-            border-right: 1px solid #ccc;[m
[31m-            height: 100%;[m
[31m-            z-index: 1000; /* Ensure visibility */[m
[31m-        }[m
[31m-[m
[31m-        .content {[m
[31m-            flex-grow: 1;[m
[31m-            padding: 20px;[m
[31m-            background-color: #fff;[m
[31m-            position: relative;[m
[31m-            margin-left: 60px; /* Make space for the sidebar */[m
[31m-        }[m
[31m-[m
[31m-        img {[m
[31m-            width: 40px;[m
[31m-            height: 40px;[m
[31m-            margin-bottom: 20px;[m
[31m-        }[m
[31m-[m
[31m-        .chat-icon {[m
[31m-            position: absolute;[m
[31m-            bottom: 20px;[m
[31m-            right: 20px;[m
[31m-        }[m
[31m-    </style>[m
[31m-</head>[m
[31m-<body>[m
[31m-    <div class="header">[m
[31m-        MMU CLUB MANAGEMENT[m
[31m-    </div>[m
[31m-    <div class="container">[m
[31m-        <div class="sidebar">[m
[31m-            <img src="{{ url_for('static', filename='home_icon.png') }}" alt="Home">[m
[31m-            <img src="{{ url_for('static', filename='menu_icon.png') }}" alt="Menu">[m
[31m-        </div>[m
[31m-        <div class="content">[m
[31m-            <img src="{{ url_for('static', filename='chat_icon.png') }}" alt="Chat" class="chat-icon">[m
[31m-        </div>[m
[31m-    </div>[m
[31m-</body>[m
[31m-</html>[m
[1mdiff --git a/admin_page.py b/admin_page.py[m
[1mdeleted file mode 100644[m
[1mindex 10c07b2..0000000[m
[1m--- a/admin_page.py[m
[1m+++ /dev/null[m
[36m@@ -1,15 +0,0 @@[m
[31m-from flask import Flask[m
[31m-from  flask_sqlalchemy import SQLAlchemy[m
[31m-from flask_admin import Admin[m
[31m-[m
[31m-db = SQLAlchemy()[m
[31m-Admin = Admin()[m
[31m-[m
[31m-def admin_page():[m
[31m-    app = Flask(__name__)[m
[31m-    app.config("SQLALCHEMY_DATABASE_URL") == "sqlite:///db.sqlite3"[m
[31m-[m
[31m-    db.init_app(app)[m
[31m-    Admin.init_app(app)[m
[31m-[m
[31m-    return app[m
[1mdiff --git a/create_account.py b/create_account.py[m
[1mindex 76a660b..68ae51c 100644[m
[1m--- a/create_account.py[m
[1m+++ b/create_account.py[m
[36m@@ -12,3 +12,4 @@[m [mdef home():[m
 [m
 if __name__ == '__main__':[m
     app.run(debug=True)[m
[41m+ [m
\ No newline at end of file[m
[1mdiff --git a/index.html b/index.html[m
[1mindex e754cdd..3eb0d05 100644[m
[1m--- a/index.html[m
[1m+++ b/index.html[m
[36m@@ -4,7 +4,6 @@[m
     <meta charset="UTF-8">[m
     <meta name="viewport" content="width=device-width, initial-scale=1.0">[m
     <title>MMU CLUB MANAGEMENT</title>[m
[31m-    <!-- Font Awesome -->[m
     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">[m
     <style>[m
         body {[m
[36m@@ -13,10 +12,11 @@[m
             height: 100vh;[m
             display: flex;[m
             flex-direction: column;[m
[32m+[m[32m            background-color: #ffffff[m
         }[m
 [m
         .header {[m
[31m-            background-color: #f5f5f5;[m
[32m+[m[32m            background-color: #868df0;[m
             padding: 10px;[m
             text-align: center;[m
             font-size: 35px;[m
[36m@@ -31,7 +31,7 @@[m
 [m
         .sidebar {[m
             width: 60px;[m
[31m-            background-color: #f5f5f5;[m
[32m+[m[32m            background-color: #868df0;[m
             display: flex;[m
             flex-direction: column;[m
             align-items: center;[m
