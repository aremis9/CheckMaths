document.addEventListener('DOMContentLoaded', () => {

    const functioninput = document.getElementById('functioninput');
    var variableparent = document.getElementsByClassName('variableinputs')[0];
    var variableinputs = document.getElementsByClassName('variableinputs')[0].children;
    var original = document.getElementsByClassName('variableinput')[0];

    var MQ = MathQuill.getInterface(2);
    // var mathdisplay = document.getElementById('math-display');
    // mathdisplay.style.textAlign = "center"
    // mathdisplay.innerHTML = functioninput.value
    // MQ.StaticMath(mathdisplay);

    var mathdisp = document.getElementsByClassName('math-disp');
    for (m of mathdisp) {
        MQ.StaticMath(m)
    }

    function isAlphabet(str) {
        return (/[a-zA-Z]/).test(str) && str.length == 1;
    }


    var variables = [];
    variables.push('x');

    for (variableinput of variableinputs) {
        let vinputclass = variableinput.classList[variableinput.classList.length - 1];
        let vinputvar = vinputclass.slice(-1);
        if (!variables.includes(vinputvar)) {
            variables.push(vinputvar)
            variables.sort()
        }
    }

    if (!functioninput.value.includes('x')) {
        original.style.display = 'none'
    }

    functioninput.addEventListener('keyup', (event) => {
        fvalue = functioninput.value
        for (i in fvalue) {
            if (isAlphabet(fvalue.slice(i)) && !variables.includes(fvalue.slice(i))) {
                variables.push(fvalue.slice(i));
                variables.sort();
                // console.log(variables);
                duplicate(fvalue.slice(i))
            }
        }

        if (functioninput.value === "") {
            original.getElementsByClassName('vinput')[0].value = ''
            original.style.display = 'none  '
            while (variableinputs.length != 1) {
                let lastchild = variableinputs[variableinputs.length - 1]
                variableparent.removeChild(lastchild)
            }
        }

        // original.children[1].removeAttribute("value");  
        var key = event['key'];
        // console.log(variables)
        if (key == 'A') {
            console.log('a')
        }

        if (isAlphabet(key) && !variables.includes(key)) {
            variables.push(key);
            variables.sort();
            // console.log(variables);
            duplicate(key)
        }


        for (variable of variables) {
            if (functioninput.value.indexOf(variable) < 0) {
                variables.splice(variables.indexOf(variable), 1)
            }
        }


        for (variableinput of variableinputs) {
            let vinputclass = variableinput.classList[variableinput.classList.length - 1];
            let vinputvar = vinputclass.slice(-1);
            if (!variables.includes(vinputvar)) {
                if (vinputclass == "variable-x") {
                    variableinput.style.display = "none";
                }
                else {
                    variableinput.remove()
                }
            }
        }

    })



    function duplicate(variable) {
        var clone = original.cloneNode(true);
        clone.style.display = "flex";
        clone.classList.remove("variable-x");
        clone.classList.add("variable-" + variable);
        var label = clone.children[0];
        var input = clone.children[1];
        label.innerHTML = variable + " = ";
        input.setAttribute("name", "variable-" + variable);
        input.removeAttribute("value");
        input.placeholder = "Enter value of '" + variable + "'";
        // console.log(label, input);

        original.parentNode.appendChild(clone);
        // console.log(clone);
    }




    var varvalues = document.createElement("input");
    varvalues.setAttribute("hidden", "");
    varvalues.setAttribute("type", "text")
    varvalues.setAttribute("name", "variables")
    functioninput.parentNode.insertBefore(varvalues, functioninput.nextSibling);

    var form = document.getElementById('form')
    form.onsubmit = function() {
        let func = functioninput.value
        let vars = {}
        for (variable of variables) {
            vars[variable] = document.getElementsByName('variable-' + variable)[0].value;
        }
        
        varvalues.setAttribute("value", JSON.stringify(vars))
        form = document.getElementById('form')
    }


})