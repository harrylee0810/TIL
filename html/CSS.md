# CSS

CSS(Cascading Stype Sheets):  마크업 언어(HTML)이 실제 표시되는 방법을 기술하는 언어

HTML이 웹사이트의 몸체를 담당한다면,  CSS는 옷, 엑세서리와 같이 웹사이트를 꾸미는 역할을 담당한다.

- Bootstrap:  트위터를 만든 회사에서 만든 CSS Framework를 제공하는 사이트

  (http://bootstrapk.com/)

- CSS Framework를 활용하면, HTML의 스타일을 직접 하지 않고, 적절한 디자인을 적용할 수 있음.

  (HTML Style을 도와주는 서비스 혹은 라이브러리의 개념)

특정 태그들을 골라내는 역할? 선택자? 셀렉터



### CSS 기본 구성

```html
<!DOCTYPE html>
<html lang="en">
    <head>
		<style>
            h1 {
                color: red;
        </style>
    </head>
```

- `h1` : 선택자
- `color` : 속성(property) 
- `aqua`  : 값(value)
- `{}` : 선언 블록
- `color: aqua;` : 선언문
- `h1(선택자) + {color: red;}(선언블록)` : 규칙(Rule)
- `규칙 묶음` : 스타일 시트(stylesheet)



### CSS 스타일의 종류

**1) Inline style (인라인 스타일)**

```html
<head>
	<section id="web">
        <ul style="list-style-type: circle;">
            <li>HTML</li>
            <li>CSS</li>
        </ul>
    </section>
</head>
```

**2) Embedding style (stye tag 사용하기)**

```html
<head>
    <style>
        h1 {
            color: red;
    </style>
</head>
```

**3) Link style (css 파일 link)**

```html
<head>
    <link rel="stylesheet" href="style.css">
</head>
```



### 선택자의 종류

**1) 전체 선택자**

- 선택자에 `*` 을 사용 할 경우, head 및 body 안의 모든 내용에 스타일이 적용 됨.

```CSS
<head>
    <style>
        * {
            color: red;
        }
    </style>
</head>
<body>
    <p>Red, 전체 선택자</p>
</body>
```

**2) 태그 선택자**

- 스타일을 적용하고 싶은 태그명을 선택자에 입력하면, 그 태그에만 스타일이 적용됨.

```css
<head>
    <style>
        h1 {
            color: rosybrown;
        }
    </style>
</head>
<body>
    <h1>rosybrown, 태그 선택자</h1>
</body>
```

**3) 클래스 선택자**

- 사용자가 지정한 클래스에 대하여 스타일을 적용함.
- 클래스를 `class="blue"` 와 같이 적용하고자 하는 태그에 클래스를 지정.
- 선택자에는 `.blue` 와 같이, `.` 을  클래스 앞에 반드시 입력해줘야 함.

```css
<head>
    <style>
        .blue {
            color: blue;
        }
    </style>
</head>
<body>
    <h2 class="blue">blue, .클래스 선택자</h2>
</body>
```

**4) 아이디 선택자**

- ​사용자가 지정한 아이디에 대하여 스타일을 적용함.
- 아이디는 html문서안에 유일하게 하나만 가질 수 있음.
- 아이디를 `id="green"` 와 같이, 적용하고자 하는 태그에 아이디를 지정.
- ​선택자에는 `#green` 와 같이, `#` 을 아이디 앞에 반드시 입력해줘야 함.

```css
<head>
    <style>
        #green {
            color: green;
        }
    </style>
</head>
<body>
    <h3 id="green">green, #아이디 선택자</h3>
</body>
```



### 선택자의 우선순위

- 태그 vs 클래스: 클래스 선택자 우선
- 태그 vs 아이디: 아이디 선택자 우선
- 태그 vs 아이디 vs 클래스: 아이디 선택자 우선
- 최종 우선 순위: 아이디 > 클래스 > 태그 > 전체 (요소들의 갯수 순서대로 라고 볼 수 있음)

```html
<body>
    <!-- vs. -->
    <!-- id > class > tag > *  -->
    
    <!-- 태그 vs 클래스: 클래스 -->
    <h1 class="blue">h1 vs .blue</h1>
    
    <!-- 태그 vs 아이디: 아이디 -->
    <h1 id="green">h1 vs #green</h1>
    
    <!-- 태그 vs 아이디 vs 클래스: 아이디 -->
    <h1 id="green" class="blue">h1 vs #green vs class</h1>
    
</body>
```



#### 한 문장내 특정 부분에 각각 다른  스타일을 적용하고 싶을 때?

- `span`  태그 이용

