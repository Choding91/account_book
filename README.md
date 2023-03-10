## π£ λλ§μ κ°κ³λΆ μλΉμ€

- μμ/μ§μΆ λ΄μ­ κΈ°λ‘ λ° κ΄λ¦¬ μλΉμ€ μ κ³΅

</br>

## πΒ Introduction

- κΈ°κ° : 2023.02.01 ~ 2023.02.04
- Solo : μ‘°μΈκ±Έ([Github](https://github.com/Choding91))

</br>

## π  Stacks

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">&nbsp;
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">&nbsp;
<img src="https://img.shields.io/badge/Django_rest_framework-A50E15?style=for-the-badge&logo=Django&logoColor=white">&nbsp;
<img src="https://img.shields.io/badge/MySQL-4169E1?style=for-the-badge&logo=MySQL&logoColor=white">&nbsp;

</br>

## π€Β Project Rules


### API

- [Notion](https://www.notion.so/API-baa0a4820226466b87bdbfd2938dc451)

</br>

### ERD

![image](https://user-images.githubusercontent.com/113072964/216600371-e905c3e0-38ba-4a3c-b7a9-56e4a68d3a0a.png)

</br>

## πΒ Structure

```
ββACCOUNT_BOOK
βββ account_book                    // project
β   βββ settings.py                 // setting
β   βββ urls.py                     // base url
β   βββ ...
βββ posts                           // app
β   βββ models.py                   // DB model - Post
β   βββ serializers.py              // serializers
β   βββ tests.py                    // test cases
β   βββ urls.py                     // posts url
β   βββ views.py                    // view functions
β   βββ ...
βββ users                           // app
β   βββ models.py                   // DB model - User
β   βββ serializers.py              // serializers
β   βββ tests.py                    // test cases
β   βββ urls.py                     // users url
β   βββ views.py                    // view functions
β   βββ ...
βββ .gitignore
βββ requirements.txt
βββ ...
```

</br>

## π»Β Development

#### κ΅¬νμ¨ : β(μλ£) / β(μΆκ° μμ νμ)

</br>

### μ μ  κΈ°λ₯

> [β] νμκ°μ : μ΄λ©μΌ/λΉλ°λ²νΈ μλ ₯, λΉλ°λ²νΈ μνΈν μ μ©

> [β] νμνν΄ : μ μ  μΈμ¦ μ¬λΆ νμΈ λ° μλΉμ€ μ΄μ© μ’λ£

> [β] λ‘κ·ΈμΈ : Simple JWT/Token(Access, Refresh) λ°κΈ

> [β] λ‘κ·Έμμ : Simple JWT/Blacklist μ μ©
>> λ‘μ»¬μ€ν λ¦¬μ§μ μ μ₯λλ ν ν° νΉμ±μ μλ²½ν λ‘κ·Έμμμ μν JS μΆκ° μμ νμ

</br>

### κ°κ³λΆ κΈ°λ₯(μΈμ¦λ μ μ λ§ μ΄μ© κ°λ₯)

> [β] μ μ²΄ μ‘°ν : κ°κ³λΆ λ΄μ­ μ μ²΄ μ‘°ν

> [β] λ±λ‘ : κ°κ³λΆ μ κ· λ±λ‘

> [β] μμΈ μ‘°ν : κ°κ³λΆ λ΄μ­ μμΈ μ‘°ν(+λ¨μΆ URL)
>> λ¨μΆ URL λΌμ΄ννμ μ€μ μ λν μΆκ° μμ νμ

> [β] λ³΅μ  : κ°κ³λΆ λ΄μ­ λ³΅μ 

> [β] μμ  : κ°κ³λΆ λ΄μ­ μμ 

> [β] μ­μ  : κ°κ³λΆ λ΄μ­ μ­μ 

</br>

## π Β Trouble Shooting

<details>
<summary>π κ°κ³λΆ λ³΅μ  μ λμΌν κ°κ³λΆμ λ?μ΄μ°κΈ° λλ λ¬Έμ </summary>

</br>

<div>

- μν© : κ°κ³λΆ λ³΅μ  κΈ°λ₯ κ΅¬ν μ€ κΈ°μ‘΄ κ°κ³λΆμ κ°μ λ΄μ©μ΄ λ?μ΄μ°κΈ° λλ λ¬Έμ  λ°μ(μμ  μκ°λ§ λ³κ²½λ¨)

![image](https://user-images.githubusercontent.com/113072964/216566037-5f7b4ab6-41bf-4090-ba9f-1778df1ce46a.png)

- ν΄κ²° : κΈ°μ‘΄ idκ°μΌλ‘ κ°κ³λΆλ₯Ό λ°μμ¨ λ€ idκ°λ§ None μ²λ¦¬νμ¬ μλ‘μ΄ κ°κ³λΆλ‘ μΈμ λ° λ±λ‘ κ°λ₯

![image](https://user-images.githubusercontent.com/113072964/216563082-b2f4cbb3-5520-4604-bed2-5461e0985196.png)

</div>
</details>
