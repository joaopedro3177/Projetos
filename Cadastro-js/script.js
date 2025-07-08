function GuardarDados() {
    let nome = window.prompt('Qual é o seu nome?')// Se cancelar, retorna 'Não informado'
    let idade = window.prompt('Qual é a sua idade?')
    let sexualidade = window.prompt('Qual é a sua identidade de gênero?')
    let consentimento = window.confirm('Você concorda que seus dados serão armazenados?'); // true/false

    let dados = {
        nome,
        idade,
        sexualidade,
        consentimento
    }

    console.log(dados);
    return dados;
}

GuardarDados();

