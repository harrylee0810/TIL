





# Bootstrap

## Flex

Flexbox Layout은, 새롭게 CSS3 명세에 반영된 레이아웃 모듈로서, 요소들이 수용된 공간을 어떻게 효과적으로 채워나갈지에 대한 아이디어에서 시작된 새로운 레이아웃 방식 

(어떠한 박스가 있을 때, 박스들을 어떻게 정렬/배치 할지? )

Flexbox는 유연한 요소( `item` ), 그리고 그요소를 담을 그릇(`container` )으로 이루어짐. 그릇과 내용물 모두에게 이것이 Flexbox라는 일종의 고유한 선언을 해줘야함.

![](https://s3-us-west-2.amazonaws.com/s.cdpn.io/t-80/llflex1-01.png)



Flex 관련 reference

https://css-tricks.com/snippets/css/a-guide-to-flexbox/

http://www.beautifulcss.com/archives/1263

http://flexboxfroggy.com/#ko

### Flex의 속성

-----

#### **display**

그릇에 해당하는 부모 요소(이하,  container라 칭함)에 `display: flex` 혹은 `display: inline-flex` 로 flexbox임을 선언 할 수 있음.

```css
.container { display: flex }
```



#### **justify-content**

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

#### align-items

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

#### flex-direction

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



#### order

flex요소의 순서를 지정  기본 값은 0이며 양수나 음수로 변경 가능

```css
#pond {
    display: flex;
}
.yellow {
    order:1 
}
```



#### align-self

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



#### flex-wrap

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



#### flex-flow

빈번히 사용되는flex-direction 과 flex-wrap을 축약하여 사용

```css
#pond {
	display: flex;
    flex-flow: column wrap;
}
```



#### align-content

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



# Responsive Web

반응형 웹: **반응형 웹 디자인**(responsive web design, RWD)이란 하나의 웹사이트에서 PC, 스마트폰, 태블릿 PC 등 접속하는 [디스플레이](https://ko.wikipedia.org/wiki/%EB%94%94%EC%8A%A4%ED%94%8C%EB%A0%88%EC%9D%B4)의 종류에 따라 화면의 크기가 자동으로 변하도록 만든 웹페이지 접근 기법을 말한다.

CSS 및 HTML을 사용하여 내용을 조정, 숨기기, 축소, 확대 또는 이동하여 화면에서 보기 좋게 만드는 형식



## View port

view port는 가로 해상도를 의미하며, 웹페이지의 사용자가 볼 수 있는 영역을 말함.

여태껏 우리는 VS CODE 자동 완성 기능을 통해 view port를 meta tag로서 head 요소 안에 넣어 놓고 진행 해옴.

```html
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

뷰포트는 모바일기기에 화면이 로드 되었을 때, 페이지가 적정 해상도로 로드 될수 있도록 돕고 확대나 축소를 허용할 것인지 결정 해줌.

뷰포트는 장치에 따라 다름 (휴대폰화면은 컴퓨터 화면 보다 작음) 



## Media query

media query는 화면의 종류와 크기에 따라서 디자인을 달리 줄 수 있는 CSS의 기능. 

특히 최근의 트랜드인 반응형 디자인의 핵심 기술이라고 할 수 있음.

[media query]: https://www.youtube.com/watch?v=y3Zx-nVH25s	"생활코딩 media query 강의"



### 기본구성(syntax)

---

```css
@media only|not mediatype and|not|,(or) (media feature) { CSS스타일코드;}
```

- not: 부정
- only: 말 그대로 only; 이것만
- media type(매체유형)
  - all(모든 미디어; 기본값)
  - screen(화면이 달린 기기; 스마트폰, 태블릿 PC등)
  - print(프린터 기기)
  - braille(점자표시장치)
  - tv(음성과 영상이 동시 출력되는 TV)
- and 또는 , (or): 조건
- media feature(표현식): 특정 조건을 입력. 예) `min-width: 800px`



### Media query의 대표적인 조건

----

#### width

- viewport의 너비를 의미하며, 일반적으로 가장 많이 사용 하는 조건.
- h2 태그의 색상을 기본적으로 녹색으로 설정하며, 너비가 800px이 되면, 노란색으로 색상이 변경됨

```css
h2 {
    color: green;
}

@media (width: 800px) {
    h2 {
        color: yellow;
    }
}

```



#### min-width  / max-width

- h3태그의 기본 색상은 회색
- viewport의 너비가 min 600 px 와 max 800 px 조건을 만족할 경우, 색상이 보라색으로 변경됨

```css
h3 {
    color:gray;
}

@media (min-width:600px) and (max-width: 800px) {
    h3 {
        color: purple;
    }
}
```



#### height /  min-height / max-height

- h4 태그의 기본색상은 Orange
- viewport의 높이(세로 길이)가 min 400 px 와 max 600 px을 만족할 경우, 색상은 검정으로 변경됨

```css
h4 {
    color: orange;
}
@media (min-height: 400px) and (max-height: 600px) {
    h4 {
        color: black;
    }
}
```



#### orientation

- 가상 선택자 `::after`  을 활용하여, view port의 방향에 따라 조건 적용
- view port의 방향이 가로일때는 '가로입니다' 출력
- view port의 방향이 세로일때는 '세로입니다' 출력

```css
h1.ori::after {
    content: '가로입니다'

}

@media (orientation: portrait) {
    h1.ori::after {
        content: '세로입니다.'
    }
}
```



#### 응용:  Bootstrap의 Break point 흉내내기

``` css
/* Extra small: 0~576px */
.rainbow {
    color: red;
}

/* Small: 576px 이상 */
@media (min-width: 576px) {
    .rainbow {
        color: orange;
    }
}

/* Medium: 768px 이상 */
@media (min-width: 768px) {
    .rainbow {
        color: yellow;
    }
}

/* Large: 992px 이상 */
@media (min-width: 992px) {
    .rainbow {
        color: green;
    }
}

/* Extra Large: 1200px 이상 */
@media (min-width: 1200px) {
    .rainbow {
        color: blue;
    }
}
```



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



