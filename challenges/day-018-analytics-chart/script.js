const DATA = {
  web: {
    label: 'Web',
    ranges: {
      7: {
        users: '42,120',
        conversion: '4.6%',
        revenue: '$128,490',
        session: '4m 32s',
        trend: [38, 40, 45, 52, 49, 57, 64],
        sources: [
          { name: 'Organic', value: 46 },
          { name: 'Email', value: 18 },
          { name: 'Paid', value: 23 },
          { name: 'Direct', value: 13 },
        ],
        summary: 'Web visits rise steadily midweek with strong organic lift and improved retention.',
      },
      30: {
        users: '182,404',
        conversion: '4.2%',
        revenue: '$612,990',
        session: '4m 21s',
        trend: [32, 36, 35, 42, 38, 45, 47, 50, 52, 48, 55, 59, 57, 61, 60, 64, 68, 66, 72, 69, 74, 78, 80, 83, 79, 85, 88, 86, 90, 92],
        sources: [
          { name: 'Organic', value: 44 },
          { name: 'Email', value: 21 },
          { name: 'Paid', value: 20 },
          { name: 'Referral', value: 15 },
        ],
        summary:
          'Month over month growth is positive; paid search stabilized while email re-engagement strengthened.',
      },
      90: {
        users: '564,010',
        conversion: '3.9%',
        revenue: '$1,742,120',
        session: '4m 07s',
        trend: [52, 48, 50, 46, 49, 53, 50, 55, 57, 58, 55, 61, 60, 63, 59, 64, 68, 65, 69, 71, 72, 70, 74, 73, 78, 76, 81, 85, 82, 86, 88, 87, 90, 92, 91, 94, 96, 98, 100, 97, 95, 99, 102, 101, 106, 104, 108, 109, 112, 107, 111, 114, 117, 119, 121, 124, 121, 127, 130, 128, 134, 133, 139, 136, 142, 140, 145, 149, 152, 150, 154, 157, 161, 159, 164, 167, 170, 173, 176, 180, 178, 182, 185, 188, 192, 195, 198, 203, 201, 205, 209, 212, 216, 220, 223, 226, 228, 230, 232],
        sources: [
          { name: 'Organic', value: 52 },
          { name: 'Email', value: 17 },
          { name: 'Paid', value: 18 },
          { name: 'Social', value: 13 },
        ],
        summary: 'Over three months, traffic volume improved steadily with seasonal variation in paid campaigns.',
      },
    },
  },
  app: {
    label: 'App',
    ranges: {
      7: {
        users: '29,870',
        conversion: '6.1%',
        revenue: '$94,760',
        session: '3m 55s',
        trend: [28, 33, 40, 44, 50, 48, 56],
        sources: [
          { name: 'Push', value: 33 },
          { name: 'Organic', value: 29 },
          { name: 'Referral', value: 26 },
          { name: 'Paid', value: 12 },
        ],
        summary: 'App users convert better with sharp growth from push re-engagement, especially late in the week.',
      },
      30: {
        users: '126,301',
        conversion: '6.4%',
        revenue: '$378,220',
        session: '3m 48s',
        trend: [31, 30, 34, 39, 42, 46, 45, 52, 56, 54, 58, 63, 61, 66, 69, 72, 70, 74, 76, 79, 84, 86, 88, 90, 94, 97, 100, 103, 108, 109],
        sources: [
          { name: 'Push', value: 36 },
          { name: 'Organic', value: 25 },
          { name: 'Referral', value: 23 },
          { name: 'Paid', value: 16 },
        ],
        summary: 'The app cohort stays consistently stronger in conversion, driven by in-app reminders.',
      },
      90: {
        users: '398,100',
        conversion: '6.0%',
        revenue: '$1,120,540',
        session: '3m 52s',
        trend: [34, 33, 35, 37, 39, 41, 40, 44, 46, 48, 49, 51, 52, 55, 56, 58, 59, 63, 64, 66, 70, 72, 71, 74, 76, 79, 82, 84, 86, 88, 90, 93, 95, 97, 98, 100, 102, 104, 107, 108, 111, 112, 114, 117, 118, 121, 123, 126, 129, 130, 133, 135, 137, 139, 142, 144, 146, 149, 152, 154, 156, 159, 161, 163, 166, 168, 171, 173, 176, 179, 181, 183, 186, 188, 191, 194, 196, 198, 202, 205, 208, 211, 214, 217, 220, 223, 227, 230, 233, 236, 240, 243, 246, 249, 252, 255, 259, 262, 265, 268],
        sources: [
          { name: 'Push', value: 39 },
          { name: 'Organic', value: 23 },
          { name: 'Referral', value: 22 },
          { name: 'Paid', value: 16 },
        ],
        summary: 'App traffic remains high-quality and steady, with conversion above site averages.',
      },
    },
  },
  store: {
    label: 'Store',
    ranges: {
      7: {
        users: '19,410',
        conversion: '9.3%',
        revenue: '$216,840',
        session: '5m 11s',
        trend: [30, 39, 42, 51, 58, 62, 69],
        sources: [
          { name: 'Direct', value: 27 },
          { name: 'Retargeting', value: 35 },
          { name: 'Email', value: 22 },
          { name: 'Affiliate', value: 16 },
        ],
        summary: 'E-commerce peaks sharply in the final two days of the window and keeps checkout conversion high.',
      },
      30: {
        users: '88,220',
        conversion: '9.8%',
        revenue: '$901,420',
        session: '5m 27s',
        trend: [34, 38, 44, 48, 52, 56, 60, 65, 63, 68, 71, 74, 77, 80, 84, 83, 87, 90, 94, 96, 99, 103, 106, 110, 114, 118, 120, 123, 127, 131],
        sources: [
          { name: 'Direct', value: 31 },
          { name: 'Retargeting', value: 29 },
          { name: 'Email', value: 25 },
          { name: 'Affiliate', value: 15 },
        ],
        summary: 'Store demand is strongest on campaign days; retargeting and email remain the highest contributors.',
      },
      90: {
        users: '261,900',
        conversion: '9.4%',
        revenue: '$2,742,760',
        session: '5m 03s',
        trend: [37, 36, 40, 43, 48, 52, 53, 56, 61, 60, 63, 66, 68, 72, 75, 77, 79, 83, 86, 88, 92, 95, 97, 99, 101, 104, 107, 110, 113, 117, 120, 123, 127, 129, 132, 135, 138, 141, 145, 147, 150, 153, 156, 159, 162, 166, 169, 171, 174, 178, 181, 183, 187, 190, 193, 197, 200, 203, 206, 209, 212, 216, 219, 223, 226, 228, 231, 235, 238, 241, 244, 248, 252, 255, 258, 262, 265, 268, 272, 276, 279, 283, 286, 289, 294, 297, 301, 304, 308, 311],
        sources: [
          { name: 'Direct', value: 34 },
          { name: 'Retargeting', value: 28 },
          { name: 'Email', value: 23 },
          { name: 'Affiliate', value: 15 },
        ],
        summary: 'E-commerce shows the strongest conversion curve over time, with sessions clustering around high-value promotions.',
      },
    },
  },
};

