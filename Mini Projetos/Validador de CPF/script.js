function removeNonDigits(cpf) {
    return cpf.replace(/\D/g, '');
}

function validateCPF(cpf) {
    cpf = removeNonDigits(cpf);
    
    if (cpf.length !== 11) {
        return false;
    }
  
    if (cpf === cpf[0].repeat(11)) {
        return false;
    }
    
    
    let total = 0;
    for (let i = 0; i < 9; i++) {
        total += parseInt(cpf[i]) * (10 - i);
    }
    
    let remainder = total % 11;
    let firstCheck = remainder < 2 ? 0 : 11 - remainder;
    
    if (parseInt(cpf[9]) !== firstCheck) {
        return false;
    }
    
   
    total = 0;
    for (let i = 0; i < 10; i++) {
        total += parseInt(cpf[i]) * (11 - i);
    }
    
    remainder = total % 11;
    let secondCheck = remainder < 2 ? 0 : 11 - remainder;
    
    if (parseInt(cpf[10]) !== secondCheck) {
        return false;
    }
    
    return true;
}

function formatCPF(cpf) {
    cpf = removeNonDigits(cpf);
    if (cpf.length !== 11) {
        return cpf;
    }
    return `${cpf.slice(0, 3)}.${cpf.slice(3, 6)}.${cpf.slice(6, 9)}-${cpf.slice(9)}`;
}


function applyCPFMask(input) {
    let value = input.value.replace(/\D/g, '');
    
    if (value.length > 0) {
        value = value.substring(0, 11);
        
        if (value.length <= 3) {
            input.value = value;
        } else if (value.length <= 6) {
            input.value = `${value.slice(0, 3)}.${value.slice(3)}`;
        } else if (value.length <= 9) {
            input.value = `${value.slice(0, 3)}.${value.slice(3, 6)}.${value.slice(6)}`;
        } else {
            input.value = `${value.slice(0, 3)}.${value.slice(3, 6)}.${value.slice(6, 9)}-${value.slice(9)}`;
        }
    }
}


function showResult(isValid, cpf) {
    const resultDiv = document.getElementById('result');
    const formattedCPF = formatCPF(cpf);
    
    
    resultDiv.classList.remove('valid', 'invalid', 'hidden');
    
   
    resultDiv.classList.add(isValid ? 'valid' : 'invalid');
    
   
    const messageEl = resultDiv.querySelector('.result-message');
    const cpfEl = resultDiv.querySelector('.result-cpf');
    
    messageEl.textContent = isValid ? 'CPF Válido!' : 'CPF Inválido!';
    cpfEl.textContent = formattedCPF;
}

function clearResult() {
    const resultDiv = document.getElementById('result');
    resultDiv.classList.add('hidden');
    resultDiv.classList.remove('valid', 'invalid');
}

function clearInput() {
    document.getElementById('cpfInput').value = '';
    clearResult();
    document.getElementById('cpfInput').focus();
}


document.addEventListener('DOMContentLoaded', function() {
    const cpfInput = document.getElementById('cpfInput');
    const validateBtn = document.getElementById('validateBtn');
    const clearBtn = document.getElementById('clearBtn');
    
    
    cpfInput.addEventListener('input', function() {
        applyCPFMask(this);
        clearResult();
    });
    
   
    validateBtn.addEventListener('click', function() {
        const cpf = cpfInput.value.trim();
        
        if (!cpf) {
            alert('Por favor, digite um CPF!');
            cpfInput.focus();
            return;
        }
        
        const isValid = validateCPF(cpf);
        showResult(isValid, cpf);
    });
    
    
    clearBtn.addEventListener('click', clearInput);
    
    
    cpfInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            validateBtn.click();
        }
    });
    

    cpfInput.focus();
});

