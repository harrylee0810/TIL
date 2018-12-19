# DAY03

문제 1.

문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

```PYTHON
str = input('문자를 입력하세요: ')
print(str[0]) #첫번째 글자
print(str[-1]) #마지막 글자
```

문제 2.

자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```

```



* git clone 'githup개인주소'

### git 활용법

----

1. git status
2. git add .  (. 은 현재폴더를 의미)
3. git commit -m "메세지명"
4. 깃헙 동기화
   * git push (커밋했던 내용을 업로드)



### VSCode 단축키

----

`ctrl+D` 동기화해서 한꺼번에 수정하기

`html:5` : 기본적인 html 구조, 템플릿을 불러와줌.



# HTML & CSS



HTML: Hypertext Markup 언어.  웹페이지를 만드는 컴퓨터 언어

CSS(Cascading Stype Sheets):  마크업 언어(HTML)이 실제 표시되는 방법을 기술하는 언어

HTML이 웹사이트의 몸체를 담당한다면,  CSS는 옷, 엑세서리와 같이 웹사이트를 꾸미는 역할을 담당한다.

* Bootstrap:  트위터를 만든 회사에서 만든 CSS Framework를 제공하는 사이트

  (http://bootstrapk.com/)

* CSS Framework를 활용하면, HTML의 스타일을 직접 하지 않고, 적절한 디자인을 적용할 수 있음.

  (HTML Style을 도와주는 서비스 혹은 라이브러리의 개념)


HTML을 꾸미는 도구/Tool ? CSS

* 특정 태그들을 골라내는 역할? 선택자? 셀렉터


## HTML의 구성

```html
<!DOCTYPE html> 
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title> 
    </head>
    <body>
    </body>
</html>
```

### 태그

#### 구역 구분

1. `<title> </title>` : 웹브라우져 Tab에 나타나는 HTML문서의 제목 (제목정보 담는 태그)

2. `<p> </p>` : 구문/단락 구분하는 태그

3. `<br>`  : Line breaking;  줄을 나누는 태그. 닫는 태그는 필요 없음. 뒤에 입력 
   * `<ul> </ul>`  + `<li> </li>` 
   * `<ol> </ol>` +  `<li> </li>` 

4. `<div> </div> & <span> </span>`  : 콘텐츠의 영역이나 그룹화를 할 때 사용(내용 블럭 잡기)
   * `div` 는 배경색이 레이아웃 가로 모두에 적용
   * `span`은 다른텍스트와 구별하기 위해 사용. 배경색은 글자가 있는 곳만 적용



###  텍스트 스타일 수정 태그

`<b> </b>`  : 텍스트 강조 (Bold)

`<i> </i>` : 텍스트 기울임 (Italic)

`<u> </u>` : 텍스트 밑줄 (Underline)



### CSS 속성

```html
  		<style>
            h1 { 
                color: red;
            }
            h2 {
                color: blue;
            }
            h3 {
                color: red;
            }
        </style>
```



같은 속성을 구분하지 않고 한꺼번에 수정하기?

```html
        <style>
            h1,h3 { 
                color: red;
            }
            h2 {
                color: blue;
            }
        </style>
```



```html
<h4 id="green"> 이것은 h4 태그입니다.</h4>
```

id: 전체문서에서 딱 하나만 입력 가능. 태그의 고유한  id 값 입력

```html
        <style>
            #green {
                color: green;
            }
            .yellow {
                color: yellow;
            }
        </style>
```

#id 입력하여 id로 지정된 태그 내용을 style을 쉽게 수정할 수 있음



```php+HTML
<h5 class="yellow">이것은 h5 태그입니다.</h5>
<h6 class="yellow">이것은 h6 태그입니다.</h6>
```

class: 어떠한 반에 속해 있는지?  같은 문서내에 여러번 사용 가능

```html
        <style>
            .yellow {
                color: yellow;
            }
        </style>
```

`.class명`  을 입력하여 class로 지정된 태그 내용을 style을 쉽게 수정할 수 있음



#### inline style

해당하는 태그 내에서 직접 입력도 가능

인라인 스타일로 들어간 것이 가장 우선순위 둠.

우선순위

 인라인 스타일 > ID > CLASS







`ctrl + /`  : 주석 입력하기





