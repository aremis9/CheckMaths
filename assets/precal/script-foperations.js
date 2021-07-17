document.addEventListener('DOMContentLoaded', () => {

    var MQ = MathQuill.getInterface(2);

    var mathdisp = document.getElementsByClassName('math-disp');
    for (m of mathdisp) {
        MQ.StaticMath(m)
    }
    
    var selectedop = document.getElementsByClassName('select-op')[0]
})