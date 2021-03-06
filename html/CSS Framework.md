[TOC]



# CSS Framework

## Introduction

까다로운 CSS 레이아웃을 손쉽게 만들어주는 소프트웨어 프레임 워크

> A CSS framework is a software framework that is meant to allow for easier, more standards-compliant web design using the Cascading Style Sheets language.



CDN를 통해 Bootstrap에 작성된 CSS, JS를 활용하자!



### 1. CDN

**CDN: Content Deliver(Distribution) Network**

컨텐츠(CSS, JS, Image, Text등)을 효율적으로 전달 하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템. 

(컴퓨터에 폰트가 없는 경우, 구글에서 제공하는 웹폰트를 사용하여 적용하는 것과 비슷한 방식)

- 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)
- 외부 서버를 활용함로써 본인 서버의 부하가 적어짐
- CDN은 보통 적절한 수준의 캐시 설정으로 빠르게 로딩 할 수 있음.



cf) Reboot / Reset CSS / normalize CSS

​     브라우져가 들고 있는 CSS를 초기화시킴. (모든 브라우져에서 똑같이 보이게 하기 위한  친구)



### 2. Bootstrap 기본 설정

Bootstrap의 CSS와 자바스크립트(JS)를 CDN을 통해 활용하기 위해 아래의 코드를 적용

```HTML
#CSS
<head>
   <link rel="stylesheet" 	 href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
</head>



<body>
    
#JS 
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>   
</body>
```



## Utilities

### 1. spacing

- margin과 padding 등 여백과 공간을 설정

  https://getbootstrap.com/docs/4.2/utilities/spacing/

```html
<body>
    <-- margin -->
    <h1 class="m-0"> margin의 space를 전부 0으로 </h1>
    <h1 class="mx-0"> x축(좌,우) space를 0으로 </h1>
    <h1 class="my-0"> y축(위,아래) space를 0으로 </h1>
    <h1 class="mt-0"> 위 space를 0으로 </h1>
    <h1 class="mb-0"> 아래 space를 0으로 </h1>
    <h1 class="ml-0"> 왼쪽 space를 0으로 </h1>
	<h1 class="mr-0"> 오른쪽 space를 0으로 </h1>
    
    <-- padding -->
    <h1 class="p-0"> padding의 space를 전부 0으로 </h1>
    <h1 class="px-0"> x축(좌,우) space를 0으로 </h1>
    <h1 class="py-0"> y축(위,아래) space를 0으로 </h1>
    <h1 class="pt-0"> 위 space를 0으로 </h1>
    <h1 class="pb-0"> 아래 space를 0으로 </h1>
    <h1 class="pl-0"> 왼쪽 space를 0으로 </h1>
	<h1 class="pr-0"> 오른쪽 space를 0으로 </h1>
   
    <-- 브라우져의 기본 rem은 16px -->
    <h1 class="m-0"> 0은 0rem 	=> 0px </h1>
    <h1 class="m-1"> 1은 0.25rem => 4px </h1>
    <h1 class="m-2"> 2은 0.5rem  => 8px </h1>
    <h1 class="m-3"> 3은 1rem    => 16px </h1>
    <h1 class="m-4"> 4은 1.5rem  => 24px </h1>
    <h1 class="m-5"> 5은 3rem    => 48px </h1>
     
    <-- 음수도 가능 -->
    <h1 class="mt-n5"> margin의 위(top)의 space를 -48px 
        			   (=48px만큼 위로 이동) 		
    </h1>    
    
    <-- 자동으로 설정 -->
    <h1 class="m-auto"> space를 자동으로 설정 </h1>      

</body>
```



### 2. Color

- 텍스트 및 배경의 색상을 설정 (https://getbootstrap.com/docs/4.2/utilities/colors/)



**1) text color**

![](https://www.freewebmentor.com/wp-content/uploads/2017/09/bootstrap-text-color-css-classes.png)



**2)  back ground color**

