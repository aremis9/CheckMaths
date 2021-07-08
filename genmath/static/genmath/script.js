document.addEventListener('DOMContentLoaded', () => {

    const functioninput = document.getElementById('functioninput');

    function isAlphabet(char) {
        return (/[a-z]/i).test(char);
    }

    functioninput.addEventListener('keyup', (event) => {
        console.log(isAlphabet(event['key']))
        console.log(event['key'])
    })


})