## masonite(メゾナイト)

## 環境構築

```shell
$ python -m venv env
$ source env/bin/activate
$ pip install --upgrade pip
$ pip install masonite-cli

$ craft new exmaple
$ cd exmaple/
$ craft install
$ craft serve --reload
```

## URL

```
http://localhost:8000/
```

## マイグレーション
```shell
$ craft migration create_blog_table --create blogs
$ craft migrate
$ craft model models/Blog
```

## コントローラー＆View作成