![bg color](https://www.beststarsofyear.com/wp-content/uploads/2018/07/new-page-background-color-bootstrap-lovely-bootstrap-4-everything-you-of-page-background-color-bootstrap.jpg)



**3) 예시 코드**

```html
<body>
    <-- background: primary 색상 / text: sucess 색상 적용 -->
    <p class="bg-primary text-success">Lorem ipsum dolor sit</p>
</body>
```



### 3. border

```html
<body>
    <-- 테두리 삽입 -->
    <p class="border">Lorem ipsum dolor sit</p>
        
    <-- 테두리 색상을 Primary로 변경(border을 넣고 추가로 border-이하를 삽입할 것) -->
    <p class="border border-primary">Lorem ipsum dolor sit</p>
    
    <-- 테두리 모양 변경 -->
    <p class="border border-rounded">박스 모서리만 둥글게</p>
    <p class="border border-rounded-circle">박스 전체를 둥글게</p>
    <p class="border border-rounded-pill">박스 양 끝을 둥글게(알약 모양)</p>
</body>
```



### 4. Display

```html
<body>
    <a class="d-block"> 태그 안의 내용을 블록 속성으로 변경 </a>
    <a class="d-inline"> 태그 안의 내용을 인라인 속성으로 변경 </a>
    <a class="d-inline-block"> 태그 안의 내용을 인라인-블록 속성으로 변경 </a>
    <a class="d-none"> 태그 안의 내용을 숨기기 </a>
    
    <a class="d-sm-none"> 태그 안의 내용을 sm보다 작을 때 none을 주기 
    					  sm; small device - 750px
        			      따라서, 태그안 내용이 750px보다 작으면 none이 됨.
    </a>
    
    <-- 테두리 색상을 Primary로 변경(border을 넣고 추가로 border-이하를 삽입할 것) -->
    <a class="border border-primary">Lorem ipsum dolor sit</p>
    

</body>
```

 

*Bootstrap의 breakpoint*

