//functions for landing page

const faqQuizFirst = document.getElementById("quiz-1")
const faqQuizSecond = document.getElementById("quiz-2")
const faqQuizThird = document.getElementById("quiz-3")
const headBtn = document.getElementById("head-btn")
const mainBtn = document.getElementById("main-btn")


faqQuizFirst.addEventListener("click", faqClick)
faqQuizSecond.addEventListener("click", faqClick)
faqQuizThird.addEventListener("click", faqClick)

headBtn.addEventListener("click", redirectMain)
mainBtn.addEventListener("click", redirectMain)


function redirectMain() {
    window.location = "http://127.0.0.1:5000/main"
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

