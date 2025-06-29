// Executa quando a página é carregada: exibe os dados atuais da tabela
window.onload = function () {
    carregarEquipamentos();
};

// Função para capturar os dados do formulário e enviar para a API
function novoEquipamento() {
    const campos = [
        "nome", "temperatura_ar", "temperatura_processo", "rpm",
        "torque", "desgaste_ferramenta", "twf", "hdf", "pwf", "osf", "rnf"
    ];
    const data = {};
    let incompleto = false;

    // Valida se todos os campos foram preenchidos
    campos.forEach(campo => {
        const valor = document.getElementById(campo).value;
        if (valor === "") {
            incompleto = true;
        }
        data[campo] = valor;
    });

    // Mostra mensagem se houver campos vazios
    if (incompleto) {
        document.getElementById("mensagem-pesquisa").textContent = "⚠️ Preencha todos os campos antes de diagnosticar.";
        return;
    }

    // Envia os dados via POST para a API
    fetch('/api/adicionar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            ...data,
            temperatura_ar: parseFloat(data.temperatura_ar),
            temperatura_processo: parseFloat(data.temperatura_processo),
            rpm: parseInt(data.rpm),
            torque: parseFloat(data.torque),
            desgaste_ferramenta: parseInt(data.desgaste_ferramenta),
            twf: parseInt(data.twf),
            hdf: parseInt(data.hdf),
            pwf: parseInt(data.pwf),
            osf: parseInt(data.osf),
            rnf: parseInt(data.rnf)
        })
    })
    .then(res => res.json())
    .then(res => {
        // Mostra mensagem de confirmação e resultado da predição
        document.getElementById("mensagem-pesquisa").textContent = res.message || "Diagnóstico realizado.";
        carregarEquipamentos();
        alert(res.falha_detectada ? "⚠️ Falha detectada" : "✅ Operação normal");

        // Limpa os campos do formulário
        campos.forEach(campo => document.getElementById(campo).value = "");
    })
    .catch(err => console.error('Erro:', err));
}

// Busca todos os registros e atualiza a tabela HTML
function carregarEquipamentos() {
    fetch('/api/listar')
        .then(res => res.json())
        .then(dados => {
            const tabela = document.querySelector("#tabelaEquipamentos tbody");
            tabela.innerHTML = '';
            dados.forEach(item => {
                const row = tabela.insertRow();
                for (let campo of [
                    'nome','temperatura_ar','temperatura_processo','rpm',
                    'torque','desgaste_ferramenta','twf','hdf','pwf','osf','rnf'
                ]) {
                    let cell = row.insertCell();
                    cell.textContent = item[campo];
                }

                // Coluna de diagnóstico
                const diag = row.insertCell();
                diag.textContent = item.resultado ? "Falha" : "Normal";

                // Botão de exclusão
                const del = row.insertCell();
                const btn = document.createElement('button');
                btn.textContent = "Delete";
                btn.onclick = () => deletarEquipamento(item.nome);
                del.appendChild(btn);
            });
        });
}

// Chama a API para deletar equipamento pelo nome
function deletarEquipamento(nome) {
    fetch(`/api/deletar/${nome}`, { method: 'DELETE' })
        .then(res => res.json())
        .then(res => {
            alert(res.message);
            carregarEquipamentos();
        });
}

// Alterna a visibilidade da tabela entre visível e oculto
function toggleTabela() {
    const botao = document.querySelector('.listar-btn');
    const container = document.getElementById("tabela-container");
    const atual = window.getComputedStyle(container).display;
    if (atual === "none") {
        carregarEquipamentos();
        container.style.display = "block";
        botao.textContent = 'Ocultar Equipamentos';
    } else {
        container.style.display = "none";
        botao.textContent = 'Listar Equipamentos';
    }
}

// Pesquisa registros por nome digitado no campo
function pesquisarEquipamento() {
    const nome = document.getElementById("nome").value;
    if (!nome) {
        document.getElementById("mensagem-pesquisa").textContent = "⚠️ Digite um nome para pesquisar.";
        return;
    }

    document.getElementById("mensagem-pesquisa").textContent = "";
    fetch(`/api/pesquisar/${nome}`)
        .then(res => {
            if (!res.ok) throw new Error("Equipamento não encontrado");
            return res.json();
        })
        .then(dados => {
            const tabela = document.querySelector("#tabelaEquipamentos tbody");
            tabela.innerHTML = '';
            dados.forEach(item => {
                const row = tabela.insertRow();
                for (let campo of [
                    'nome','temperatura_ar','temperatura_processo','rpm',
                    'torque','desgaste_ferramenta','twf','hdf','pwf','osf','rnf'
                ]) {
                    let cell = row.insertCell();
                    cell.textContent = item[campo];
                }

                const diag = row.insertCell();
                diag.textContent = item.resultado ? "Falha" : "Normal";

                const del = row.insertCell();
                const btn = document.createElement('button');
                btn.textContent = "Delete";
                btn.onclick = () => deletarEquipamento(item.nome);
                del.appendChild(btn);
            });

            // Mostra a tabela e atualiza botão após pesquisa
            document.getElementById("tabela-container").style.display = "block";
            document.querySelector(".listar-btn").textContent = "Ocultar Equipamentos";
        })
        .catch(err => document.getElementById("mensagem-pesquisa").textContent = "❌ " + err.message);
}