> ![breakpoint](https://wpmaster.com/wp-content/uploads/2017/02/bootstrap-4-grid.jpg)



### 5. Position

```html
<body>
    <a class="position-static"> 박스의 position을 static으로 설정 </a>
    <a class="position-aboslute"> 박스의 position을 absolute으로 설정 </a>
    <a class="position-relative"> 박스의 position을 relative으로 설정 </a>
    <a class="position-fixed"> 박스의 position을 fixed으로 설정 </a>
    
   	<-- fixed position은 추가로 고정 위치를 설정 할 수 있음 -->
    <a class="position-fixed fixed-top"> fixed + 위치는 위 </a>
    <a class="position-fixed fixed-bottom"> fixed + 위치는 아래 </a>
    <a class="position-fixed fixed-left"> fixed + 위치는 왼쪽 </a>
    <a class="position-fixed fixed-right"> fixed + 위치는 오른쪽 </a>
   
</body>
```



### 6. Text/Font

```html
<body>
   	<-- text 정렬  -->
    <a class="text-center"> 특정한 박스의 콘텐츠를 가운데 정렬 </a>
    <a class="text-right"> 특정한 박스의 콘텐츠를 오른쪽 정렬 </a>
    <a class="text-left"> 특정한 박스의 콘텐츠를 왼쪽 정렬 </a>
    <a class="position-fixed"> 박스의 position을 fixed으로 설정 </a>
        
   	<-- font style 적용  -->
    <a class="font-weight-normal"> text의 기본값(Default) </a>
    <a class="font-weight-bold"> text를 굵게 </a>
    <a class="font-weight-bolder"> text를 더 굵게 </a>
    <a class="font-weight-light"> text를 연하게 </a>
    <a class="font-weight-lighter"> text를 더 연하게 </a>    
    <a class="font-italic"> text를 기울임 </a>
        
</body>
```



### 7. Layout

- container: 기본으로 깔고 가는 bootstrap의 basic layout element
- 기본적으로 양쪽 끝에 공백이 있음.
- 공백을 최소화 하고 싶을땐? `.container-fluid` 입력

```html
<div class="container">
  <!-- Content here -->
</div>
```



### 8. Grid System

- 일련의 컨테이너, 행 및 열을 사용하여 내용을 정렬하고 구성하는 시스템.

- 12개의 열(Column)으로 기본적으로 나뉘어져 있음. 

  (열이 12개인 이유? 12개가 활용도가 제일 높음 / 약수 多)

- 기본적인 구성:  `container`  > `row`  > `col-4`  

```html
<div class="container">
  <div class="row">
    <div class="col-4 border border-primary">
```



![GRID SYSTEM EXAMPLE](https://dzone.com/storage/temp/891125-dzone1.jpg)



- 아래의 예시는 4칸씩 3개의 열을 구성함.

```html
<div class="container">
  <div class="row">
    <div class="col-4 border border-primary">
      One of three columns
    </div>
    <div class="col-4 border border-primary">
      One of three columns
    </div>
    <div class="col-4 border border-primary">
      One of three columns
    </div>
  </div>
</div>
```



-   `offset` 값을  추가로 입력하면,  컬럼 사이에 빈 공간을 만들 수 있음
- Grid system은 12칸이 Maximum으로 12칸을 초과하면 다음 줄로 넘어감

```html
<div class="container">
  <div class="row">
    <div class="col-4 border border-primary">
      One of three columns
    </div>
    <div class="offset-3 col-4 border border-primary">
      One of three columns
    </div>
    <div class="col-4 border border-primary">
      One of three columns
    </div>
  </div>
</div>
```



- 구분된 컬럼안에 또다시 컬럼을 세분화 하는 것도 가능함.

```html
<div class="container">
  <div class="row">
    <div class="col-3 border border-primary">
        <div class="row">
            <div class="col-4 border border-danger">1</div>
            <div class="col-4 border border-danger">2</div>
            <div class="col-4 border border-danger">3</div>
        </div>
      One of three columns
    </div>
  </div>
</div>
```



- break point를 활용하여 화면크기에 따라 컬럼 갯수를 다르게 설정할 수 있음.

  - 기본 설정: col-4  (4칸씩 3개의 박스가 2줄 생김)

  - 창이 768 px을 초과하면 컬럼을 2개씩 차지하는 것으로 변경

    (2칸씩 6개의 박스가 생김 => 1줄)

```html
<div class="container mb-5">
    <div class="row">
        <div class="col-4 col-md-2 border border-success">1</div>
        <div class="col-4 col-md-2 border border-success">3</div>
        <div class="col-4 col-md-2 border border-success">2</div>
        <div class="col-4 col-md-2 border border-success">4</div>
        <div class="col-4 col-md-2 border border-success">5</div>
        <div class="col-4 col-md-2 border border-success">6</div>
    </div>
</div>
```



Bootstrap의 breakpoint*

> ![breakpoint](https://wpmaster.com/wp-content/uploads/2017/02/bootstrap-4-grid.jpg)



### 9. Flex

Flexbox Layout은, 새롭게 CSS3 명세에 반영된 레이아웃 모듈로서, 요소들이 수용된 공간을 어떻게 효과적으로 채워나갈지에 대한 아이디어에서 시작된 새로운 레이아웃 방식 

(어떠한 박스가 있을 때, 박스들을 어떻게 정렬/배치 할지? )

Flexbox는 유연한 요소( `item` ), 그리고 그요소를 담을 그릇(`container` )으로 이루어짐. 그릇과 내용물 모두에게 이것이 Flexbox라는 일종의 고유한 선언을 해줘야함.

![](https://s3-us-west-2.amazonaws.com/s.cdpn.io/t-80/llflex1-01.png)



Flex 관련 reference

https://css-tricks.com/snippets/css/a-guide-to-flexbox/

http://www.beautifulcss.com/archives/1263

http://flexboxfroggy.com/#ko



**Flex의 속성**

------

**display**

그릇에 해당하는 부모 요소(이하,  container라 칭함)에 `display: flex` 혹은 `display: inline-flex` 로 flexbox임을 선언 할 수 있음.

```css
.container { display: flex }
```



**justify-content**

Flex의 요소를 가로선상에서 정렬

- `flex-start` : 요소들을 컨테이너의 왼쪽으로 정렬
- `flex-end` : 요소들을 컨테이너의 오른쪽으로 정렬
- `center` : 요소들을 컨테이너의 가운데로 정렬
- `space-between` : 요소들 사이에 동일한 간격 삽입
- `space-around` : 요소들 주위에 동일한 간격 삽입

```css
#pond {
	display: flex;
    justify-content: flex-start
}
```

![](https://images.thoughtbot.com/cp-design-for-the-web/rJPfdQBaR1toJmmH87ao_layout-justify-content.png)

**align-items**

Flex의 요소를 세로선상에서 정렬

- `flex-start` : 요소들을 컨테이너의 꼭대기로 정렬
- `flex-end` : 요소들을 컨테이너의 바닥으로 정렬
- `center` : 요소들을 컨테이너의 가운데로 정렬
- `baseline` : 요소들을 컨테이너의 시작 위치에 정렬
- `stretch` : 요소들을 컨테이너에 맞도록 늘림

```css
#pond {
	display: flex;
    align-items: flex-end;
}
```



![](https://images.thoughtbot.com/cp-design-for-the-web/SOtxyVsFR5uFGQAps9wW_layout-align-content.png)

**flex-direction**

Flex의 요소들이 정렬할 방향 지정

- `row` : 요소들을 텍스트의 방향과 동일하게 정렬
- `row-reverse` : 요소들을 텍스트의 반대 방향으로 정렬
- `column` : 요소들을 위에서 아래로 정렬
- `column-reverse` : 요소들을 아래에서 위로 정렬

```css
#pond {
	display: flex;
    flex-direction: row-reverse;
}
```

![](https://images.thoughtbot.com/cp-design-for-the-web/MwnTUG5TBaJHUM7hnMaw_layout-flex-direction.png)



**order**

flex요소의 순서를 지정  기본 값은 0이며 양수나 음수로 변경 가능

```css
#pond {
    display: flex;
}
.yellow {
    order:1 
}
```



**align-self**

flex 내 개별 요소에 적용할 수 있는 또 다른 속성.

이 속성은 align-items가 사용하는 값들을 인자로 받으며, 그 값들은 지정한 요소에만 적용됨.

- `flex-start` : 특정 요소를 컨테이너의 꼭대기로 정렬
- `flex-end` : 특정 요소를 컨테이너의 바닥으로 정렬
- `center` : 특정 요소를 컨테이너의 가운데로 정렬
- `baseline` : 특정 요소를 컨테이너의 시작 위치에 정렬
- `stretch` : 특정 요소를 컨테이너에 맞도록 늘림

```css
#pond {
	display: flex;
    align-items: flex-start;
}
.yellow {
    align-self: flex-end 
}
```



**flex-wrap**

flex요소를 한줄 또는 여러줄에 걸쳐 정렬

- `nowrap` : 모든요소를 한줄에 정렬
- `wrap` : 요소들을 여러줄에 걸쳐 정렬
- `wrap-reverse` : 요소들을 여러줄에 걸쳐 반대로 정렬 (오른쪽 하단부터...)

```css
#pond {
	display: flex;
    flex-wrap: wrap;
}
```

![](https://images.thoughtbot.com/cp-design-for-the-web/Flonm9P5TgSzWVtiqFyR_layout-flex-wrap.png)



**flex-flow**

빈번히 사용되는flex-direction 과 flex-wrap을 축약하여 사용

```css
#pond {
	display: flex;
    flex-flow: column wrap;
}
```



**align-content**

여러 줄 사이의 간격을 지정

- `flex-start`: 여러 줄들을 컨테이너의 꼭대기에 정렬
- `flex-end`: 여러 줄들을 컨테이너의 바닥에 정렬
- `center`: 여러 줄들을 세로선 상의 가운데에 정렬
- `space-between`: 여러 줄들 사이에 동일한 간격 적용
- `space-around`: 여러 줄들 주위에 동일한 간격 적용
- `stretch`: 여러 줄들을 컨테이너에 맞도록 늘림

이 속성을 사용하는 방법이 어려울 수 있습니다. `align-content`는 여러 줄들 사이의 간격을 지정하며, `align-items`는 컨테이너 안에서 어떻게 모든 요소들이 정렬하는지를 지정합니다. 한 줄만 있는 경우, `align-content`는 효과를 보이지 않습니다.

```css
#pond {
	display: flex;
    flex-wrap: wrap;
	align-content: flex-start
}
```

![](https://images.thoughtbot.com/cp-design-for-the-web/9IoOcGARiqjCjtCGARkw_layout-align-items.png)













## Component

### 1. Alerts

- bootstrap에서 제공하는 기본적인 박스. 블록 속성을 가짐.
- 배경,테두리,글자 색을 추가로 적용 할 수 있음.

```html
<div class="alert alert-primary" role="alert">
    A simple primary alert—check it out!
</div>
```

예)

![alerts](https://i.stack.imgur.com/G7wXP.png)



### 2. Badge

- Alert와 달리, Inline-block 속성을 적용하고 싶은 단어에 적용

```html
<!-- Alert -->
<div class="alert alert-primary" role="alert">
    A simple primary alert—check it out!
</div>

<!-- Badge  -->
<h1>Example heading <span class="badge badge-secondary">New</span></h1>
```

예)

![badges](https://www.tutorialrepublic.com/lib/images/bootstrap-3.3/bootstrap-inline-labels.png)



### 3. Buttons

```html
<!--Default: 배경에 색이 적용되어 있음 -->
<button type="button" class="btn btn-primary">Primary</button>

<!-- outline: 배경은 투명, 윤곽선에 색 적용  -->
<button type="button" class="btn btn-outline-secondary">Secondary</button>

<!-- btn-lg/sm: 버튼 크기 크게/작게-->
<button type="button" class="btn btn-primary btn-lg">Large button</button>
<button type="button" class="btn btn-primary btn-sm">Small button</button>

<!-- btn-block: Display에 블럭 속성 적용(줄 전체에 버튼 적용) -->
<button type="button" class="btn btn-block">Block level button</button>

<!-- disabled: 클릭이 안되게, diabled하게 적용 -->
<button type="button" class="btn btn-lg" disabled>Button</button>

```



### Button group

```html
<!-- default -->
<div class="btn-group" role="group" aria-label="Basic example">
    <button type="button" class="btn btn-secondary">Left</button>
    <button type="button" class="btn btn-secondary">Middle</button>
    <button type="button" class="btn btn-secondary">Right</button>
</div>
<!-- btn-group-lg: 버튼 그룹 크기 크게 -->
<div class="btn-group btn-group-lg" role="group" aria-label="Basic example">
    <button type="button" class="btn btn-secondary">Left</button>
    <button type="button" class="btn btn-secondary">Middle</button>
    <button type="button" class="btn btn-secondary">Right</button>
</div>
<!--vertical: 버튼 그룹 세로로 -->
<div class="btn-group-vertical" role="group" aria-label="Basic example">
    <button type="button" class="btn btn-secondary">Left</button>
    <button type="button" class="btn btn-secondary">Middle</button>
    <button type="button" class="btn btn-secondary">Right</button>
</div>
```

예)

![button group](https://www.tutorialrepublic.com/lib/images/bootstrap-3.3/bootstrap-button-groups-height-sizing.png)



### 4. Card

```html
<div class="container">
    <div class="row">
        <div class="col-4">
            <div class="card">
                <img src="../images/mino.JPG" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">Some quick example....</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
            </div>
        </div>
    </div>
</div>
```

예)

![카드](https://i.ytimg.com/vi/2qQxwT-Qm5E/maxresdefault.jpg)

### 5. Carousel - With indicators

```html
<!-- carousel: 슬라이드 형태로 사진을 넘기는 기능 -->
<div class="container">
    <div id="carouselExampleIndicators" class="carousel slide" data-			ride="carousel">
        <ol class="carousel-indicators">
            <li data-target="#carouselExampleIndicators" data-slide-to="0" 				class="active"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="1">				</li>
            <li data-target="#carouselExampleIndicators" data-slide-to="2">				</li>
        </ol>
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="../images/1.JPG" class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
                <img src="../images/2.JPG" class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
                <img src="../images/3.JPG" class="d-block w-100" alt="...">
            </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleIndicators" 				role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleIndicators" 				role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
</div>
```

예)

![collapse](https://www.tutorialrepublic.com/lib/images/bootstrap-3.3/bootstrap-carousel.png)



### 6. collapse

- ​컨텐츠를 숨기고 보이는 플러그인.

```html
<p>
    <a class="btn btn-primary" data-toggle="collapse" href="#collapseExample" 	      role="button" aria-expanded="false" aria-controls="collapseExample">
        Link with href
    </a>
    <button class="btn btn-primary" type="button" data-toggle="collapse" data-			  target="#collapseExample" aria-expanded="false" aria-        					controls="collapseExample"> Button with data-target
    </button>
</p>
<div class="collapse" id="collapseExample">
    <div class="card card-body">
        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus 		 terry richardson ad squid. Nihil anim keffiyeh helvetica, craft beer 			labore wes anderson cred nesciunt sapiente ea proident.
    </div>
</div>
```

예)

![collapse](https://leamug.com/wp-content/uploads/2018/10/Bootstrap-Accordion.png)



### 7. Forms

- 아이디 / 패스워드 로그인 창과 같은 Form을 생성.

```html
<form>
    <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-			describedby="emailHelp" placeholder="Enter email">
        <small id="emailHelp" class="form-text text-muted">We'll never share 			your email with anyone else.</small>
    </div>
    <div class="form-group">
        <label for="exampleInputPassword1">Password</label>
        <input type="password" class="form-control" id="exampleInputPassword1" 			placeholder="Password">
    </div>
    <div class="form-group form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1">
        <label class="form-check-label" for="exampleCheck1">Check me 				  out</label>
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

예)



### 8. Input group

- input들의 묶음 예) button + input tag



### 9. Media object

```html
<div class="media">
    <img src="../images/mino.JPG" class="mr-3" alt="...">
    <div class="media-body">
        <h5 class="mt-0">Mino Seo</h5>
        	Cras sit amet nibh libero, in gravida nulla. Nulla vel metus 				scelerisque ante sollicitudin. Cras purus odio, vestibulum in 				vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi 			vulputate fringilla. Donec lacinia congue felis in faucibus.
    </div>
</div>
```

예)

![media object](https://www.codevscolor.com/wp-content/uploads/bootstrap-media-object-1.png)

### 10. Modal

```html
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-				target="#exampleModal">
    Launch demo modal
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-		 labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
                <button type="button" class="close" data-dismiss="modal" aria-l						   abel="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                모달 안의 내용을 적는 칸.
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-								dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save 									changes</button>
            </div>
        </div>
    </div>
</div>
```

예)

![Modal](https://jcblogimages.blob.core.windows.net/img/2014/07/image14.png)



### 11. Progress

```html
<div class="progress">
    <div class="progress-bar bg-success" role="progressbar" style="width: 50%;" 	aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">50%
    </div>
</div>
```

예)

![progress](https://www.tutorialrepublic.com/lib/images/bootstrap-3.3/bootstrap-striped-progress-bar-with-emphasis.png)



### 12. Spinners

- `<span class="sr-only">Loading...</span>` 부분을 빼도 정상적으로 작동을 함. 

- 그러나, 움직이는 이미지나 사진 등을 보지 못하는 유저를 위해 sr-only(screen reader) 클래스를 

  입력하여 이 이미지가 무엇인지 컴퓨터가 인식할 수  있음. (비슷한 예. `alt=value`)

```html
<div class="spinner-border" role="status">
  <span class="sr-only">Loading...</span>
</div>
```



예)

![spinner](https://designmodo.com/wp-content/uploads/2011/10/925.jpg)





https://bootstrapcreative.com/resources/bootstrap-4-css-classes-index/



### 13. Navbar

- 웹 페이지의 상단에 Navigation을 만드는 기능

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" 			data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-			  label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">					(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Link</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" 									id="navbarDropdown" role="button" data-										toggle="dropdown"
                        aria-haspopup="true" aria-expanded="false">
                        Dropdown
                    </a>
                    <div class="dropdown-menu" aria-												labelledby="navbarDropdown">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#">Something else 							here</a>
                    </div>
                </li>
                <li class="nav-item">
                    <a class="nav-link disabled" href="#" tabindex="-1" aria-						disabled="true">Disabled</a>
                </li>
            </ul>
            <form class="form-inline my-2 my-lg-0">
                <input class="form-control mr-sm-2" type="search" 								   placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success my-2 my-sm-0" 								type="submit">Search</button>
            </form>
        </div>
    </nav>
```

예)

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTozOPy6ijF-Pd3D9tNTUJIW4ho7R4CVDTbS3ZQENnP9IVuyW_NGg)



### 14. Pagination

- 페이지 이동/넘기기 버튼 적용

```html
<div class="container">
    <nav aria-label="Page navigation example">
        <ul class="pagination">
            
            <-- disabled: 페이지 비활성화 -->
            <li class="page-item disabled"><a class="page-link" 							href="#">Previous</a></li>
                
            <li class="page-item"><a class="page-link" href="#">1</a></li>
                
            <-- disabled: 해당 버튼 활성화 -->
            <li class="page-item active" aria-current="page">
                <a class="page-link" href="#">2 <span class="sr-only">(current)					  </span></a>
            </li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item"><a class="page-link" href="#">Next</a></li>
        </ul>
    </nav>
</div>
```

예)

![](https://i.stack.imgur.com/hTCT3.png)





- `<div class="container"> ` 을 쓰면  페이지 양 끝에 빈 공간이 생김!



## break point

Bootstrap의 break point를 활용하여 view port의 width에 따라 컬럼 갯수를 다르게 설정할 수 있음.

- 576px보다 작을 때: col-12 조건 적용 => 한줄에 12칸을 차지하는 박스 생성 (총 12줄)
- 576px보다 클때: col-sm-6 조건 적용 => 한줄에 6칸을 차지하는 박스 생성 (총 6줄)
- 768px보다 클때: col-md-4 조건 적용 => 한줄에 4칸을 차지하는 박스 생성 (총 4줄)
- 992px보다 클때: col-lg-3 조건 적용 => 한줄에 3칸을 차지하는 박스 생성 (총 3줄)
- 1200px 보다 클때: col-xl-2 조건 적용 => 한줄에 2칸을 차지하는 박스 생성 (총 2줄)

상기 조건을 활용하여, view point에 따라 박스를 숨기는 등의 추가적인 속성도 적용 가능

- view port가 small(576px ~ 768px) 일 경우, 마지막 박스는 숨겨짐

```css
<div class="container">
    <div class="row">
        <div class="d-sm-none col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">01</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">02</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">03</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">04</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">05</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">06</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">07</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">08</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">09</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">10</div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">11</div>
        <div class="d-sm-none col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">12</div>
    </div>
</div>
```



*Bootstrap의 breakpoint*

> ![breakpoint](https://wpmaster.com/wp-content/uploads/2017/02/bootstrap-4-grid.jpg)

