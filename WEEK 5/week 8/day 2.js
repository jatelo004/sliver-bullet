// === Simulated Python Backend ===
const pythonBackend = {
  checkins: [],

  GET: async (path) => {
    if (path === "/api/checkins") {
      return { status: 200, body: pythonBackend.checkins };
    }
    if (path.startsWith("/api/checkins/")) {
      const name = decodeURIComponent(path.split("/")[3]);
      const records = pythonBackend.checkins.filter(c => c.name === name);
      if (!records.length) return { status: 404, body: { error: "Not found" } };
      return { status: 200, body: records };
    }
    return { status: 404, body: { error: "Route not found" } };
  },

  POST: async (path, payload) => {
    if (path === "/api/checkins") {
      const entry = {
        ...payload,
        hit_goal: payload.steps >= 10000,
        rating:   payload.sleep >= 7.5 && payload.water >= 8 && payload.steps >= 10000
                    ? "Excellent"
                    : payload.steps >= 10000 ? "Good" : "Below target",
        id: pythonBackend.checkins.length + 1
      };
      pythonBackend.checkins.push(entry);
      return { status: 201, body: { success: true, entry } };
    }
    return { status: 404, body: { error: "Route not found" } };
  }
};

// Adapter: makes pythonBackend look like fetch()
const apiFetch = async (path, options = {}) => {
  const method = (options.method || "GET").toUpperCase();
  const payload = options.body ? JSON.parse(options.body) : undefined;
  const result  = method === "POST"
    ? await pythonBackend.POST(path, payload)
    : await pythonBackend.GET(path);
  return { ok: result.status < 400, status: result.status, json: async () => result.body };
};

// === JavaScript Frontend ===
const submitCheckIn = async (data) => {
  const res = await apiFetch("/api/checkins", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
};

const loadCheckIns = async () => {
  const res = await apiFetch("/api/checkins");
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
};

// Submit three check-ins
const entries = [
  { name: "Brian Otieno",    sleep: 8.0, water: 10, steps: 12100 },
  { name: "Wanjiku Muthoni", sleep: 5.5, water:  4, steps:  7800 },
  { name: "Kamau Njoroge",   sleep: 7.5, water:  9, steps: 10050 },
];

for (const entry of entries) {
  const result = await submitCheckIn(entry);
  console.log(`POST /api/checkins --> 201`);
  console.log(`  Stored: ${result.entry.name} | Goal: ${result.entry.hit_goal ? "HIT" : "MISS"} | Rating: ${result.entry.rating}`);
}

// Load all
console.log("\nGET /api/checkins --> 200");
const all = await loadCheckIns();
console.log(`  Total records: ${all.length}`);
all.forEach(c => {
  console.log(`  [${c.id}] ${c.name} | ${c.rating}`);
});
