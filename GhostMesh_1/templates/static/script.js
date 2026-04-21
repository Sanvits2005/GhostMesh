let attackerData = [];
let defenderData = [];
let labels = [];

const ctx = document.getElementById('chart').getContext('2d');

const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [
            { label: 'Attacker', data: attackerData },
            { label: 'Defender', data: defenderData }
        ]
    }
});

async function loadLogs() {
    const res = await fetch('/logs');
    const data = await res.json();

    const table = document.getElementById("logTable");
    table.innerHTML = "";

    let breach = false;

    data.logs.reverse().forEach(log => {
        if (log.status.includes("Breached")) breach = true;

        table.innerHTML += `
            <tr>
                <td>${log.id}</td>
                <td>${log.attack}</td>
                <td style="color:${log.status.includes('Breached') ? 'orange' : 'green'}">
                    ${log.status}
                </td>
                <td>${log.confidence}%</td>
            </tr>
        `;
    });

    document.getElementById("score").innerText =
        `Attacker: ${data.attacker} ⚔️ | Defender: ${data.defender} 🛡️`;

    labels.push("");
    attackerData.push(data.attacker);
    defenderData.push(data.defender);

    if (labels.length > 20) {
        labels.shift();
        attackerData.shift();
        defenderData.shift();
    }

    chart.update();

    if (breach) {
        document.getElementById("alertSound").play();
    }
}

setInterval(loadLogs, 2000);