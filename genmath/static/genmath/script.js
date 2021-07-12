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
        console.log(m)
        MQ.StaticMath(m)
    }

    function isAlphabet(str) {
        return (/[a-zA-Z]/).test(str) && str.length == 1;
    }

    function isNum(num) {
        return (/[0-9]/).test(num);
    }


    var variables = [];
    variables.push('x');
    functioninput.addEventListener('keyup', (event) => {

        // var MQ = MathQuill.getInterface(2);
        // var mathdisplay = document.getElementById('math-display');
        // mathdisplay.innerHTML = functioninput.value
        // MQ.StaticMath(mathdisplay);
        if (functioninput.value === "") {
            while (variableinputs.length != 1) {
                let lastchild = variableinputs[variableinputs.length - 1]
                console.log(lastchild)
                variableparent.removeChild(lastchild)
        }
    }
        original.children[1].removeAttribute("value");  
        var key = event['key'];
        // console.log(variables)
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

    document.getElementById('form').onsubmit = function() {
        let func = functioninput.value
        let vars = {}
        for (variable of variables) {
            vars[variable] = document.getElementsByName('variable-' + variable)[0].value;
        }
        
        varvalues.setAttribute("value", JSON.stringify(vars))
    }

})