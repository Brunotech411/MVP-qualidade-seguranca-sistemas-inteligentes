// Carregar dados ao iniciar
document.addEventListener("DOMContentLoaded", function () {
    carregarEquipamentos();
});

// Carrega equipamentos salvos no banco
function carregarEquipamentos() {
    fetch("http://127.0.0.1:5000/equipamentos")
        .then(response => response.json())
        .then(data => {
            data.equipamentos.forEach(e => inserirTabela(e));
        });
}

// Envia equipamento para diagnóstico e salva no banco
function novoEquipamento() {
    const formData = new FormData();
    formData.append("nome", document.getElementById("nome").value);
    formData.append("temperatura_ar", document.getElementById("temperatura_ar").value);
    formData.append("temperatura_processo", document.getElementById("temperatura_processo").value);
    formData.append("rpm", document.getElementById("rpm").value);
    formData.append("torque", document.getElementById("torque").value);
    formData.append("desgaste_ferramenta", document.getElementById("desgaste_ferramenta").value);
    formData.append("twf", document.getElementById("twf").value);
    formData.append("hdf", document.getElementById("hdf").value);
    formData.append("pwf", document.getElementById("pwf").value);
    formData.append("osf", document.getElementById("osf").value);
    formData.append("rnf", document.getElementById("rnf").value);

    fetch("http://127.0.0.1:5000/equipamento", {
        method: "POST",
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            const resultado = data.resultado;
            const mensagem = resultado === 1 ? "⚠️ Equipamento em falha" : "✅ Equipamento em operação normal";
            alert(mensagem);
            limparCampos();
            document.getElementById("tabelaEquipamentos").innerHTML = `
                <tr>
                    <th>Nome</th><th>Ar (K)</th><th>Processo (K)</th><th>RPM</th><th>Torque</th><th>Desgaste</th>
                    <th>TWF</th><th>HDF</th><th>PWF</th><th>OSF</th><th>RNF</th><th>Diagnóstico</th><th>Remover</th>
                </tr>`;
            carregarEquipamentos();
        });
}

// Adiciona linha à tabela com botão deletar
function inserirTabela(e) {
    const tabela = document.getElementById("tabelaEquipamentos");
    const row = tabela.insertRow();
    row.innerHTML = `
        <td>${e.nome}</td>
        <td>${e.temperatura_ar}</td>
        <td>${e.temperatura_processo}</td>
        <td>${e.rpm}</td>
        <td>${e.torque}</td>
        <td>${e.desgaste_ferramenta}</td>
        <td>${e.twf}</td>
        <td>${e.hdf}</td>
        <td>${e.pwf}</td>
        <td>${e.osf}</td>
        <td>${e.rnf}</td>
        <td style="font-weight:bold; color:${e.resultado === 1 ? 'red' : 'green'}">${e.resultado === 1 ? 'FALHA' : 'NORMAL'}</td>
        <td><button onclick="removerEquipamento(${e.id})" class="close">×</button></td>
    `;
}

// Remove equipamento por ID
function removerEquipamento(id) {
    if (!confirm("Tem certeza que deseja remover este registro?")) return;
    fetch(`http://127.0.0.1:5000/equipamento?id=${id}`, {
        method: "DELETE"
    })
        .then(() => {
            document.getElementById("tabelaEquipamentos").innerHTML = `
                <tr>
                    <th>Nome</th><th>Ar (K)</th><th>Processo (K)</th><th>RPM</th><th>Torque</th><th>Desgaste</th>
                    <th>TWF</th><th>HDF</th><th>PWF</th><th>OSF</th><th>RNF</th><th>Diagnóstico</th><th>Remover</th>
                </tr>`;
            carregarEquipamentos();
        });
}

// Limpa inputs
function limparCampos() {
    const campos = ["nome", "temperatura_ar", "temperatura_processo", "rpm", "torque",
                    "desgaste_ferramenta", "twf", "hdf", "pwf", "osf", "rnf"];
    campos.forEach(id => document.getElementById(id).value = "");
}