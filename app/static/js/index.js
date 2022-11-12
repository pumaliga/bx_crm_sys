const productFirst = document.getElementById("product1")
const productSecond = document.getElementById("product2")
const faqQuizFirst = document.getElementById("quiz-1")
const faqQuizSecond = document.getElementById("quiz-2")
const faqQuizThird = document.getElementById("quiz-3")


productFirst.addEventListener("mouseover", respondMouseOver)
productSecond.addEventListener("mouseover", respondMouseOver)

productFirst.addEventListener("mouseout", respondMouseOut)
productSecond.addEventListener("mouseout", respondMouseOut)

faqQuizFirst.addEventListener("click", faqClick)
faqQuizSecond.addEventListener("click", faqClick)
faqQuizThird.addEventListener("click", faqClick)


function respondMouseOver(e) {
    let product = e.target
    if (product.id === "product1") {
        product.src = 'http://127.0.0.1:5000/static/images/shoes2.png'
    } else {
        product.src = 'http://127.0.0.1:5000/static/images/shoes4.png'
    }
}

function respondMouseOut(e){
    let product = e.target
    if(product.id === "product1"){
        product.src = 'http://127.0.0.1:5000/static/images/product1.png'
    } else {
        product.src = 'http://127.0.0.1:5000/static/images/product2.png'
    }
}

function faqClick(e){
    let numb_quiz = e.target.id
    let answerId = `answer-${numb_quiz.slice(-1)}`
    let div_answer = document.getElementById(answerId)
    if(div_answer.style.display === 'block'){
        e.target.style.transform = 'rotate(0)'
        div_answer.style.display = 'none';
    } else {
        e.target.style.transform = 'rotate(45deg)'
        div_answer.style.display = 'block';
    }
}





