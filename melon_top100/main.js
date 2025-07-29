// melon_top100/main.js

const DATA_URL = 'https://pyhub.kr/melon/20231204.json';

async function fetchMelonData() {
  const res = await fetch(DATA_URL);
  if (!res.ok) throw new Error('데이터를 불러오지 못했습니다.');
  return await res.json();
}

function renderTable(data) {
  const table = document.createElement('table');
  const thead = document.createElement('thead');
  thead.innerHTML = `<tr>
    <th>순위</th>
    <th>곡명</th>
    <th>아티스트</th>
    <th>앨범</th>
  </tr>`;
  table.appendChild(thead);
  const tbody = document.createElement('tbody');
  data.forEach(item => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${item.rank}</td>
      <td>${item.title}</td>
      <td>${item.artist}</td>
      <td>${item.album}</td>
    `;
    tbody.appendChild(tr);
  });
  table.appendChild(tbody);
  return table;
}

function renderArtistChart(data) {
  // 아티스트별 곡 수 집계
  const artistCount = {};
  data.forEach(item => {
    artistCount[item.artist] = (artistCount[item.artist] || 0) + 1;
  });
  // 상위 10명만
  const sorted = Object.entries(artistCount).sort((a,b)=>b[1]-a[1]).slice(0,10);
  const labels = sorted.map(x=>x[0]);
  const counts = sorted.map(x=>x[1]);
  const ctx = document.getElementById('artistChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels,
      datasets: [{
        label: '아티스트별 곡 수 (상위 10명)',
        data: counts,
        backgroundColor: '#60a5fa',
      }]
    },
    options: {
      plugins: { legend: { display: false } },
      scales: {
        x: { title: { display: true, text: '아티스트' } },
        y: { title: { display: true, text: '곡 수' }, beginAtZero: true, stepSize: 1 }
      }
    }
  });
}

async function main() {
  try {
    const data = await fetchMelonData();
    const tableArea = document.getElementById('table-area');
    tableArea.innerHTML = '';
    tableArea.appendChild(renderTable(data));
    renderArtistChart(data);
  } catch (e) {
    document.getElementById('table-area').textContent = e.message;
  }
}

main();