const DEFAULT_CHANNEL = 'web';
const DEFAULT_RANGE = '7';

const state = {
  channel: DEFAULT_CHANNEL,
  range: DEFAULT_RANGE,
};

const metricUsers = document.getElementById('metric-users');
const metricConversion = document.getElementById('metric-conversion');
const metricRevenue = document.getElementById('metric-revenue');
const metricSession = document.getElementById('metric-session');
const trendLine = document.getElementById('trend-line');
const trendPoints = document.getElementById('trend-points');
const trendGrid = document.getElementById('trend-grid');
const trendAxis = document.getElementById('trend-axis');
const trendSummary = document.getElementById('trend-summary');
const barsWrap = document.getElementById('source-bars');
const statusScope = document.getElementById('status-scope');
const statusRange = document.getElementById('status-range');
const trendCaption = document.getElementById('trend-caption');

function drawGrid() {
  trendGrid.innerHTML = '';
  const lines = 4;
  const height = 140;
  for (let i = 0; i <= lines; i++) {
    const y = 30 + (height / lines) * i;
    const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line.setAttribute('x1', '20');
    line.setAttribute('y1', y.toString());
    line.setAttribute('x2', '580');
    line.setAttribute('y2', y.toString());
    trendGrid.appendChild(line);
  }
}

function renderAxis(labels) {
  trendAxis.innerHTML = '';
  const width = 560;
  const leftPadding = 20;
  const usableWidth = width - leftPadding;

  labels.forEach((label, index) => {
    const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    const x = leftPadding + (usableWidth / (labels.length - 1)) * index;
    text.setAttribute('x', x);
    text.setAttribute('y', '207');
    text.setAttribute('text-anchor', 'middle');
    text.textContent = label;
    trendAxis.appendChild(text);
  });
}