```html
<body>
    <p>나는 <span class="blue">파랑색</span>이고 싶고, 
       여기는<span class="pink">핑크색</span>이고 싶을 때는?</p>
</body>
```



#### CSS에서 색상을 적용하는 방법

1. Color name
2. Color code
3. rgb 
4. rgba : a(alpha)의 범위는 0.0~1.0 으로 값이 작아 질 수록, 색이 투명해짐.

```html
<head>
    <style>
        /* 1. color name */
        h1 {color: red;}
        
        /* 2. color code */
        h2 {color: #0000ff;}
        
        /* 3. rgb() */
        h3 {color: rgb(0,255,0);}
        
        /* 4. rgba() */
        /* 4. a(alpha): 0.0 ~ 1.0 */
        p {color: rgba(255,0,0,0.5)}   
    </style>
</head>
<body>
    <h1>빨간색</h1>
    <h2>파란색</h2>
    <h3>초록색</h3>
    <p>흐릿한 빨간색(투명도)</p>
</body>
```



### CSS font-sizes(단위 길이)

https://www.w3schools.com/css/css_units.asp

**1) 문서 전체의 단위 길이 적용**

```html
<head>
    <style>
        /* 단위 길이(font-size) */
        html {font-size: 10px;}
</head>
```



**2) rem  &  em**

- 단위 길이를 다른 요소들고 비교하여 상대적으로 정함.

- `rem` : Root Element (html)의 폰트사이즈가 기준이 됨.

  - 1.2 rem =>  10 px(html)  * 1.2 = 12 px

- `em` : 상위 Element의 폰트사이즈가 기준이 됨.

  - `<li class="em">저는 1.2em입니다.</li>` 에서, `li < ul < body < head`  순의 상위 Element 로 이동하여 기준 폰트사이즈를 찾음.

  - `ul`의 폰트 사이즈는 `1.2 em`  &  `li`의 폰트 사이즈는 `1.2 em`

  - 따라서, 최종적으로 10px(html)  * 1.2(ul)  *  1.2(ul안의 li)  = 14.4 px 

    

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        /* 단위 길이(font-size) */
        html {font-size: 10px;}
        
   		/* rem: html에 정의된 font-size에 비례 */
    	ol {font-size: 1.2rem;}
        /* 10px * 1.2 = 12px */
    
    	/* em: 자신의 상위 요소의 font-size에 비례 */
    	ul {font-size: 1.2em;}
    
        .em {font-size: 1.2em;}
        /* 10px(html) * 1.2(ul) * 1.2(ul li) = 14.4px */
     </style>
</head>

<body>
     <ol>
        <li>저는 1.2rem입니다.</li>
    </ol>
    <ul>
        <li class="em">저는 1.2em입니다.</li>
    </ul>  
</body>
```



**3)  vh(viewpoint height) & vw(viewpoint height) **

- 사용자가 보고있는 브라우져의 세로,가로 길이 (상대적인 값)
- 브라우져의 크기를 의도적으로 수정할 경우, 폰트 사이즈의 크기가 자동으로 변경됨.

```html
<head>
    <style>
        .vh {font-size: 5vh;}
        .vw {font-size: 5vw;}
    </style>
</head>

<body>
    <span class="vh">5vh</span>
    <span class="vw">5vw</span>
</body>
```



### CSS Box Model

모든 HTML 요소들은 박스로 간주 할 수 있으며, CSS Box Model은 문서의 design과 layout을 일컫음.  

기본 구성 요소 (https://www.w3schools.com/css/css_boxmodel.asp 참조)

- Content

- Padding

- Margin

- Border

  

**1)  box-sizing / width / height**

- `box-sizing` : 박스 크기의 기준을 설정할 수 있음. (기본: `content-box` )
  - 세로 & 가로 길이가 각각 100px 이며, `box-sizing: border-box;` 인 경우, `border-box` 전체의 세로 가로 길이가 100px을 의미한다.
- `width & height` : 박스의 너비 & 높이

```html
<head>
    <style>
        box {
            box-sizing: content-box;
            width: 100px;
            height: 100px;
         }      
    </style>
</head>
```



**2) padding & margin**

```html
<head>
    <style>
        box {
            /* 안쪽 여백 */
            padding-top: 25px; 
            padding-right: 25px;
            padding-bottom: 25px;
            padding-left: 25px;
            /*margin: 25px 20px 15px 10px ; 바깥쪽 여백 */
            margin-top: 25px; 
            margin-right: 25px;
            margin-bottom: 25px;
            margin-left: 25px;
         }      
    </style>
</head>
```





padding: 안쪽여백

marging: 바깥쪽 여백

상하좌우 모두 동시에 적용됨.

방향에 따라 따로 여백 조정?