function pathFromSeries(values) {
  const width = 560;
  const height = 140;
  const leftPadding = 20;
  const topPadding = 30;
  const usableWidth = width - leftPadding;

  const min = Math.min(...values);
  const max = Math.max(...values);
  const range = Math.max(1, max - min);

  const points = values.map((value, index) => {
    const x = leftPadding + (usableWidth / (values.length - 1)) * index;
    const y = topPadding + height - ((value - min) / range) * height;
    return `${x},${y}`;
  });

  return points.join(' ');
}

function renderTrend(values, labels) {
  drawGrid();
  renderAxis(labels);
  trendLine.setAttribute('d', `M ${pathFromSeries(values).replace(/,/g, ' ')}`);
  trendLine.style.stroke = 'var(--accent)';

  trendPoints.innerHTML = '';
  const width = 560;
  const height = 140;
  const leftPadding = 20;
  const topPadding = 30;
  const usableWidth = width - leftPadding;
  const min = Math.min(...values);
  const max = Math.max(...values);
  const range = Math.max(1, max - min);

  values.forEach((value, index) => {
    const x = leftPadding + (usableWidth / (values.length - 1)) * index;
    const y = topPadding + height - ((value - min) / range) * height;
    const point = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    point.setAttribute('cx', x);
    point.setAttribute('cy', y);
    point.setAttribute('r', '4');
    point.setAttribute('fill', '#0f172a');
    trendPoints.appendChild(point);
  });
}

function renderBars(sources) {
  barsWrap.innerHTML = '';
  const max = Math.max(...sources.map((entry) => entry.value));

  sources.forEach((entry) => {
    const item = document.createElement('div');
    item.className = 'bar-item';
    item.setAttribute('role', 'listitem');

    const top = document.createElement('div');
    top.className = 'bar-top';
    const name = document.createElement('span');
    name.textContent = entry.name;
    const percent = document.createElement('span');
    percent.textContent = `${entry.value}%`;

    top.append(name, percent);

    const track = document.createElement('div');
    track.className = 'bar-track';
    const fill = document.createElement('div');
    fill.className = 'bar-fill';
    fill.style.width = '0%';
    track.appendChild(fill);

    item.append(top, track);
    barsWrap.appendChild(item);

    requestAnimationFrame(() => {
      fill.style.width = `${(entry.value / max) * 100}%`;
    });
  });
}

function renderAll() {
  const current = DATA[state.channel].ranges[state.range];

  metricUsers.textContent = current.users;
  metricConversion.textContent = current.conversion;
  metricRevenue.textContent = current.revenue;
  metricSession.textContent = current.session;
  trendSummary.textContent = current.summary;

  const periodLabel = state.range === '7' ? '7 days' : `${state.range} days`;
  statusScope.textContent = DATA[state.channel].label;
  statusRange.textContent = periodLabel;
  trendCaption.textContent = `${periodLabel} trend by index period`;

  const labels = state.range === '7' ? 'Mon Tue Wed Thu Fri Sat Sun'.split(' ') : state.range === '30'
    ? ['Week 1', 'Week 2', 'Week 3', 'Week 4']
    : ['Month 1', 'Month 2', 'Month 3'];

  renderBars(current.sources);
  renderTrend(current.trend, labels);
}

function updateChannel(newChannel) {
  state.channel = newChannel;
  document.querySelectorAll('[data-channel]').forEach((button) => {
    const active = button.dataset.channel === newChannel;
    button.classList.toggle('active', active);
    button.setAttribute('aria-pressed', String(active));
  });
  renderAll();
}

function updateRange(newRange) {
  state.range = newRange;
  document.querySelectorAll('[data-range]').forEach((button) => {
    const active = button.dataset.range === newRange;
    button.classList.toggle('active', active);
    button.setAttribute('aria-pressed', String(active));
  });
  renderAll();
}

function bindControls() {
  document.querySelectorAll('[data-channel]').forEach((button) => {
    button.addEventListener('click', () => {
      updateChannel(button.dataset.channel);
    });
  });

  document.querySelectorAll('[data-range]').forEach((button) => {
    button.addEventListener('click', () => {
      updateRange(button.dataset.range);
    });
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft' && document.activeElement?.dataset?.channel) {
      const buttons = [...document.querySelectorAll('[data-channel]')];
      const index = buttons.indexOf(document.activeElement);
      const target = buttons[(index + buttons.length - 1) % buttons.length];
      target.focus();
      target.click();
    }

    if (event.key === 'ArrowRight' && document.activeElement?.dataset?.channel) {
      const buttons = [...document.querySelectorAll('[data-channel]')];
      const index = buttons.indexOf(document.activeElement);
      const target = buttons[(index + 1) % buttons.length];
      target.focus();
      target.click();
    }
  });
}

bindControls();
renderAll();
